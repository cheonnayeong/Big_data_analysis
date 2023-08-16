import cv2
# BGR 색공간을 RGB로 변경
image = cv2.imread('data/img.png')  # 사진 파일 로드
img_rgb = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2RGB)
cv2.imshow('RGB', image_rgb)
cv2.waitKey(0)
# 흑백 이미지 설정
img_rgb = cv2.cvtColor(image, cv2.COLOR_BAYER_BGRA2GRAY)
cv2.imshow('RGB', gray_rgb)
cv2.waitKey(0)
# 특정 시간동안 이미지 보여주기
cv2.imshow('Timed Display', image)
cv2.waitKey(3000)
cv2.destroyAllWindows()
