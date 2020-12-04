class ExtCable():
	def __init__(self):
		self.px = 0
		self.py = 0
		self.nx = 0
		self.ny = 0
		self.P = False
		self.N = False
		self.cabling = False
		self.pos = True
		self.mouseHit = False

	def show(self, capacitorCharge):
		if capacitorCharge > 0:
			noFill()
			strokeWeight(4)
			if mouseX > 360 and mouseX < 440 and mouseY > 260 and mouseY < 280 and mousePressed:
				self.cabling = True
				self.pos = True
				self.mouseHit = True
			elif mouseX > 360 and mouseX < 440 and mouseY > 285 and mouseY < 310 and mousePressed:
				self.cabling = True
				self.pos = False
				self.mouseHit = True
			else:
				self.mouseHit = False
			if self.cabling:
				if self.pos:
					self.px = mouseX
					self.py = mouseY
					if mousePressed and not self.mouseHit:
						self.cabling = False
						self.P = True
					stroke(255, 0, 0)
					curve(1200, 900, self.px, self.py, 425, 270, 500, 100)
					stroke(0)
				if not self.pos:
					self.nx = mouseX
					self.ny = mouseY
					if mousePressed and not self.mouseHit:
						self.cabling = False
						self.N = True
					curve(1200, 0, self.nx, self.ny, 420, 300, 500, 100)
		if self.P:
			stroke(255, 0, 0)
			curve(1200, 900, self.px, self.py, 425, 270, 500, 100)
			stroke(0)
		if self.N:
			curve(1200, 0, self.nx, self.ny, 420, 300, 500, 100)
		strokeWeight(1)
	def collide(self):
		pass 
		#if self.N