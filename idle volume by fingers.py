import cv2 as cv
import mediapipe as mp
import numpy as np
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

capture=cv.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
while True:
    success,img=capture.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result=hands.process(imgRGB)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                #print(id,lm)
                height,width,column=img.shape
                cx , cy=int(lm.x*width) , int(lm.y*height)
                #print(id,cx,cy)
                if id==4:
                    l1=[id,cx,cy]
                if id==8:
                    l2=[id,cx,cy]
                #print([l1,l2])               
            mpdraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)

            x1,y1=l1[1],l1[2]
            x2,y2=l2[1],l2[2]
            cv.circle(img,(x1,y1),10,(123,0,10),cv.FILLED)
            cv.circle(img,(x2,y2),10,(123,0,10),cv.FILLED)

            length=math.hypot(x2-x1 , y2-y1)
            print(length)

        volrange=volume.GetVolumeRange()
        minvol=volrange[0]
        maxvol=volrange[1]
        vol=np.interp(length,[50,260],[minvol,maxvol])

        volbar=np.interp(length,[50,260] , [500,50])

        volume.SetMasterVolumeLevel(vol,None)
        cv.rectangle(img,(50,50),(90,500),(234,12,3),5)
        cv.rectangle(img,(50,int(volbar)),(90,500),(123,12,3),cv.FILLED)
    cv.imshow("Image",img)
    cv.waitKey(1)
    
