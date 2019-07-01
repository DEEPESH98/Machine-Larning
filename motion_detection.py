import cv2

# start camera

cap = cv2.VideoCapture(0)

tap1=cap.read()[1] # take1
tap2=cap.read()[1] # take2
tap3=cap.read()[1] # take3

# to make molre perfect
gray1=cv2.cvtColor(tap1,cv2.COLOR_BGR2GRAY) # convert into gray
gray2=cv2.cvtColor(tap2,cv2.COLOR_BGR2GRAY) # convert into gray
gray3=cv2.cvtColor(tap3,cv2.COLOR_BGR2GRAY) # convert into gray


# now creating image diff
def img_diff(x,y,z):
    # diff b/w x,y--gray1,gray2 --d1
    d1=cv2.absdiff(x,y)
    # diff b/w y,z--gray2,gray3 --d2
    d2=cv2.absdiff(y,z)
    # absilute diff d1-d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg
    
# now apply funtion
while cap.isOpened():
    status,frame=cap.read() # continu me imsge lega
    motionimg=img_diff(gray1,gray2,gray3)
    # replacing image frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # passing live image to gray3
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)

    if cv2.waitKey(10) & 0xff == ord('q'):
            break

# distroy ker ne ke liye
cv2.destroyAllWindows()
cap.release()
