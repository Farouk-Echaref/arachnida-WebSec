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

#check if the images contain EXIF metadata
for index, img in enumerate(images):
    # print(img)
    if img.has_exif:
        status = f"Contains EXIF (Version {img.exif_version}) Data"
    else :
        status = "Does not contain EXIF Data"
    print(f"Image{index}: {status}")

#store available tags
image_members = []
for image in images:
    image_members.append(dir(image))

#print available tags
for index, image_member_list in enumerate(image_members):
    print(f"Image {index} contains {len(image_member_list)} members:")
    print(f"{image_member_list}\n")

#Make and Model of the device used to take the photo
for index, image in enumerate(images):
    print(f"Device Information - Image => {index}: ")
    print("----------------------------")
    print(f"Make: {image.make}")
    print(f"Model: {image.model}\n")