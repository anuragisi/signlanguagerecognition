##########################################################
###       Email id - anuragprasad@gmail.com            ###
###        Contact us if you need any help             ### 
###             Feel Free to ask anything              ###
##########################################################

import cv2
import numpy as np
import math
import os

kernel = np.ones((5,5),np.uint8)

def ready():
    t=0
    while t<30:
        t+=1
        ret, img = cap.read()
        img=cv2.flip(img,1)
        cv2.rectangle(img,( 300 , 300 ),( 100 , 100 ),( 0 , 255, 0 ), 0)
        crop_img = img[ 100 : 300 , 100 : 300 ]
        cv2.imshow('cam',img)
        cv2.imshow('crop',crop_img)
        cv2.waitKey(15)

def getImage(img):
    img1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)   #Morphological Gradient is one of filtering technique which provides better results.
    blurred = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    _, thresh1 = cv2.threshold(blurred, 70 , 255 , cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
    cv2.imshow('Threshold',thresh1)
    _, contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    max_area = - 1
    for i in range (len (contours)):
        cnt =contours[i]
        area = cv2.contourArea(cnt)
        if(area >max_area):
            max_area = area
            ci= i
    cnt =contours[ci]
    moments=cv2.moments(cnt)
    if moments['m00']!=0:
        cx=int(moments['m10']/moments['m00'])
        cy=int(moments['m01']/moments['m00'])
        centr=(cx,cy)
        cv2.circle(img1,centr,5,[255,0,255],2)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img1,(x,y),(x + w,y + h),( 0 , 0, 255 ), 0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(img1.shape,np.uint8)
    cv2.drawContours(drawing,[cnt], 0 ,( 0 , 255 , 0), 0 )
    cv2.drawContours(drawing,[hull], 0 ,( 0, 0 , 255 ), 0 )
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, - 1 , ( 0 , 255 ,0 ), 3)
    #print '\nno. of defects ',defects.shape[ 0]
    count_defects=0
    minl=(255,255)
    upper=0
    lower=0
    left=0
    right=0
    for i in range (defects.shape[ 0]):
        s,e,f,d = defects[i, 0 ]
        start = tuple (cnt[s][ 0 ])
        end = tuple (cnt[e][ 0 ])
        far = tuple (cnt[f][ 0 ])
        cv2.line(img1,start,end,[ 255, 0 , 255 ], 2 )
        cv2.line(img1,start,centr,[255,0,255],2)
        num1=centr[0]-far[0]
        num2=centr[1]-far[1]
        if far[1]<centr[1]:
            upper+=1
        else:
            lower+=1
        if far[0]<centr[0]:
            left+=1
        else:
            right+=1    
        count_defects+=1
    cv2.imshow('Contours', drawing)
    return count_defects,upper,lower,left,right,cnt
def isInRange(num,num2):
    if num>num2-1 and num<num2+1:
        return 1
    else:
        return 0
    
cap = cv2.VideoCapture( 1 )
word=''
stop=0
timer=0
move=0
cntname=[]
cntvalue=[]
upprv=[]
lowrv=[]
leftv=[]
rightv=[]
defectsv=[]
list1=os.listdir(os.getcwd()+'/sign')      # 'sign' is the folder name 
while move<len(list1):
    list2=os.listdir(os.getcwd()+'/sign/'+list1[move])  # 'sign' is the folder name
    moveunder=0                                         # directory listing are as sign/sign/a/jsf.jpeg etc 
    while moveunder<len(list2):                           
        img=cv2.imread('./sign/'+list1[move]+'/'+list2[moveunder])
        #img=cv2.imread('./sign/a/'+list2[moveunder])
        df,up,lw,lt,rt,ct= getImage(img)
        cntname.append(list1[move])
        cntvalue.append(ct)
        upprv.append(up)
        lowrv.append(lw)
        leftv.append(lt)
        rightv.append(rt)
        defectsv.append(df)        
        moveunder+=1
    move+=1
ready()
print 'start\n'
timer=0
while True:
    ret, img = cap.read()
    img=cv2.flip(img,1)
    cv2.rectangle(img,( 300 , 300 ),( 100 , 100 ),( 0 , 255, 0 ), 0)
    crop_img = img[ 100 : 300 , 100 : 300 ]
    df,up,lw,lt,rt,ct=getImage(crop_img)
    move=0
    while move<len(cntname):
        if isInRange(defectsv[move],df) and isInRange(rightv[move],rt) and isInRange(leftv[move],lt)  and isInRange(lowrv[move],lw) and isInRange(upprv[move],up):
            diffvalue=cv2.matchShapes(ct,cntvalue[move],1,0.0)
            if diffvalue<0.1:
               print '\nmatched with  ',cntname[move],'   diff : ',diffvalue
               cv2.putText(img,cntname[move],(100,400),cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2)
        move+=1
    cv2.imshow('cam',img)
    cv2.imshow('crop',crop_img)
    k=cv2.waitKey(15)
    if k == ord('q'):
      break
cv2.destroyAllWindows()


############### !!!!!! END !!!!!!!!! ##################