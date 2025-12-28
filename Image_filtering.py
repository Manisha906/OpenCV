import cv2
import numpy as np
img=cv2.imread("opencv/flower.webp")
blurred_img=cv2.GaussianBlur(img,(7,7),7)
medianblur_img=cv2.medianBlur(img,5)
sharpen_kernel=np.array([[0,-1,0],
                [-1,5,-1],
                [0,-1,0]])
sharpen_img=cv2.filter2D(blurred_img,-1,sharpen_kernel)
inp=input("enter which filter do you want Gaussianblur/medianblur/sharpening")
if inp=="gaussianblur":
    cv2.imshow("original image",img)
    cv2.imshow("blurred image",blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif inp=="medianblur":
    cv2.imshow("Medianblur image",medianblur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif inp=="sharpening":
    cv2.imshow("sharpen image",sharpen_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

