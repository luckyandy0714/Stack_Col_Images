import cv2
import numpy as np
import os

output_path = "output_image.jpg"
output_height = 1024
output_width = 1920

images = sorted([img for img in os.listdir() if img.lower().endswith((".jpg", ".png"))])
dist = int(output_height / len(images))
output_height = dist * len(images)
result = np.zeros((output_height, output_width, 3), dtype=np.uint8)

for i, image in enumerate(images):
    img_path = os.path.join(os.getcwd(), image)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (output_width, dist))
    result[i * dist : i * dist + dist, :, :] = img
cv2.imwrite(output_path, result)
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", result)
cv2.resizeWindow("Result", 800, 600)
cv2.waitKey(0)
cv2.destroyAllWindows()
