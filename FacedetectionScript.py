import cv2 
import numpy as np
import sys
import logging as log
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
anterior = 0

url = 'ENTER ADDRESS FROM IP CAM HERE'
cap = cv2.VideoCapture(url)
video_capture = cap

while(True):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
   ## conver to gray 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
    #dection size 
        minSize=(100,100) 
    )

    # Draw a rectangle around the faces
    ## faces that are found in the faceCascade
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (102,255,0), 2)
    #logging purposes 
    ## logs how many faces are detected 
    ## and at what date and time it was detected
    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)

    ## press Q on the keyboard to exit the application 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    # Display the resulting frame
    cv2.imshow('Video', frame)
## destroy and release 
cv2.destroyAllWindows()
video_capture.release()



