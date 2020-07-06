## TODO: implement Exception handling
## TODO: Implement more Cascades  for different objects
## TODO: optimize code Etc
## TODO: implement a GUI
## TODO: implement custom android app for IP WEBCAM

## imports 
import cv2  # OpenCV lib
import logging as log
import datetime as dt

cascPath = 'FaceCascadeClassifier.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)
anterior = 0

url = '		' #url from the IP WEBCAM android application
video_capture = cv2.VideoCapture(url) # pass the url into the CV Capture into  cv2.VideoCapture(url) then give it a varible for later use 

while(True):
    ret, frame = video_capture.read() # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the frames to Gray 

    faces = faceCascade.detectMultiScale( # this is apart of the detection algorithm 
        gray,
        scaleFactor=1.1, #Parameter specifying how much the image size is reduced at each image scale.
        minNeighbors=35, #Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        minSize=(80,80) #Minimum possible object size. Objects smaller than that are ignored.
    )

    # Draw a rectangle around the faces at position  (x, y, w, h)
   
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (102,255,0), 2)
	#logging purposes 
    if anterior != len(faces):
        anterior = len(faces)
        log.info("Number of faces detected: "+str(len(faces))+" at this Date and time: "+str(dt.datetime.now()))

    # Display the resulting frame
    cv2.imshow('Video', frame)
    #exit the program by pressing q 
    q = cv2.waitKey(1)
    if q == ord("q"):
     print ('program has exited')
     break
cv2.destroyAllWindows()
video_capture.release()
