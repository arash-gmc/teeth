import cv2
import mediapipe as mp

#Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('arash21.jpg')
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

(x1,x2,y1,y2) = (0,0,0,0)
for line in coords:
    for i in range(len(line)-1):
        cv2.line(image,(line[i][0],line[i][1]),(line[i+1][0],line[i+1][1]),(55,55,55),2)
        cv2.circle(image,(line[i][0],line[i][1]),1,(200,50,0),-1)
        
        if line[i][2]==78:
            x1 = line[i][0]
        if line[i][2]==308:
            x2 = line[i][0]
        if line[i][2]==14:
            y1 = line[i][1]
        if line[i][2]==13:
            y2 = line[i][1]

smile_index = (x2-x1)/(y2-y1)  
print("Smile index = ",smile_index)

cv2.imshow("Figo",image)
cv2.imwrite("result.jpg",image)
cv2.waitKey(0)