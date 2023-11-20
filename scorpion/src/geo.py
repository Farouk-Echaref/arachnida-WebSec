def convert_to_decimal_degrees(coord_tuple):
    degrees, minutes, seconds = coord_tuple
    decimal_degrees = degrees + minutes/60 + seconds/3600
    return decimal_degrees

# Example coordinates
latitude_coords = (34.0, 32.0, 23.999999)
longitude_coords = (4.0, 39.0, 0.0)

# Convert to decimal degrees
latitude = convert_to_decimal_degrees(latitude_coords)
longitude = convert_to_decimal_degrees(longitude_coords)

# Create Google Maps URL
google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

# Print the URL
print("Google Maps URL:", google_maps_url)
