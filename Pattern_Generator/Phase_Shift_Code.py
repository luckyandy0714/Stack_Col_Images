import cv2
import numpy as np

width = 1024
height = 720
wave_unm = 8

pattern = np.zeros((height, width), dtype=np.uint8)
for i in range(width):
    pattern[:, i] = 255 * ((np.cos(np.radians((i / width) * (360 * wave_unm) + 180)) + 1) / 2)

#cv2.imshow("Phase_Shift_Code", pattern)
cv2.imwrite("Phase_Shift_Code.jpg", pattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
