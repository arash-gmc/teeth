import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('predictors/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('predictors/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('predictors/haarcascade_mcs_mouth.xml')

img = cv2.imread('imgs/figo.jpg')
c=0;


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,3)


for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2);

    face_area_gray = gray[x:x+w,y:y+h]
    face_area = img[x:x+w,y:y+h]
    eyes = eyes_cascade.detectMultiScale(face_area_gray)
    mouths = mouth_cascade.detectMultiScale(face_area_gray,minSize=(100,20))
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    for (mx,my,mw,mh) in mouths:
        cv2.rectangle(face_area,(mx,my),(mx+mw,my+mh),(0,255,0),2)
    
    # (mx,my,mw,mh) = mouths[1]
    # cv2.rectangle(face_area,(mx,my),(mx+mw,my+mh),(0,255,0),2)
    # print(mouths)
        
cv2.imshow('face',img)
cv2.imwrite('cascade.jpg',img)
cv2.waitKey(0)

 

