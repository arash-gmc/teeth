import cv2
import dlib

img = cv2.imread('imgs/figo.jpg')

hog_face_detector = dlib.get_frontal_face_detector()

dlib_face_landmark = dlib.shape_predictor("predictors/shape_predictor_68_face_landmarks.dat")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = hog_face_detector(gray)

for face in faces:
    face_landmarks = dlib_face_landmark(gray,face)

    for n in range (0,68):
        x=face_landmarks.part(n).x
        y=face_landmarks.part(n).y
        cv2.circle(img,(x,y),3,(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)