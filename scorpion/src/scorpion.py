#!/usr/bin/python3

import pycountry
from exif import Image
import reverse_geocoder as rg

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

#Additional Information
for index, image in enumerate(images):
    print(f"Lens and OS - Image {index}")
    print("---------------------")
    print(f"Lens make: {image.get('lens_make', 'Unknown')}")
    print(f"Lens model: {image.get('lens_model', 'Unknown')}")
    print(f"Lens specification: {image.get('lens_specification', 'Unknown')}")
    print(f"OS version: {image.get('software', 'Unknown')}\n")

#Date and time when the photo was taken
for index, image in enumerate(images):
    print(f"Date/time taken - Image {index}")
    print("-------------------------")
    print(f"{image.get('datetime_original','Not Specified')}.{image.get('subsec_time_original', 'Not Specified')} {image.get('offset_time', 'Not Specified')}\n")

#Getting the photo’s GPS coordinates
def format_dms_coordinates(coordinates):
    return f"{coordinates[0]}° {coordinates[1]}\' {coordinates[2]}\""

def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + \
                      coordinates[1] / 60 + \
                      coordinates[2] / 3600
    
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees
    
    return decimal_degrees

for index, image in enumerate(images):
    print(f"Coordinates - Image {index}")
    print("---------------------")
    if hasattr(image, "gps_latitude") and hasattr(image, "gps_longitude"):
        # Access attributes using getattr or directly
        print(f"Latitude (DMS): {format_dms_coordinates(getattr(image, 'gps_latitude'))}{getattr(image, 'gps_latitude_ref')}")
        print(f"Longitude (DMS): {format_dms_coordinates(getattr(image, 'gps_longitude'))}{getattr(image, 'gps_longitude_ref')}")
        print(f"Latitude (DD): {dms_coordinates_to_dd_coordinates(getattr(image, 'gps_latitude'), getattr(image, 'gps_latitude_ref'))}")
        print(f"Longitude (DD): {dms_coordinates_to_dd_coordinates(getattr(image, 'gps_longitude'), getattr(image, 'gps_longitude_ref'))}")

def draw_map_for_location(latitude, latitude_ref, longitude, longitude_ref):
    
    decimal_latitude = dms_coordinates_to_dd_coordinates(latitude, latitude_ref)
    decimal_longitude = dms_coordinates_to_dd_coordinates(longitude, longitude_ref)
    url = f"https://www.google.com/maps?q={decimal_latitude},{decimal_longitude}"
    print("Access Location: ", url)

for index, image in enumerate(images):
    if hasattr(image, "gps_latitude") and hasattr(image, "gps_longitude"):
        draw_map_for_location(getattr(image, 'gps_latitude'), 
                          getattr(image, 'gps_latitude_ref'), 
                          getattr(image, 'gps_longitude'),
                          getattr(image, 'gps_longitude_ref'))

#finding country and city of where the pictures was taken
for index, image in enumerate(images):
    print(f"Location info - Image {index}")
    print("-----------------------")
    if hasattr(image, "gps_latitude") and hasattr(image, "gps_longitude"):
        decimal_latitude = dms_coordinates_to_dd_coordinates(getattr(image, 'gps_latitude'), getattr(image, 'gps_latitude_ref'))
        decimal_longitude = dms_coordinates_to_dd_coordinates(getattr(image, 'gps_longitude'), getattr(image, 'gps_longitude_ref'))
        coordinates = (decimal_latitude, decimal_longitude)
        location_info = rg.search(coordinates)[0]
        location_info['country'] = pycountry.countries.get(alpha_2=location_info['cc'])
        print(f"{location_info}\n")

#Update EXIF Data
