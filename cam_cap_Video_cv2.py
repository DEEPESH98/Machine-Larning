import cv2

cap=cv2.VideoCapture(0)
# adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID') # ye avi or mp4 dono ko support ker ta he
# saving video          //uplod ker te time   width,hight
#output=cv2.VideoWriter('class.avi',plugin,20,(640,480))# is ka matlab he 25x20
#output=cv2.VideoWriter('class.avi',plugin,40,(640,480))
output=cv2.VideoWriter('class.avi',plugin,5,(640,480))
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    # drw pattern
    output.write(frame) # sending data to videowriter
    if cv2.waitKey(10) & 0xff == ord('q') : # q se window bande ho jae gi
        break

# distroy ker ne ke liye
cv2.destroyAllWindows()

cap.release()
