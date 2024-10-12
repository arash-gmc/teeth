import cv2
import mediapipe as mp

#Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('arash.jpg')
height,width,_ = image.shape
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
result = face_mesh.process(rgb_image)

for facial_landmarks in result.multi_face_landmarks:
    count = len(facial_landmarks.landmark)
    for i in range(0,count):

        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
   
        cv2.circle(image,(x,y),2,(200,50,int(i*250/count)),-1)
        cv2.imshow("Figo",image)
        # cv2.waitKey(30)


    # print(facial_landmarks)


# cv2.imshow("Figo",image)
cv2.waitKey(0)