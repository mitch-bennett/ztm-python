# convert jpg to png
# want to give two arguments from CLI while calling
# 1st: give it the input folder of jpg files
# 2nd: give it the output folder name to store png files

import sys
import os
from PIL import Image

# grab first and second argument
# input_folder = sys.argv[1]
# output_folder = sys.argv[2]
input_folder = "Pokedex"
output_folder = "PokePNG"

# get current dir
dir_path = os.path.dirname(os.path.realpath(__file__))

# check is new/exists, if not create (folder)
if not os.path.isdir(os.path.join(dir_path, output_folder)):
    os.makedirs(os.path.join(dir_path, output_folder))

input_files = os.path.join(dir_path, input_folder)
output_files = os.path.join(dir_path, output_folder)
input_ext = (".jpg", ".jpeg")
output_ext = ".png"

# loop through pokedex
# convert images to png
# save to new folder
for root, dirs, files in os.walk(input_files):
    # jpg_filename = os.fsdecode(jpg_file)
    for jpg_file in files:
        if jpg_file.endswith(input_ext):
            jpg_filename = os.path.splitext(jpg_file)[0]
            ext = os.path.splitext(jpg_file)[-1]
            savepath = os.path.join(output_files, jpg_filename + output_ext)
            img = Image.open(os.path.join(root, jpg_file))
            img.save(savepath, "png")


# # alternate method:
# for filename in os.listdir(input_files):
#     img = Image.open(f"{input_files}/{filename}")
#     clean_name = os.path.splitext(filename)[0]
#     img.save(f"{output_files}/{clean_name}.png", "png")
