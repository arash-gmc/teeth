import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('predictors/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('predictors/haarcascade_eye.xml')

img = cv2.imread('imgs/figo.jpg')
c=0;


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2);

    face_area_gray = gray[x:x+w,y:y+h]
    face_area = img[x:x+w,y:y+h]
    eyes = eyes_cascade.detectMultiScale(face_area_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
        
cv2.imshow('face',img)
cv2.waitKey(0)

 

