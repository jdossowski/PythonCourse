'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student

Purpose: Learning to code in Python!  (Item 64 in Python Course)
This program will move a file from one folder to another based on when they were
last modified.
'''

import shutil, os, time
from math import floor

source = 'C:\\Users\Student\Desktop\Folder_A\\' #additional \ needed to escape the \ for the file name string
destination = 'C:\\Users\Student\Desktop\Folder_B'

files = os.listdir(source)  #generates a list of file names

for file in files:
    status = os.stat(source+file)   #gets status of file
    modified = status.st_mtime      #isolating the time that file was last modified
    now = time.time()               #current time
    recent = floor((now - modified)/3600)  #get age of file in hours
    if recent < 24:                 #check to see if file recently modified, within past 24 hours
        shutil.move(source+file,destination)    #moves files
        print("File: {} is {} hours old and was moved".format(source+file,recent)) #prints file path and age
        #prints list of files moved as a check

