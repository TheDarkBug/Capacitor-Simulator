from ExtCable import *

class Capacitor():
	def __init__(self):
		self.rx, self.ry, self.rz = 70, 0, 30
		self.x, self.y = 250, 219
		self.charge = 400
		self.eCable = ExtCable()

	def show(self):
		pushMatrix()
		stroke(0)
		translate(self.x, self.y)
		rotateX(radians(self.rx))
		rotateY(radians(self.ry))
		rotateZ(radians(self.rz))
		# upper sheet
		fill(100, 120, 125)
		rect(0, 0, 200, 150)
		rect(200, 55, 40, 40)
		# lower sheet
		fill(100, 120, 125 + self.charge/6)
		translate(0, 0, - 20)
		rect(0, 0, 200, 150)
		rect(200, 55, 40, 40)
		# insulator
		fill(250, 200, 140)
		translate(0, 0, 10)
		rect(0, 0, 200, 150)
		popMatrix()
		self.cables()
	
	def cables(self):
		self.eCable.show(self.charge)
		self.eCable.collide() 