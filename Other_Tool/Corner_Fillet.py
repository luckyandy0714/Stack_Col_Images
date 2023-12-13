import cv2
import numpy as np

input_path = "Input.png"
output_path = "Output.png"
corner_radius = 100

image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

height, width, _ = image.shape


black_pixels = (image[:, :, :3] == [0, 0, 0]).all(axis=2)
image[black_pixels] = [0, 0, 0, 255]

mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (corner_radius, 0), (width - corner_radius, height), 255, thickness=cv2.FILLED)
cv2.rectangle(mask, (0, corner_radius), (width, height - corner_radius), 255, thickness=cv2.FILLED)
cv2.ellipse(mask, (corner_radius, corner_radius), (corner_radius, corner_radius), 180, 0, 90, 255, -1)
cv2.ellipse(mask, (corner_radius, image.shape[0] - corner_radius), (corner_radius, corner_radius), 90, 0, 90, 255, -1)
cv2.ellipse(mask, (image.shape[1] - corner_radius, corner_radius), (corner_radius, corner_radius), 270, 0, 90, 255, -1)
cv2.ellipse(mask, (image.shape[1] - corner_radius, image.shape[0] - corner_radius), (corner_radius, corner_radius), 0, 0, 90, 255, -1)
image[mask != 255] = [255, 255, 255, 0]

cv2.imwrite(output_path, image)
