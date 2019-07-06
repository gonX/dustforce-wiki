#!/usr/bin/env python3
import json
import os
import glob
import io
import sys
import numpy as np
from PIL import Image
from dustmaker import *

maps_path = "/home/gonx/.steam/steam/steamapps/common/Dustforce/content/levels2/"

if __name__ == '__main__':
    import subprocess
    topdir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').rstrip()
    sprites_dir = os.path.join(topdir, "raw-assets", "sprites")
    if not os.path.exists(sprites_dir):
        print("""Sprites folder not found!

Due to licensing, please refer to https://pastebin.com/VU41Gt9W for the 'Big .rar archive'
Disregard the other instructions - simply extract it to the 'raw-assets/' directory so that it's presented as 'sprites/'!""")
        sys.exit(1)

    if not os.path.exists(maps_path):
        print("Please set 'maps_path' in this script to your 'levels2/' folder in your Dustforce installation")
        sys.exit(2)

    with open(os.path.join(topdir, "website", "_data", "stock-maps.json"), "r") as f:
        maps = json.loads(f.read())

    names = [m["srcfile"] for m in maps]
    srcfiles_dir = os.path.join(sprites_dir, "area", "icons")

    for n in names:
        found = False
        os.chdir(srcfiles_dir)
        match = glob.glob("**/" + n + "_*.png")
        if n in "wiringfixed": # wiring has "incorrect" name in sprite files
            match = glob.glob("**/wiring_*.png")
        if match:
            if len(match) > 1:
                print("WARN: We matched more than 1 file, but we only care about 1 :o")
            srcpng = Image.open(match[0])
            found = True
            print("sprites   --> {} ".format(n))
        else: # pre-DX levels seem to not use the sprite format, so we extract them via Dustmaker
            mapfile = os.path.join(maps_path, n)
            if os.path.isfile(mapfile):
                with open(mapfile, "rb") as f:
                    m = read_map(f.read())
                    # some maps have empty screenshots anyway, and PIL throws a fit if we give it an empty image
                    if m.sshot:
                        print("dustmaker --> {}".format(n))
                        rgba = np.array(Image.open(io.BytesIO(m.sshot)))
                        rgba[rgba[...,-1]==0] = [255,255,255,0] #convert transparent values to white
                        srcpng = Image.fromarray(rgba)
                        found = True

        if found and srcpng:
            w, h = srcpng.size
            srcpng = srcpng.crop((1,1, w-1, h-1))
            jpg = srcpng.convert('RGB')
            jpg.save(os.path.join(topdir, "website", "assets", "img", "maps", n + ".jpg"), quality=60)
        else:
            print("none found--> {}".format(n))

