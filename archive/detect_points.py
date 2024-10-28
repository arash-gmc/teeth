import cv2
import mediapipe as mp

#Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('figo.jpg')
height,width,_ = image.shape
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
result = face_mesh.process(rgb_image)

#l,r,u,b = (191,57,43,92)
l,r,u,b = (287,310,375,322)

detecting_points = [l,r,u,b]
detecing_coords = {}

for facial_landmarks in result.multi_face_landmarks:
    count = len(facial_landmarks.landmark)

    for c in detecting_points:
        pt1 = facial_landmarks.landmark[c]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        detecing_coords[c] = (x,y)

    for i in range(0,count):

        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)

        if x>detecing_coords[r][0] and x<detecing_coords[l][0] and y<detecing_coords[u][1] and y>detecing_coords[b][1] :

            cv2.circle(image,(x,y),2,(200,50,0),-1)
            cv2.putText(image,str(i),((x-100)*2,(y-300)*2),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
            print(i)
            
        
        # cv2.waitKey(30)

        


    # print(facial_landmarks)


# cv2.imshow("Figo",image)
cv2.imshow("Figo",image)
cv2.imwrite("result.jpg",image)
cv2.waitKey(0)