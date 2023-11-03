#!/usr/bin/python3

import requests

down_iter = 0
url = 'https://images.unsplash.com/photo-1696075619078-6cb640d329ec?auto=format&fit=crop&q=80&w=1000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw3fHx8ZW58MHx8fHx8'  # Replace with your specific URL
response = requests.get(url, stream=True)
path = './download' 
if response.status_code == 200:
    file_path = './download/' + 'img' + str(down_iter) + '.jpeg' 
    with open(file_path, 'wb') as output_file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                output_file.write(chunk)
    print("Download complete.")
else:
    print("Request failed with status code:", response.status_code)
