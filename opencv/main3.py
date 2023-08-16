# 윈도우 전체화면
import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image.fill(200)  # 흰색 바탕
screen_width = 1920
screen_height = 1080
image = cv2.resize(image, (screen_width, screen_height))
cv2.namedWindow('Fullscreen Image', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(
    'Fullscreen Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow('Fullscreen Imgae', image)  # 행렬 원소를 영상으로 표시
cv2.waitKey(0)  # 키 이벤트 대
cv2.destroyWindow()  # 열린 모든 윈도우 제거
