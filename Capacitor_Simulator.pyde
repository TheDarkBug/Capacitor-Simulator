from Battery import *
from Cable import *
from Capacitor import *
h, l = 800, 600
battery = Battery(l, h)
capacitor = Capacitor()

def setup():
    size(h, l, P3D)

def draw():
    global rx, ry, rz, x, y, cableColor, cabling, cable_1, cable_2
    background(150)
    battery.show()
    capacitor.show()
    #print(mouseX, mouseY)

def move():
    global x,	y, rx, ry, rz
    if keyPressed and key == 'x':
        rx += 1
    if keyPressed and key == 'y':
        ry += 1
    if keyPressed and key == 'z':
        rz += 1
    if keyPressed and key == 'X':
        rx -= 1
    if keyPressed and key == 'Y':
        ry -= 1
    if keyPressed and key == 'Z':
        rz -= 1
    if keyPressed and key == 'w':
        y -= 1
    if keyPressed and key == 'a':
        x -= 1
    if keyPressed and key == 's':
        y += 1
    if keyPressed and key == 'd':
        x += 1
    if keyPressed and key == 'r':
        rx,	ry,	rz = 80, 40, 0
        x, y = 315, 262
    # print(x,	y)
    # print(rx,	ry,	rz)
