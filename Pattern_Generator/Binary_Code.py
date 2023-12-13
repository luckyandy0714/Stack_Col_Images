import cv2
import numpy as np

width = 1024
height = 720
pattern_num = 8

for i in range(0, pattern_num):
    num_stripes = 2 ** (i + 1)
    stripe_width = int(width / num_stripes)
    pattern = np.zeros((height, width), dtype=np.uint8)
    for j in range(num_stripes):
        start_col = int(j * stripe_width)
        end_col = int(start_col + stripe_width)
        if (j + 2) % 2 != 0:
            pattern[:, start_col:end_col] = 255

    #cv2.imshow(f"Binary_Code_{i}", pattern)
    cv2.imwrite(f"Binary_Code_{i}.jpg", pattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
