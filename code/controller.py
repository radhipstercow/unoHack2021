# imports
import cv2
import face_recognition
import PySimpleGUI as sg
import time
import pyrebase
import os.path
# firebase authentication 
firebaseConfig = { "apiKey": "AIzaSyAyBVfmwl7Mzvr-cTxEErzFnFUvx4gAF5Y",
  "authDomain": "wellbeing-buddy.firebaseapp.com",
  "databaseURL": "https://wellbeing-buddy-default-rtdb.firebaseio.com",
  "projectId": "wellbeing-buddy",
  "storageBucket": "wellbeing-buddy.appspot.com",
  "messagingSenderId": "714633287482",
  "appId": "1:714633287482:web:ee3dd102975bec1da42203"}

firebase = pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

# pull user info 



#users
all_users = db.child("users").get()
for user in all_users.each():
    print(user.key()) 

mood = "none"

if mood == "none":
  layout = [  [sg.Text("JAMES", font='sansserif 24',)],
              [sg.Text('How are you feeling?', font='sansserif 15', size=(15, 1)), sg.InputText(key='-IN-')],
              [sg.Text('*Suggetion will appear after you enter your current mood', font='sansserif 13'),],
              [sg.Text('', font='sansserif 18'),],
              [sg.Text('To Do: ', font='sansserif 24'),],
              [sg.Text(' - Programming assignment 1', font='sansserif 18'),],
              [sg.Text(' - Case study paper', font='sansserif 18'),],
              [sg.Text('', font='sansserif 18'),],
              [sg.Text('Goals: ', font='sansserif 24'),],
              [sg.Text(' - Lose 5 pounds', font='sansserif 18'),],
              [sg.Text(' - Run a marathon', font='sansserif 18'),],
              [sg.Text('', font='sansserif 18'),],
              [sg.Submit(),sg.Cancel()]]


elif mood == "nervous":
  layout = [  [sg.Text("JAMES", font='sansserif 24',)],
              [sg.Text('Your mood is Nervous', font='sansserif 18'),],
              [sg.Text('I suggest taking a 5 minute mediation break.', font='sansserif 18'),],
              [sg.Cancel()]]
elif mood == "happy":
  layout = [  [sg.Text("JAMES", font='sansserif 24',)],
              [sg.Text('Your mood is Happy', font='sansserif 18'),],
              [sg.Text('I suggest going for a walk.', font='sansserif 18'),],
              [sg.Cancel()]]
# Create the Window
window = sg.Window('Health Buddy', layout, margins=(100, 30,))
# Event Loop to process "events"

#updatedMood = values['-IN-']
#sg.popup('You entered', updatedMood)
while True:             
  event, values = window.read()
  if event in (sg.WIN_CLOSED, 'Cancel'):
    break
  if event == 'Submit':
    updatedMood = values['-IN-']
    if updatedMood == 'sad':
      sg.popup('Since you are sad, I suggest listening to cheerful music. Music can drastically change your mood.')
    elif updatedMood == 'happy':
      sg.popup('I am glad you are happy. Eat an apple to work on your goal of loosing 5 pounds.')
    elif updatedMood == 'tired':
      sg.popup('Try going for a 15 minute walk or drink a glass of water. This will improve your energy levels. ')
    elif updatedMood == 'nervous':
      sg.popup('Try meditating for 5 minutes. Remember to just focus on your breathing, nothing else.')
    elif updatedMood == 'lonely':
      sg.popup('I suggest reaching out to a friend and ask about their day.')
    elif updatedMood == 'anxious about assignment 1':
      sg.popup('Try to break up the assignment into small sections. Do no be afraid to reach out to your professor. You can do it!')    







window.close()
# pull user goal list



# analyze current user mood (Facial Expression)


