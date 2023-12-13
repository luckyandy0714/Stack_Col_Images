import cv2

threshold=150

image = cv2.imread('Input.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', binary_image)

cv2.imwrite("Output.jpg", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()