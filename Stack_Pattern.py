import cv2
import numpy as np
import os

width = 1920
height = 1024

input_patterns = sorted([img for img in os.listdir() if img.lower().endswith((".jpg", ".png"))])
dist = int(height / len(input_patterns))
height = dist * len(input_patterns)
pattern = np.zeros((height, width, 3), dtype=np.uint8)

for i, input_pattern in enumerate(input_patterns):
    img_path = os.path.join(os.getcwd(), input_pattern)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (width, dist))
    pattern[i * dist : i * dist + dist, :, :] = img

cv2.imwrite("Stack_Pattern.jpg", pattern)
cv2.namedWindow("Stack_Pattern", cv2.WINDOW_NORMAL)
cv2.imshow("Stack_Pattern", pattern)
cv2.resizeWindow("Stack_Pattern", 1280, 760)
cv2.waitKey(0)
cv2.destroyAllWindows()
