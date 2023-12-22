import cv2
import numpy as np

width = 1024
height = 720
pattern_num = 8

for i in range(0, pattern_num):
    num_stripes = 2 ** (i + 1)
    pattern = np.zeros((height, width), dtype=np.uint8)
    for j in range(num_stripes):
        start_col = int((j / num_stripes) * width)
        end_col = int(((j + 1) / num_stripes) * width)
        if (j + 2) % 2 != 0:
            pattern[:, start_col:end_col] = 255
    #pattern = cv2.rotate(pattern, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow(f"Binary_Code_{i}", pattern)   
    cv2.imwrite(f"Binary_Code_{i}.jpg", pattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
