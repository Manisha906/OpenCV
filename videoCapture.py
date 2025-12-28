import cv2
cap=cv2.VideoCapture(0)
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(* 'XVID')
out=cv2.VideoWriter('output.avi',codec,20.0,(frame_width,frame_height))
while True:
    ret,frame=cap.read()
    if not ret:
        print("could not read frame")
        break
    out.write(frame)
    cv2.imshow("web captured",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("quitting")
        break
cap.release()
out.release()
cv2.destroyAllWindows()

