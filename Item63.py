'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student 

Purpose: Learning to code in Python!  (Item 63 in Python Course)
This program will move a file from one folder to another on my desktop.
'''

import shutil, os


source = 'C:\\Users\Student\Desktop\Folder_A\\' #additional \ needed to escape the \ needed for file name string
destination = 'C:\\Users\Student\Desktop\Folder_B'

files = os.listdir(source)
#print(source)

#shutil.move('C:\\Users\Student\Desktop\Folder_A\Random2.txt','C:\\Users\Student\Desktop\Folder_B')

for f in files:
    if f.endswith(".txt"):
        shutil.move(source+f ,destination)
        print("File that moved was: {}".format(source+f))
        


