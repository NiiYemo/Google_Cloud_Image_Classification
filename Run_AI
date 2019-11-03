# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 02:16:23 2019

@author: yemoQ
"""
import os 

host_location="http://localhost:9000/assets/images/"
#host_location=" https://i.ebayimg.com/images/g/4T4AAOSwyKxXhe3q/s-l300.jpg"
py = "python theAi.py"
f=open("strikes.txt", "r")

if f.mode == 'r':
  	contents =f.read()

file_path = host_location + contents
the_command = py + file_path
print(the_command)
os.system(the_command)
os.system("exit")
