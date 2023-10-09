import cv2
src = cv2.imread('./data/tomato.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.imshow('h', h)  # 색상
cv2.imshow('s', s)  # 채도
cv2.imshow('v', v)  # 명도
cv2.waitKey()
cv2.destroyAllWindows()
