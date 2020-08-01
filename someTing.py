#These module comes default with python
import os
from tkinter import filedialog

#This module need to be install using pip install moviepy
from moviepy.editor import * 

while True:
	#giving option to user
    choice = input('Choice option\n1.Select File\n2.Close\nChoice: ')

    if choice == '1':
    	#Selecting file to be converted
        videoFile =  filedialog.askopenfilename(initialdir = "/",
        	title = "Select file",
        	filetypes = (("mp4s files","*.mp4"),("all files","*.*")))
        
        #Checking that the file was selected or not
        if videoFile == '':
            k = input('Please select video we cann\'t do any thing without a video\nHit enter to continue')
            #rerunning loop again 
            continue        

        	#Asking user options	
        methode = input('1.Save directly \n2.Do changes\nChoice: ')
        
        if methode == '2':
        	#select location and file name
            audioFile =  filedialog.asksaveasfilename(initialdir = fileActualLocation,
            	title = "Save as mp3",
            	filetypes = (("mp3 file","*.mp3"),("all files","*.*")))

            audioFile+='.mp3'
            
        else:
            #splitting up the location eg:-C:\Users\User\Desktop\Blog\videoConverter\converter.exe
            #to a list which looks like ['C:','User','User','Desktop','Blog','videoConverter','converter.exe']
            filePath = videoFile.split('/')
            fileName = filePath[-1] #Selecting last item from list

            fileActualLocation = filePath.pop(-1) #Removing file name

            fileActualLocation = ("/").join(filePath)#Joing list without file name
            #using default name and location

            fileName = fileName.split('.')

            #Getting file name without extension
            fileActualName = fileName[0] 
            #Default file name with .mp3 file formate
            audioFile = fileActualLocation+fileActualName+'.mp3'

        #Selecting video which was selected  
        videoClip = VideoFileClip(videoFile)
        audioClip = videoClip.audio #converting it into audio
        audioClip.write_audiofile(audioFile)#writing file in mp3 formate
        audioClip.close()
        videoClip.close()        

    elif choice == '2':
    	#if user select 2 quitting program
        quit()
        
    else:
    	#if user enter a invalidata
        print('Enter a validate option')
        k = input('Hit enter try again')
        continue
