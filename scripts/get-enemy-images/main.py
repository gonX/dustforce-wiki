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

production = False # should be True when committed to git since files don't get generated consistently

import frontmatter
import ffmpeg
import glob

import unidecode
import re

import os
import subprocess
topdir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').rstrip()
sprites_dir = os.path.join(topdir, "raw-assets", "sprites")

video_output_dir = os.path.join(topdir, "website/assets/video/enemies")

framerate = 6 # TODO: this seems to be sprite-specific, but Dustcourse uses 6

for f in glob.glob(os.path.join(topdir, 'website/_enemies/**/*.md')):
    with open(f) as postFile:
        enemy, _ = frontmatter.parse(postFile.read())
        print(enemy["name"].rjust(30), end=": ")

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

        outputName = re.sub(r'[\W_]+', '-', unidecode.unidecode(enemy["name"]).lower()).strip('-')

        glob_path = os.path.join(sprites_dir, "entities") + "/**/" + spriteFolderName + "/" + spriteName + "*.png"

        if not glob.glob(glob_path):
            print("no images found in glob '{}'".format(glob_path))
            continue

        output_path = video_output_dir + "/" + outputName + ".webm"
        if production and os.path.isfile(output_path) and os.path.isfile(output_path[-4:] + "mp4"):
            print("skipped (exists)")
            continue

        try:
            ffm = ffmpeg.input(glob_path, pattern_type='glob', framerate=framerate)
            out1 = ffm.output(output_path, vcodec="libvpx-vp9", bitrate=10000, deadline="best")
            out2 = ffm.output(output_path[:-4] + "mp4", pix_fmt="yuv420p")
            out = ffmpeg.merge_outputs(out1, out2)
            out.overwrite_output().run()
        except:
            print("ffmpeg fail")
            raise
            continue

        print(outputName)


