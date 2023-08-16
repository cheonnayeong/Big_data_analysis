import cv2
image = cv2.imread('data/img.png')  # 사진 파일 로드
cv2.imshow('Image', image)  # 이미지 출력
key = cv2.waitKey(0)
if key == ord('s'):  # s 키를 누르면 이미지 저장
    cv2.imwrite('data/save_img.png', image)
    print('Image saved successfully!')
cv2.destroyAllWindows()
