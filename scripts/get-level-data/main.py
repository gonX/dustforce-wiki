#!/usr/bin/env python3
# needs 'pip install --user dustmaker'

from dustmaker import *
import json
import sys
import os
import copy
import requests

import wiki_output_format

records_url = "https://dustkid.com/json/records"
records = {}
print(f"Pulling record data from {records_url}")
exit
jsonobj = requests.get(records_url).json()
for x in jsonobj["Scores"]:
    mapoutput = {}
    for y in jsonobj:
        mapobj = jsonobj[y][x]
        mapoutput["best_" + y[:-1].lower() + "_time_ms"] = mapobj["time"]
        mapoutput["best_" + y[:-1].lower() + "_timestamp_epoch"] = mapobj["timestamp"]
        mapoutput["best_" + y[:-1].lower() + "_username"] = mapobj["username"]
        mapoutput["best_" + y[:-1].lower() + "_character"] = wiki_output_format.Character(mapobj["character"])
        mapoutput["best_" + y[:-1].lower() + "_replay_id"] = mapobj["replay_id"]

    records[x] = mapoutput

def generateMapData(mapfile):
    with open(mapfile, "rb") as f:
        map = read_map(f.read())
        print("Reading map '{}' ({})".format(map.name(), os.path.basename(mapfile)))

        output = copy.deepcopy(wiki_output_format.output_format)
        output["name"] = map.name()
        output["srcfile"] = os.path.basename(mapfile)
        output["key_get_type"] = wiki_output_format.Keytype(map.vars["key_get_type"].value)
        output["props"] = len(map.props)
        # keep in mind Beginner Tutorial does not have the flag, but the game is hardcoded to use it
        if "Beginner Tutorial" in map.name():
            output["is_virtual"] = True
        else:
            output["is_virtual"] = map.virtual_character()

        # tile layers
        for ((layer, x, y), tile) in map.tiles.items():
            output_key = "tiles_layer" + str(layer)
            if not output_key in output:
                output[output_key] = 0
                print("Tile layer {} is not in wiki_output_format!".format(layer), file=sys.stderr)
            output[output_key] += 1
            # dust check
            if tile.has_filth():
                output["covered_tiles"] += 1
                # check all faces of tile for "filth"
                for orientation in TileSide:
                    if tile.edge_filth_sprite(orientation)[0] == TileSpriteSet.none_0:
                        continue
                    if tile.edge_filth_sprite(orientation)[1]:
                        output["spiked_surfaces"] += 1
                    else:
                        output["filthy_surfaces"] += 1
            output["dustblocks"] += tile.is_dustblock()

        # enemies
        for (id, (x, y, entity)) in list(map.entities.items()):
            if isinstance(entity, Enemy):
                output["enemies"] += 1
                output["dust_from_enemies"] += entity.combo()
                if not entity.TYPE_IDENTIFIER in output:
                    output[entity.TYPE_IDENTIFIER] = 0
                    print("Enemy {} is not in wiki_output_format!".format(entity.TYPE_IDENTIFIER), file=sys.stderr)
                output[entity.TYPE_IDENTIFIER] += 1
            if isinstance(entity, Apple):
                output["apples"] += 1

        output["total_dust"] = output["dust_from_enemies"] + output["dustblocks"] + output["filthy_surfaces"]

        # scores
        if output["srcfile"] in records:
            output.update(records[output["srcfile"]])

        return output


# non-multithreaded takes 1:19 minutes on an OC'd 4770k
# multithreaded takes 23s wall time but 2:30 minutes cpu time

if __name__ == '__main__':
    from joblib import Parallel, delayed
    import multiprocessing
    import subprocess

    localpath = "/home/gonx/.steam/steam/steamapps/common/Dustforce/content/levels2/"

    num_cores = multiprocessing.cpu_count()

    results = Parallel(n_jobs=num_cores)(delayed(generateMapData)(current_map) for current_map in [localpath + f for f in os.listdir(localpath) if os.path.isfile(os.path.join(localpath, f))])

    topdir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').rstrip()
    with open(os.path.join(topdir, "website", "_data", "stock-maps.json"), 'w+') as f:
        f.write(json.dumps(sorted(results,key=lambda x: x["srcfile"].lower()), indent=2))
        print("File written to '{}'".format(f.name))
