import cv2 
import numpy as np

#이미지 불러오기
image = cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 도형, 글자 생성
cv2.circle(image_big, (360, 150), 50, (0,0,255), 5)
cv2.circle(image_big, (270, 150), 50, (0,0,255), 5)
cv2.putText(image_big, "Lenna", (100,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,250))
pts = np.array([[150,300], [50,450], [250,450]], dtype=np.int32)
cv2.polylines(image_big, [pts], True, (0,0,255), 10)


cv2.imshow('Image Window', image_big)

cv2.waitKey(0)
cv2.destroyAllWindows() 