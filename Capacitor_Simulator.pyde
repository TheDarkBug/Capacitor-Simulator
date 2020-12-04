from Battery import *; from Cable import *; from Capacitor import *
h, l = 800, 600
capacitor = Capacitor()
battery = Battery(l, h)


def setup():
	size(h, l, P3D)


def draw():
	background(150)
	battery.show()
	capacitor.show()
	capacitor.move()
	#print(mouseX, mouseY)
	if capacitor.charge < 400 and battery.cable.cableP and battery.cable.cableN:
		capacitor.charge += 1
		if capacitor.charge >= 400:
			battery.cable.cableP = False
			battery.cable.cableN = False
		print(battery.charge, capacitor.charge)
