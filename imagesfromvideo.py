#!/usr/bin/env python3

import cv2
import numpy as np


# Включаем любую камеру
cap = cv2.VideoCapture(-1)
# значения минимума и максимума для маски
hsv_min = np.array((53, 55, 147), np.uint8)
hsv_max = np.array((83, 160, 255), np.uint8)
color_yellow = (0,255,255)
for i in range (30):
    cap.read() # читаем с камеры
while True:
    ret, frame = cap.read() # делаем снимок
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max) # маска для зеленого цвета

    # находим моменты изображения
    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    # центр пятна, которое больше 100 пикселей
    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(frame, (x, y), 5, color_yellow, 2)
        koor_str = cv2.putText(frame, "%d-%d" % (x,y), (x+10,y-10), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2) # строчка с координатами центра


    cv2.imshow('result', frame) 

    ch = cv2.waitKey(5)
    if ch == ord("q"):
        break
# Отключаем камеру
cap.release()
cv2.destroyAllWindows()

