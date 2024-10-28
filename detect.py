import cv2
import mediapipe as mp

points = [78,95,88,178,87,14,317,402,318,324,308]
four_corners = [61,291,0,17]

def detect(path):
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    image = cv2.imread(path)
    height,width,_ = image.shape

    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_image)
    lip_points = []
    around = []
    for marks in result.multi_face_landmarks:
        for p in points:
            point = marks.landmark[p]
            x = int(point.x * width)
            y = int(point.y * height)
            lip_points.append([x,y,p])
        
        for p in four_corners:
            point = marks.landmark[p]
            x = int(point.x * width)
            y = int(point.y * height)
            around.append((x,y,p))

        upper_point =  marks.landmark[13]
        xu = int(upper_point.x * width)
        yu = int(upper_point.y * height)
        #cv2.circle(image,(xu,yu),5,(0,0,0),-1)

    buffer_x = int(width/20)
    buffer_y = int(height/30)

    
    x_min = around[0][0]-buffer_x
    x_max = around[1][0]+buffer_x
    y_min = around[2][1]-buffer_y
    y_max = around[3][1]+buffer_y
    
    
    croped_image = image[y_min:y_max,x_min:x_max]

    cvt_img = cv2.cvtColor(croped_image,cv2.COLOR_BGR2RGB)

    for p in lip_points:
        p[0]-= x_min
        p[1]-= y_min

    gray_croped = cv2.cvtColor(croped_image,cv2.COLOR_RGB2GRAY)

    # cv2.imshow('gray',cvt_img)
    # cv2.waitKey(0)

    return cvt_img,gray_croped,lip_points,(xu-x_min,yu-y_min)

   


    # for p in lip_points:
    #     cv2.circle(croped_image,(p[0],p[1]),3,(255,0,0),-1)

    # cv2.imshow('face',croped_image)
    # cv2.waitKey(0)

    



