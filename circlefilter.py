# new_file=('redcirclefileter.csv')

# f = open(new_file, "wt")
# writer=csv.writer(f)
# writer.writerow( ('circle_no','center_x','center_y','radious','point_r','point_r+1','point_r+2') )



# img = cv2.imread('sensor_video/frame/frame1505.jpg')
# hsvimage=cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
# red_hue_image=colordetection(hsvimage,0)
# circles_red=detectcircle(red_hue_image)
# if circles_red is not None:
#    no_red_c=0
#    for circles in circles_red[0]:
#       no_red_c +=1
#       [x_c,y_c,r]=circles
#       bottom=rectangle_per(hsvimage,x_c,y_c,r,0)
#       right=rectangle_per(hsvimage,x_c,y_c,r,1)
#       upper=rectangle_per(hsvimage,x_c,y_c,r,2)
#       left=rectangle_per(hsvimage,x_c,y_c,r,3)
#       print bottom,right,upper,left
#       if bottom > 70 or right > 70 or upper > 70 or left > 70:
#          cv2.circle(img, (x_c, y_c), r, (0, 0, 255), 3)
#          cv2.circle(img, (x_c, y_c), 1, (0, 255, 0), 1)

# green_hue_image=colordetection(hsvimage,1)
# circles_green=detectcircle(green_hue_image)

# if circles_green is not None:
#    for circles in circles_green[0]:
#       [x_c,y_c,r]=circles
#       bottom=rectangle_per(hsvimage,x_c,y_c,r,0)
#       right=rectangle_per(hsvimage,x_c,y_c,r,1)
#       upper=rectangle_per(hsvimage,x_c,y_c,r,2)
#       left=rectangle_per(hsvimage,x_c,y_c,r,3)
#       print bottom,right,upper,left
#       if bottom > 70 or right > 70 or upper > 70 or left > 70:
#          cv2.circle(img, (x_c, y_c), r, (0, 0, 255), 3)
#          cv2.circle(img, (x_c, y_c), 1, (0, 255, 0), 1)

# cv2.imshow("Detected red circles on the input image", img)
# cv2.waitKey(0)





# if circles_red is not None:
#             for circles in circles_red[0]:
#                 [x_c,y_c,r]=circles    
#                 point= midpointcircledraw(x_c,y_c,(r+1.2))
#                 count=0
#                 for i in range(0,len(point)):
#                     x,y = point[i]
#                     color=(hsvimage[int(y),int(x)])
#                     if color[2]<= blackrange:
#                         count+=1
#                 print(count/float(len(point)))*100,color[2]        
#                 if (count/float(len(point)))*100 <= percentile:
        
#                     cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#                     cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#                     cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  

# if circles_green is not None:
#             for circles in circles_green[0]:
#                 [x_c,y_c,r]=circles    
#                 point= midpointcircledraw(x_c,y_c,(r+1))
#                 print point
#                 count=0
#                 for i in range(0,len(point)):
#                     x,y = point[i]
#                     print x,y
#                     color=(hsvimage[int(y),int(x)])
#                     if color[2]<= blackrange:
#                         count+=1
#                 print(count/float(len(point)))*100,color
#                 if (count/float(len(point)))*100 >= percentile:
#                     cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#                     cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#                     cv2.putText(org_image,"green go",(int(x_c+10),int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)  

        # #for j in [1,1.5,2]:
#         point= midpointcircledraw(x_c,y_c,(r+1))
#         count=0
#         #color=[]
#         for i in range(0,len(point)):
#             x,y = point[i]
#             color=(hsvimage[int(y),int(x)])
#             #cv2.circle(img,(int(x),int(y)),0,(255,0,0),1)
#             writer.writerow( (no_red_c,x_c,y_c,r,color))        
#             # if color[2]<= blackrange:
#             #     count+=1
#             #     print(count/float(len(point)))*100,color[2]        
#             #     if (count/float(len(point)))*100 >= percentile:
        
#             #         cv2.circle(org_image, (x_c, y_c), r, (0, 0, 255), 2)
#             #         cv2.circle(org_image, (x_c, y_c), 1, (0, 255, 0), 1)
#             #         cv2.putText(org_image,"red don't go",(int(x_c+10), int(y_c+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)

  
# cv2.imshow('circles',img)
# cv2.waitKey(0)
# f.close()

# point= midpointcircledraw(825.5,325.5,5.5)
# for i in range(0,len(point)):
#    x,y = point[i]

#    #print x,y
#    color=(hsvimage[int(y),int(x)])

#    light=(hsl[int(y),int(x)])
#    print light
#    print color[2]
#    cv2.circle(img,(int(x),int(y)),1,(255,0,0),1)

  
# cv2.imshow('circles',img)
# cv2.waitKey(0)
