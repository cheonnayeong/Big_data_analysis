# 직선사각형 선 그리기
import cv2
import numpy as np
# 흰색 배경 생성
# img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
img = np.full((512, 512, 3), (255, 0, 0), dtype=np.uint8)  # 색깔지정

pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

cv2.line(img, (0, 0), (512, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
