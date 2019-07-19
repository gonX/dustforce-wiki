#!/usr/bin/env python3
#
#  manually:
# to mp4:
#   ffmpeg -framerate 5 -pattern_type glob -i 'idle*.png' -c:v libx264 -r 5 -pix_fmt yuv420p idle.mp4
# to webm:
#   ffmpeg -framerate 5 -pattern_type glob -i 'idle*.png' -c:v libvpx-vp9 -deadline best -b:v 10k -r 5 idle.webm
#
# cropping seems to produce larger sizes, so let's just keep a consistent size
# it is however possible to detect cropping size using ffmpeg, however this seems inconsistent:
#   ffmpeg -pattern_type glob -i 'idle*.png' -filter cropdetect=limit=0:round=2 -f null - 2>&1
#
# webp/apng however has lower resource usage so we'll be using that instead

production = True # should be True when committed to git since files don't get generated consistently

import frontmatter
import apng as APNG
import glob

import re

from PIL import Image
import io

import os
import subprocess
topdir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').rstrip()
sprites_dir = os.path.join(topdir, "raw-assets", "sprites")

video_output_dir = os.path.join(topdir, "website/assets/video/enemies")

framerate = 6 # TODO: this seems to be sprite-specific, but Dustcourse uses 6

for f in glob.glob(os.path.join(topdir, 'website/_enemies/**/*.md')):
    with open(f) as postFile:
        webp = []
        bboxes = []
        apng = APNG.APNG()
        enemy, _ = frontmatter.parse(postFile.read())
        print(enemy["name"].rjust(30), end=": ")
        output_name = re.sub(r'[\W_]+', '-', enemy["name"].lower()).strip('-')
        output_path_apng = video_output_dir + "/" + output_name + ".png"
        output_path_webp = video_output_dir + "/" + output_name + ".webp"

        if production and os.path.isfile(output_path_apng) and os.path.isfile(output_path_webp):
            print("skipped (exists)")
            continue

        if "sprite_folder_name" in enemy:
            # hardcoded folder name for enemy
            spriteFolderName = enemy["sprite_folder_name"]
        elif "game_name" not in enemy:
            print("no game_name")
            continue
        else:
            # trim first 6 characters because it always starts with 'enemy_'
            spriteFolderName = enemy["game_name"][6:]

        if "sprite_image_name" in enemy:
            spriteName = enemy["sprite_image_name"]
        else:
            spriteName = "idle"

        glob_path = os.path.join(sprites_dir, "entities") + "/**/" + spriteFolderName + "/" + spriteName + "*.png"

        if not glob.glob(glob_path):
            print("no images found in glob '{}'".format(glob_path))
            continue

        # get bounding box to use for all images in this collection
        for pngf in glob.glob(glob_path):
            image = Image.open(pngf)
            bboxes.append(image.getbbox())

        bboxL = min(bboxes,key=lambda item:item[0])[0]
        bboxU = min(bboxes,key=lambda item:item[1])[1]
        bboxR = max(bboxes,key=lambda item:item[2])[2]
        bboxD = max(bboxes,key=lambda item:item[3])[3]

        # crop and convert PNG's to appropriate animated formats
        for pngf in glob.glob(glob_path):
            ba = io.BytesIO()
            image = Image.open(pngf)

            crop = image.crop((bboxL, bboxU, bboxR, bboxD))

            output = crop

            output.save(ba, format='PNG')
            #output.save("tmp/{}-{}".format(output_name, os.path.basename(pngf)), format='PNG')
            webp.append(output)
            apng.append(APNG.PNG.from_bytes(ba.getvalue()), delay=int(1000/framerate))

        apng.save(output_path_apng)
        webp[0].save(output_path_webp, save_all=True, append_images=webp[1:],
                duration=int(1000/framerate), loop=0, minimize_size=True,
                quality=60)

        print(output_name)
