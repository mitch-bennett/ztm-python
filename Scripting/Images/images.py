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

# convert to different colorspace. show will display image.
bw_img = img.convert("L")
bw_img.save("grey.png", "png")
# bw_img.show()

# can also rotate images
filtered_img = img.convert("L")
crooked = filtered_img.rotate(180)
crooked.save("rotate.png", "png")

# resizing image takes a tuple for w, h
filtered_img = img.convert("L")
tiny = filtered_img.resize((300, 300))
tiny.save("tiny.png", "png")

# cropping takes a box tuple and apply to region
filtered_img = img.convert("L")
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("cropped.png", "png")

# take massive astro image and make smaller
# pay attention to aspect ratio, which is not locked by default
img = Image.open("./astro.jpg")
new_img = img.resize((400, 400))
new_img.save("astro_thumbnail.jpg")

# this will apply correct scaling. thumbnail modifies current file
# and does not require writing to a new variable
img = Image.open("./astro.jpg")
img.thumbnail((400, 400))
new_img.save("astro_thumbnail-2.jpg")
print(img.size)
