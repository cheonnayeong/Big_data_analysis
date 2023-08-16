import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(200)  # 흰색 바탕
title1, title2 = 'AUOTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)
cv2.imshow(title1, image)  # 행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)  # 키 이벤트 대
cv2.destroyWindow()  # 열린 모든 윈도우 제거
