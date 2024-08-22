import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("ideal.jpg")
ideal_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image2 = cv2.imread("sample3.jpg")
sample_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

print(image.shape)
print(type(image))


ret,ideal_binary = cv2.threshold(ideal_gray, 127, 255, cv2.THRESH_BINARY)
ideal_not = cv2.bitwise_not(ideal_binary)
ret,sample_binary = cv2.threshold(sample_gray, 127, 255, cv2.THRESH_BINARY)
img_xor = cv2.bitwise_xor(ideal_not, sample_binary)

fig, axs = plt.subplots(1, 5, figsize=(20, 10))
axs[0].imshow(ideal_not,cmap='gray')
axs[1].imshow(sample_binary,cmap='gray')
axs[2].imshow(img_xor,cmap='gray')
#plt.title("my name is jeff")

img_xor =  cv2.medianBlur(img_xor, 5) # removing noise

black_image = np.zeros_like(ideal_binary)
cv2.circle(black_image, (300, 320), 200, 255, -1)
cv2.circle(black_image, (300, 320), 180, 0, -1)

tips = cv2.bitwise_or(img_xor, cv2.bitwise_not(black_image))

contours, hierarchy = cv2.findContours(cv2.bitwise_not(tips), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#print(str(len(contours)))
Number_of_tips = len(contours)
#____________________________________________________________________________________________________  
black_image2 = np.zeros_like(ideal_binary)
cv2.circle(black_image2, (300, 320), 165, 255, -1)
cv2.circle(black_image2, (300, 320), 150, 0, -1)
#axs[2].imshow(cv2.bitwise_or(img_xor,cv2.bitwise_not(black_image2)),cmap = 'gray')
#axs[3].imshow(cv2.bitwise_not(black_image2),cmap = 'gray')
bases = cv2.bitwise_or(img_xor, cv2.bitwise_not(black_image2))
#axs[4].imshow(bases, cmap = 'gray')
contours, hierarchy = cv2.findContours(cv2.bitwise_not(bases), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#print(str(len(contours)))
Number_of_bases = len(contours)
#_______________________________________________________________________
black_image = np.zeros_like(ideal_binary)
cv2.circle(black_image, (300, 320), 60, 255, -1)
axs[3].imshow(cv2.bitwise_not(black_image),cmap = 'gray')
center = cv2.bitwise_or(img_xor, cv2.bitwise_not(black_image))
axs[4].imshow(center, cmap = 'gray')
contours, hierarchy = cv2.findContours(cv2.bitwise_not(center), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

Problem_in_center = len(contours)
#_____________________________________________

if not(Number_of_bases) and not(Number_of_tips) and not(Problem_in_center):
   print("This gear is perfect")
else:
    if Number_of_bases:
        print("Number of missing teeth = " + str(Number_of_bases))
    if Number_of_tips:
        print("Number of worn-out teeth = " + str(Number_of_tips - Number_of_bases))
    if(Problem_in_center):
        print("there a problem with the opening")

#plt.show()