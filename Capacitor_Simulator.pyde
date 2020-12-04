from Battery import *
from Cable import *
from Capacitor import *
h, l = 800, 600
battery = Battery(l, h)
capacitor = Capacitor()


def setup():
    size(h, l, P3D)


def draw():
    background(150)
    battery.show()
    capacitor.show()
    capacitor.move()
    print(mouseX, mouseY)
