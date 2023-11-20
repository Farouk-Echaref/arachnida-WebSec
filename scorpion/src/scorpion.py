#!/usr/bin/python3

from exif import Image

# load image data
with open("./proto1.jpg", "rb") as proto1_file:
    proto1_img = Image(proto1_file)

with open("./proto2.jpg", "rb") as proto2_file:
    proto2_img = Image(proto2_file)

#store image data in a list
images = [proto1_img, proto2_img]

# print(images[0].list_all())
# print(images[1])

#
for index, img in enumerate(images):
    # print(img)
    if img.has_exif:
        status = f"Contains EXIF (Version {img.exif_version}) Data"
    else :
        status = "Does not contain EXIF Data"
    print(f"Image{index}: {status}")