from Cable import *

class Battery():
	def __init__(self, l, h):
		self.l = l
		self.h = h
		self.charge = 4000
		self.cable = Cable()

	def show(self):
		pushMatrix()
		translate(self.h - 130, self.l / 3, 0)
		fill(60, 200, 50)
		rect(0, 0, 120, 240, 20)
		rect(45, -15, 30, 10, 20, 20, 5, 5)
		popMatrix()
		if self.cable.cableP and self.cable.cableN:
			self.btoc()
		self.cable.show()

	def btoc(self):
			self.charge -= 1
			stroke(0, 0, 255)
			noFill()
			strokeWeight(6)
			curve(1200, 900, 730, 190, 425, 270, 100, 100)
			strokeWeight(1)
			stroke(0)
			if self.charge <= 0:
				self.charge = 0
				self.cable.cableP = False
				self.cable.cableN = False

