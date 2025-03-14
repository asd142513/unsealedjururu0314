import cv2

image1 = cv2.imread("qr.png")
image2 = cv2.imread("noqr.png")

result = cv2.subtract(image1, image2)
result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY)

cv2.imwrite("result.png", result)
