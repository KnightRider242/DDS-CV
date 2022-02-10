import cv2
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# input File name
file_name = input("Input Your Name: ")
path = "..//Data//Video//"+file_name+".avi"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(path, fourcc, 30.0, (640, 480),0)

# loop runs if capturing has been initialized.
while(True):
	# reads frames from a camera
	# ret checks return at each frame
	ret, frame = cap.read()

	# Converts to grayscale space, OCV reads colors as BGR
	# frame is converted to gray
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# output the frame
	out.write(gray)
	
	# The original input frame is shown in the window
	cv2.imshow('Original', frame)

	# The window showing the operated video stream
	cv2.imshow('frame', gray)
	
	# Wait for 'a' key to stop the program
	if cv2.waitKey(1) & 0xFF == ord('a'):
		break

# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the out-out.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()

