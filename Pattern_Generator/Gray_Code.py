import cv2
import numpy as np

width = 1024
height = 720
pattern_num = 8

for i in range(0, pattern_num):
    num_stripes = 2 ** (i + 1)
    stripe_width = int(width / num_stripes)
    pattern = np.zeros((height, width), dtype=np.uint8)
    bit_negate = False
    for j in range(num_stripes):
        start_col = int(j * stripe_width)
        end_col = int(start_col + stripe_width)
        if not bit_negate:
            if (j + 2) % 2 != 0:
                pattern[:, start_col:end_col] = 255                
        else:
            if (j + 2) % 2 != 1:
                pattern[:, start_col:end_col] = 255
        if (j + 2) % 2 == 1:
            bit_negate = not bit_negate

    #cv2.imshow(f"Gray_Code_{i}", pattern)
    cv2.imwrite(f"Gray_Code_{i}.jpg", pattern)

cv2.waitKey(0)
cv2.destroyAllWindows()
