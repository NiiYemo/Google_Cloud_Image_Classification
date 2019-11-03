"""
Created on Fri Apr 26 22:09:04 2019

@author: yemoQ

'strike' variable is declared. Which will count strikes later.
Setting up the ImageAnnotatorClient(). Which assigns labels to parts of the image
recognised. 
The file path is set with the variable file_name, then it is read
by the 'with' call  working with the io.open command to open image as an image file.
After reading as an image from the file location I need to tell the google cloud vision
it is dealing with an image. 
'response' tells google cloud vision to assign labels to the image.
'labels' simply holds the labels assigned.

I then iterate through the labels in a for loop. If any of the labels match 
the strike is incremented. 

Finally I write to a text file the number of strikes.


"""

import io
import os 

os.system("pip install google-cloud")

import argparse
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="apikey.json"
os.system("exit")



if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    path_help = str('The image to detect, can be web URI, '
                    'Google Cloud Storage, or path to local file.')
    parser.add_argument('image_url', help=path_help)
    args = parser.parse_args()
    path = args.image_url   
    
    client = vision.ImageAnnotatorClient()
    
    strike = 0
    
    if path.startswith('http') or path.startswith('gs:'):
       image = types.Image()
       image.source.image_uri = path
    else:
       
        with io.open(path, 'rb') as image_file:
          content = image_file.read()

          image = types.Image(content=content)
   

    
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels")

    for label in labels:
        if(label.description=="Joint"):
          strike = strike + 1
        if(label.description=="Thigh"):
          strike = strike + 1
        if(label.description=="Muscle"):
          strike = strike + 1
        if(label.description=="Stomach"):
          strike = strike + 1
        if(label.description=="Trunk"):
          strike = strike + 1
        if(label.description=="Barefoot"):
          strike = strike + 1
        if(label.description=="Leg"):
          strike = strike + 1
        if(label.description=="Muscle"):
          strike = strike + 1
        if(label.description=="Neck"):
          strike = strike + 1
        if(label.description=="Flesh"):
          strike = strike + 1
        if(label.description=="Chest"):
          strike = strike + 1
        if(label.description=="Hip"):
          strike = strike + 1    
        if(label.description=="Abdomen"):
          strike = strike + 1
        if(label.description=="Art Model"):
          strike = strike + 1
        
        print(label.description)
   
    print("\n Strikes: ") 
    print(strike)

    
    strikeString=str (strike) 
    file = open("strikes.txt","w") 
    file.write(strikeString) 
    file.close()
