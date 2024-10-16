import cv2
import mediapipe as mp

#Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('imgs/figo.jpg')
height,width,_ = image.shape
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
result = face_mesh.process(rgb_image)

lines = [
        [61,185,40,39,37,0,267,269,270,409,291],
        [78,191,80,81,82,13,312,311,310,415,308],
        [78,88,178,87,14,317,402,318,324,308],
        [61,146,91,181,84,17,314,405,321,375,291]
         ]
coords = []

for facial_landmarks in result.multi_face_landmarks:
    for line in lines:
        coords.append([])
        for num in line:
            point = facial_landmarks.landmark[num]
            x= int(point.x * width)
            y = int(point.y * height)
            coords[-1].append((x,y,num))

(x1,y1,x2,y2,x3,y3,x4,y4) = (0,0,0,0,0,0,0,0)
for line in coords:
    for i in range(len(line)):
        if (i<len(line)-1):
            cv2.line(image,(line[i][0],line[i][1]),(line[i+1][0],line[i+1][1]),(55,55,55),2)
        cv2.circle(image,(line[i][0],line[i][1]),1,(200,50,0),-1)
        if line[i][2]==78:
            x1 = line[i][0]
            y1 = line[i][1]
        if line[i][2]==308:
            x2 = line[i][0]
            y2 = line[i][1]
        if line[i][2]==14:
            x3 = line[i][0]
            y3 = line[i][1]
        if line[i][2]==13:
            x4 = line[i][0]
            y4 = line[i][1]

smile_index = (x2-x1)/(y3-y4)  
print("Smile index = ",smile_index)

cv2.line(image,(x1,y1),(x2,y2),(255,0,255),1)
cv2.line(image,(x3,y3),(x4,y4),(255,0,255),1)

cv2.circle(image,(x1,y1),3,(255,255,255),-1)

cv2.imshow("Figo",image[y1:])
cv2.imwrite("result.jpg",image)
cv2.waitKey(0)