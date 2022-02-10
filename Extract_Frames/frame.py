import cv2 
# Opens the Video file
file_name = input("Input Your Name: ")
path = "..//Data//Video//"+file_name+".avi"
cap= cv2.VideoCapture(path)
i=0
while(cap.isOpened()):
    # Get the Frame from the video
    ret, frame = cap.read()
    if ret == False:
        break
    # Write the frame in jpg at the desired folder with iterated frame number
    cv2.imwrite('..//Data//Frames//'+file_name+str(i)+'.jpg',frame)
    i+=1
 # Close the window / Release webcam
cap.release() 
# After we release our webcam, we also release the out-out.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()