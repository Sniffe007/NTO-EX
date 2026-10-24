def centr_search(cnt):
moments = cv2.moments(cnt)
        try:
            x = int(moments['m10'] / moments['m00'])
            y = int(moments['m01'] / moments['m00'])
            return(x,y)
        except ZeroDivisionError:
            pass
 def process_frame(lower,upper,name):
     image = auv.get_image_bottom()
     image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
     mask = cv2.inRange(image,lower,upper)
     contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
     cv2.imshow('mask',mask)
     cv2.waitKey(1)
     for cnt in contours:
         area = cv2.contourArea(cnt)
         if area > 500:
             centr,radius = cv2