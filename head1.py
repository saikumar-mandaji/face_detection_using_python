import numpy as np
import cv2
face1 = cv2.CascadeClassifier('locate this file here-haarcascade_frontalface_default.xml')
eye1 = cv2.CascadeClassifier('locate this file here-haarcascade_eye.xml')
cap =cv2.VideoCapture(0)
font =cv2.FONT_HERSHEY_DUPLEX

while cap.isOpened():
    ret, fr=cap.read()
    faces = face1.detectMultiScale(fr, scaleFactor = 1.2,minNeighbors = 10)
    eye = eye1.detectMultiScale(fr,scaleFactor = 1.2,minNeighbors = 10)
    cap.get(0)
    if faces ==() and () == eye:
        cv2.putText(fr,'No face',(int(480/2),int(640/2)),font,2,(255,0,0),1,cv2.LINE_AA)

    for x,y,w,h in faces:
        fr=cv2.rectangle(fr,(x,y),(x+w,y+h),(0,255,0),5)
        cv2.putText(fr,'face',(x,y),font,1,(255,255,0),1,cv2.LINE_AA)
    for x,y,w,h in eye:
        
        fr=cv2.rectangle(fr,(x,y),(x+w,y+h),(0,255,0),5)
        cv2.putText(fr,'eye',(x,y),font,1,(255,255,0),1,cv2.LINE_AA)
    cv2.imshow('img',fr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(fr.shape)
cap.release()
