import cv2
import numpy as np

width = 1024
height = 720
pattern_num = 8

for i in range(0, pattern_num):
    pattern = np.zeros((height, width), dtype=np.uint8)

    num_stripes = 2 ** (i + 1)
    bit_negate = False
    for j in range(num_stripes):
        start_col = int((j / num_stripes) * width)
        end_col = int(((j + 1) / num_stripes) * width)
        if not bit_negate:
            if j % 2 != 0:
                pattern[:, start_col:end_col] = 255
        else:
            if j % 2 != 1:
                pattern[:, start_col:end_col] = 255
        if j % 2 == 1:
            bit_negate = not bit_negate
    #pattern = cv2.rotate(pattern, cv2.ROTATE_90_CLOCKWISE)
    #cv2.imshow(f"Gray_Code_{i}", pattern)
    cv2.imwrite(f"Gray_Code_{i}.jpg", pattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
