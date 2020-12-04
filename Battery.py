from Cable import *


class Battery():
    def __init__(self, l, h):
        self.l = l
        self.h = h
        self.cable = Cable()

    def show(self):
        pushMatrix()
        translate(self.h - 130, self.l / 3, 0)
        fill(60, 200, 50)
        rect(0, 0, 120, 240, 20)
        rect(45, -15, 30, 10, 20, 20, 5, 5)
        popMatrix()
        self.cable.show()
