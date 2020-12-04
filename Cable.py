class Cable():
	def __init__(self):
		self.cableColor = False
		self.cabling = False
		self.cableP = False
		self.cableN = False

	def show(self):
		strokeWeight(4)
		noFill()
		if mousePressed:
			if mouseX > 715 and mouseY < 745 and mouseY > 185 and mouseY < 200:
				self.cableColor = True
				self.cabling = True
			elif mouseX > 720 and mouseX < 735 and mouseY > 430 and mouseY < 450:
				self.cableColor = False
				self.cabling = True
		if self.cableColor and self.cabling:
			stroke(255, 0, 0)
			curve(1200, 900, 730, 190, mouseX, mouseY, 300, 460)
			if mouseX > 360 and mouseX < 440 and mouseY > 260 and mouseY < 280:
				curve(1200, 900, 730, 190, 425, 270, 100, 100)
				self.cabling = False
				self.cableP = True
		elif self.cableColor == False and self.cabling:
			stroke(0)
			curve(1200, 0, 727, 440, mouseX, mouseY, 100, 100)
			if mouseX > 360 and mouseX < 440 and mouseY > 285 and mouseY < 310:
				curve(1200, 0, 727, 440, 420, 300, 100, 100)
				self.cabling = False
				self.cableN = True

		if self.cableP == True:
			stroke(255, 0, 0)
			curve(1200, 900, 730, 190, 425, 270, 100, 100)
		if self.cableN == True:
			stroke(0)
			curve(1200, 0, 727, 440, 420, 300, 100, 100)

		strokeWeight(1)
		stroke(0)
