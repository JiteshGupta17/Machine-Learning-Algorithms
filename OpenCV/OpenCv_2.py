import cv2

img = cv2.imread('./KnnDataset/ambulance.jpg')

gryImg = cv2.imread('./KnnDataset/ambulance.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow("Ambulance",img)
cv2.imshow("Gray one",gryImg)

cv2.waitKey(0)
cv2.destroyAllWindows()