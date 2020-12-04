class Capacitor():
	def __init__(self):
		self.rx, self.ry, self.rz = 70, 0, 30
		self.x, self.y = 250, 219
		self.charge = 0

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
		fill(100, 120, 125 + self.charge/5)
		translate(0, 0, - 20)
		rect(0, 0, 200, 150)
		rect(200, 55, 40, 40)
		# insulator
		fill(250, 200, 140)
		translate(0, 0, 10)
		rect(0, 0, 200, 150)
		popMatrix()

	def move(self):
		if keyPressed and key == 'x':
			self.rx += 1
		if keyPressed and key == 'y':
			self.ry += 1
		if keyPressed and key == 'z':
			self.rz += 1
		if keyPressed and key == 'X':
			self.rx -= 1
		if keyPressed and key == 'Y':
			self.ry -= 1
		if keyPressed and key == 'Z':
			self.rz -= 1
		if keyPressed and key == 'w':
			self.y -= 1
		if keyPressed and key == 'a':
			self.x -= 1
		if keyPressed and key == 's':
			self.y += 1
		if keyPressed and key == 'd':
			self.x += 1
		if keyPressed and key == 'r':
			self.rx, self.ry, self.rz = 70, 0, 30
			self.x, self.y = 250, 219
		# print(self.x,	self.y)
		# print(self.rx,	self.ry,	self.rz)
