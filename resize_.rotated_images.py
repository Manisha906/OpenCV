import cv2
import numpy as np
img=cv2.imread("opencv/python.jpg")
if img is not None:
    h,w,c=img.shape
    print(f"image loaded:\nheight {h}\nwidth {w}\nchannel {c}")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    resize=cv2.resize(img,(300,300))
    center=(h//2,w//2)
    m=cv2.getRotationMatrix2D(center,90,1.0)
    rotated=cv2.warpAffine(img,m,(w,h))
    n=input("Enter what you want to show(Gray image/Resize image/Rotated image\flip image)")
    if n=="gray":
        cv2.imshow("gray image",gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif n=="resize":
        cv2.imshow("resized image",resize)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif n=="Rotated":
        cv2.imshow("Rotated image",rotated)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        flipped_imgh=cv2.flip(img,1)
        flipped_imgv=cv2.flip(img,0)
        flipped_imghv=cv2.flip(img,-1)
        combined=np.hstack((flipped_imgh,flipped_imgv,flipped_imghv))
        # cv2.imshow("real image",img)
        # cv2.imshow("flipping image horizontally",flipped_imgh)
        # cv2.imshow("flipping imgage vertically",flipped_imgv)
        # cv2.imshow("flipping image vertically and horizontally",flipped_imghv)
        cv2.imshow("flipping images",combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("image is not loaded")
