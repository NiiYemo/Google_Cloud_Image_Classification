# Google_Cloud_Image_Classification
Demonstrates the use of google cloud vision.
The idea for the an image scanner is to stop indecent images from being circulated on a website. It could be used at the uploading stage of the image, to then work with the back end, and maybe stop the image from being uploaded and ask for a more appropriate one. 

How it works:
Using google cloud vision. Which is a Machine Learning agent developed by google to classify images.  
'strike' variable is declared. Which will count strikes later. Setting up the ImageAnnotatorClient(). Which assigns labels to parts of the image recognised. The file path is set with the variable file_name, then it is read by the 'with' call, which is in conjunction  with the io.open command to open image as an image file. After reading as an image from the file location, google cloud vision has to know it is dealing with an image. Which is done in ‘image’.  'response' tells google cloud vision to assign labels to the image. 'labels' simply holds the labels assigned. 
The program then iterates through the labels in a for loop. If any of the labels match then ‘strike’ is incremented.  
Finally it write’s to a text file called ‘strikes.txt’ the number of strikes. 

‘Run_AI.py’ is a file that run theAI.py (Does the actual scanning of the image and counts the strikes) using a url
