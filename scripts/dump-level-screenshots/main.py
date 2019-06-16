#!/usr/bin/env python3
# needs 'pip install --user dustmaker'

from dustmaker import *
import os

def dumpPNG(mapfile):
    with open(mapfile, "rb") as f:
        map = read_map(f.read())
        print("Reading map '{}' ({})".format(map.name(), os.path.basename(mapfile)))
        if map.parent:
            if map.parent.sshot:
                print("Returning PARENT!")
                return map.parent.sshot
        if map.sshot:
            return map.sshot

def outputPNG(mapfile, destpath):
    results = dumpPNG(mapfile)
    if not results:
        print("Skipping empty screenshot for '{}'".format(os.path.basename(mapfile)))
    else:
        with open(os.path.join(destpath, os.path.basename(mapfile) + ".png"), "wb+") as outf:
            outf.write(results)
            print("File written to '{}'".format(outf.name))

if __name__ == '__main__':
    from joblib import Parallel, delayed
    import multiprocessing
    import subprocess

    localpath = "/home/gonx/.steam/steam/steamapps/common/Dustforce/content/levels2/"
    num_cores = multiprocessing.cpu_count()
    topdir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').rstrip()
    destpath = os.path.join(topdir, "website", "assets", "img", "maps")
    Parallel(n_jobs=num_cores)(delayed(outputPNG)(current_map, destpath) for current_map in [localpath + f for f in os.listdir(localpath) if os.path.isfile(os.path.join(localpath, f))])
    print("Done")
