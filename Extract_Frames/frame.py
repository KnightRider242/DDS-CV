import cv2 
# Opens the Video file
file_name = input("Input Your Name: ")
path = "..//Data//Video//"+file_name+".avi"
cap= cv2.VideoCapture(path)
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('..//Data//Frames//'+file_name+str(i)+'.jpg',frame)
    i+=1
 
cap.release() 
cv2.destroyAllWindows()