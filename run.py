import os
import requests
import re

desc_path = 'supplier-data/descriptions/'
image_path = 'supplier-data/images/'

text_files = sorted(os.listdir(desc_path))
jpeg_images = sorted([image_name for image_name in os.listdir(image_path) if '.jpeg' in image_name])

list_content = []
image_counter = 0

for file in text_files:
    #Make a format that keep the title, name, weight (in lbs), and description as keys for the content value, respectively
    format = ['name', 'weight', 'description']

    with open(desc_path + file, 'r') as f:
        data = {}
        #We will read only the first 3 line, because there is empty lines in the end of file
        contents = f.read().split("\n")[0:3]

        #We will define the weight field as an integer field
        contents[1] = int((re.search(r'\d+', contents[1])).group())

        counter = 0
        for content in contents:
            data[format[counter]] = content
            counter += 1
        
        """
        The image_name field will allow the system to find the image associated with the fruit
        Don't forget to add all fields, including the image_name!
        """
        data['image_name'] = jpeg_images[image_counter]

        list_content.append(data)
        image_counter += 1

for item in list_content:
    #Use the Python requests module to post the dictionary to the website
    resp = requests.post('http://35.232.113.195/fruits/', json = item)

    #Print the status_code and text of the response objects to check out what's going on
    if resp.status_code != 201:
        raise Exception('POST error status = {}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))