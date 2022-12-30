# image processing with python
# google friend: OpenCV, pillow
# for this exercise, pip install pillow

from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

# common structure of the img type
# print(dir(img))
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# add filters such as blur and sharpen, and save as new file
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("sharpen.png", "png")

# convert to different colorspace
bw_img = img.convert("L")
bw_img.save("grey.png", "png")
