import time
import os
from datetime import datetime 

#need to install using pip install win10toast
from win10toast import ToastNotifier

toaster = ToastNotifier()
logFileName = 'log.txt' #storing user entered data

#sending notification that program is started

toaster.show_toast("ExerciseKa", "This will take care of your health", threaded=True, icon_path=None, duration=6) #Notification duration will be 6 second
while toaster.notification_active(): #checking is there any other notification or not if yes waiting for 0.5 second 
    time.sleep(0.5)

#cheking does file is there or not 

def checkFile(fileName):
    try:
        logFile = open(fileName,'r') # If file doesn't then goes to exception
    except FileNotFoundError:
        logFile = open(fileName,'w') # Creates a logfile 
        data = ' '.join(['180','30','15'])
        logFile.write(data) #Write data
    finally:
        logFile.close() #Close file

def clear():
    os.system('cls||echo -e \\\\033c') # To clean terminal

def perfectTime():
    now = datetime.now() # using date time module
    hours = now.hour
    minute = now.minute
    perfectTime = int((hours*60)+minute)# converting hours to minutes then adding them
    return perfectTime #geting hours and minutes
    
clear() # A function define on line number 24
checkFile(logFileName)# Chacking files

#Giving options to users
        
file = open(logFileName,'r') # Opening file as read mode
data = file.read()#Reading data
file.close()#Closing file
        
clear()

data = data.split(' ')#Splitting up data

startingTime = perfectTime() #Getting the started time and function is define on line number 27

#calculating the time at which user should get notification	

waterReminderTime = startingTime+int(data[0]) 
exerciseReminderTime = startingTime+int(data[1])
eyeReminderTime = startingTime+int(data[2])
        
#This while loop will run till program is not closed and 1 stands for True

while 1:
    currentTime = perfectTime() # this will refresh after every loop cycle
    
    #checking does reminder time is equl to current time if yes then showing up the notification	
    
    if waterReminderTime == currentTime:
      waterReminderTime = waterReminderTime + int(data[0])
      toaster.show_toast("ExerciseKa","Time to drink water",threaded=True, icon_path=None, duration=6) #Notification duration will be 6 second
      while toaster.notification_active(): #checking is there any other notification or not if yes wating for 0.5 second 
          time.sleep(10)
    if exerciseReminderTime == currentTime:
        exerciseReminderTime = exerciseReminderTime + int(data[1])
        toaster.show_toast("ExerciseKa","Time to do exercise", threaded=True, icon_path=None, duration=6)
        while toaster.notification_active():
            time.sleep(10)

    if eyeReminderTime == currentTime:
        eyeReminderTime = eyeReminderTime + int(data[2])
        toaster.show_toast("ExerciseKa","Time to do eye exercise ",threaded=True, icon_path=None, duration=6)
        while toaster.notification_active():
            time.sleep(10)
            
    #waiting for 1 sec before running loop again you can use print here to checking loop is running or not
    
    time.sleep(1)
