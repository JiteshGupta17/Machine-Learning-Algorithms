import cv2

cap = cv2.VideoCapture(0)

while True:

	ret,frame = cap.read()

	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret == False:
		contine

	cv2.imshow("VideoFrame",frame)
	cv2.imshow("GrayForm",gray_frame)

	key_pressed = cv2.waitKey(1) & 0xFF

	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()