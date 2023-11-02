import cv2

src = cv2.imread('./data/img.png', cv2.IMREAD_COLOR)
dst = src[100:600, 200:700].copy()
# Opencv 이미지는 numpy 베열 형식과 동일
# src 이미지에 높이 너비로 관심영역을 설정 합니다
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
