import cv2


image = cv2.imread('image.jpg')


grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


inverted_img = cv2.bitwise_not(grey_img)


blur_img = cv2.GaussianBlur(inverted_img,(31,21),35)


inverted_blur_img = cv2.bitwise_not(blur_img)


sketch = cv2.divide(grey_img, inverted_blur_img, scale = 256.0)


cv2.imwrite('sketch.jpg',sketch)