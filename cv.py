import cv2
img=input("enter your image")
image=cv2.imread(img)
if image is not None:
    input1=input("what do you want draw from these pleasa enter line/circle/rectangle/text")
    if input1=="line":
        pt1=map(int,input())
        pt2=map(int,input())
        color=(255,0,0)
        thickness=3
        cv2.line(image,pt1,pt2,color,thickness)
        input=input("do you want save/show the imge" )
        if input=="save":
            inp=input("enter file name")
            output=cv2.imwrite(inp,image)
        else:
            cv2.imshow("drwaing line",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    elif input1=="rectangle":
        pt1=map(int,input())
        pt2=map(int,input())
        color=(255,0,0)
        thickness=4
        cv2.rectangle(image,pt1,pt2,color,thickness)
        input=input("do you want save/show the imge" )
        if input=="save":
            inp=input("enter file name")
            output=cv2.imwrite(inp,image)
        else:
            cv2.imshow("drawing a rectangle",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    elif input1=="circle":
        h,w=image.shape[:2]
        center=(h//2,w//2)
        radius=int(input())
        color=(255,0,0)
        thickness=-1
        cv2.circle(image,center,radius,color,thickness)
        input=input("do you want save/show the imge" )
        if input=="save":
            inp=input("enter file name")
            output=cv2.imwrite(inp,image)
        else:
            cv2.imshow("drawing a circle",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    else:
        cv2.putText(image,"Hello python lovers",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),2)
        input=input("do you want save/show the imge" )
        if input=="save":
            inp=input("enter file name")
            output=cv2.imwrite(inp,image)
        else:
            cv2.imshow("adding a text",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
else:
    print("image not loaded successfully")

