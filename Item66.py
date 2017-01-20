'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student - original code partly inspired by post from stackoverflow user joaquin at
(http://stackoverflow.com/questions/9239514/filedialog-tkinter-and-opening-files)

Purpose: Learning to code in Python!  (Item 66 in Python Course)
This program helps users move files that are less than a day old.  This program creates a GUI allowing users to browse
and select source and destination folders.  It also allows them to manually execute the move operation.  The program
has some built-in checks to make sure the user gave a source and destination directory and that these were different
directories.

This program will also show the last date and time files were moved using this program.
It stores the datestamp in a database and reads that up initialization.
'''

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from math import floor
import shutil, os, sqlite3, time, datetime 

#GUI STRUCTURE------------------------------------------------------------------------------------------
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("File Mover")
        self.master.rowconfigure(3, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.grid(sticky=W+E+N+S)
        self.source = "source"
        self.destination = "destination"
        self.create_db()
        self.update()

        #BUTTONS----------------------------------------------------------------------------------------
        #Button for getting source folder
        self.src_button = Button(self, text="Select Source Folder", command=self.load_src_directory, width=25)
        self.src_button.grid(row=1, column=0, sticky=W)
        #Button for getting destination folder
        self.dest_button = Button(self, text="Select Destination Folder", command=self.load_dest_directory, width=25)
        self.dest_button.grid(row=2, column=0, sticky=W)
        #Button for executing file move
        self.move_button = Button(self, text="Check and Move Files", command=self.file_mover, width=25)
        self.move_button.grid(row=3, column=0, sticky=W)

        #LABELS----------------------------------------------------------------------------------------
        #Label (static text) to indicate datestamp follows:
        self.txt_lbl = Label(self, text="File mover last ran on: ")
        self.txt_lbl.grid(row=0, column=0, sticky=E, padx = 10, pady = 10)
        #Label to display source folder path
        self.src_lbl = Label(self, text="source")
        self.src_lbl.grid(row=1, column=1, sticky=W, padx = 10, pady = 10)
        #Label to display destination folder path
        self.dest_lbl = Label(self, text="destination")
        self.dest_lbl.grid(row=2, column=1, sticky=W, padx = 10, pady = 10)
        #Label to display status of move
        self.move_lbl = Label(self, text="status")
        self.move_lbl.grid(row=3, column=1, sticky=W, padx = 10, pady = 10)

#FUNCTIONS---------------------------------------------------------------------------------------------
    #Create the DB
    def create_db(self):
        conn=sqlite3.connect("file_mover.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS last_move (ID INTEGER PRIMARY KEY AUTOINCREMENT, datestamp TEXT)")
        conn.commit()

    #Command code for creating and updating GUI upon initialization to show when file_mover last ran:
    def update(self):
        #Label to contain datestamp as read from db:
        self.datestamp_lbl = Label(self, text="")
        self.datestamp_lbl.grid(row=0, column=1, sticky=W, padx = 10, pady = 10)

        #Get data from last_move table to populate the datestamp label:
        conn=sqlite3.connect("file_mover.db")
        c = conn.cursor()
        c.execute("SELECT datestamp FROM last_move ORDER BY datestamp DESC LIMIT 1")
        last_run = c.fetchone()
        if last_run == None:
            self.datestamp_lbl.config(text="No prior file moves performed.")
        else:
            self.datestamp_lbl.config(text=last_run[0])

    #Command code for source folder button (gets source directory)
    def load_src_directory(self):
        src_name = askdirectory()
        if src_name:
            self.src_lbl.config(text=src_name)
            self.source = src_name
        return(self.source)

    #Command code for destination folder button (gets destination directory)
    def load_dest_directory(self):
        dest_name = askdirectory()
        if dest_name:
            self.dest_lbl.config(text=dest_name)
            self.destination = dest_name
        return(self.destination)

    #Command code for the move files button - first tests source and destination and executes file move if appropriate
    def file_mover(self):
        if self.source == "source" and self.destination == "destination":
            messagebox.showwarning(title='Warning!',message='Please enter both source and destination folders.')
            self.move_lbl.config(text="Error!")
        elif self.source == "source" or self.destination == "destination":
            messagebox.showwarning(title='Warning!',message='Please enter both source and destination folders.')
            self.move_lbl.config(text="Error!")
        elif self.source == self.destination:
            messagebox.showwarning(title='Warning!', message='Source and destination are the same. Try again.')
            self.move_lbl.config(text="Error!")
        else:
            files = os.listdir(self.source) #makes a list of all files in the self.source directory
            contents = os.listdir(self.destination) #makes a list of all files in the self.destination directory
            
            for file in files:                              #this routine ensures that the file in source directory does not exist in the destination directory
                for i in range(len(contents)):              
                    if file == contents[i]:
                        files.remove(file)
                undup_files = files

            for file in undup_files:                        #this routine will move unduplicated files that are <24 hours old
                status = os.stat(self.source+'/'+file)      #gets status of file
                modified = status.st_mtime                  #isolating the time that file was last modified
                now = time.time()                           #current time
                recent = floor((now - modified)/3600)       #get age of file in hours
                if recent < 24:                             #check to see if file recently modified, within past 24 hours
                    shutil.move(self.source+'/'+file,self.destination)    #moves files

            self.move_lbl.config(text="Files moved from: " + self.source + " to: " + self.destination)  #reports file move
            time_of_move = time.time()
            datestamp_of_move = str(datetime.datetime.fromtimestamp(time_of_move).strftime('%Y-%m-%d %H:%M:%S'))
            self.log_last_move(datestamp_of_move)

    #Command code for updating the GUI to show the last date and time file_mover ran.  Also logs this time to the db.
    def log_last_move(self, datestamp_of_move):
        self.datestamp_lbl.config(text=datestamp_of_move) #update GUI
        #Routine for logging the datestamp to the database.
        conn=sqlite3.connect("file_mover.db")
        c = conn.cursor()
        c.execute("INSERT INTO last_move (datestamp) VALUES (?)",(datestamp_of_move,))
        conn.commit()
        c.close()
        conn.close()   

if __name__ == "__main__":
    MyFrame().mainloop()


