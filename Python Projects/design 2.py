from turtle import *
from colorsys import *
bgcolor('black')
speed(0) 
h=0
goto (150,50)
for i in range(12):
    color(hsv_to_rgb(h,1,1)) 
    for j in range (75):
        h+= 0.005
        fd(100)
        bk(100)
        rt(2)
    fd(250)
done()