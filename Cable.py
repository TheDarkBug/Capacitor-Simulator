class Cable():
    def __init__(self):
        self.cableColor = False
        self.cabling = False
        self.cableP = "no"
        self.cableN = "no"

    def show(self):
        strokeWeight(4)
        noFill()
        if mousePressed:
            if mouseX > 715 and mouseY < 745 and mouseY > 185 and mouseY < 200:
                self.cableColor = True
                self.cabling = True
            elif mouseX > 700 and mouseX < 755 and mouseY > 430 and mouseY < 450:
                self.cableColor = False
                self.cabling = True
        if self.cableColor and self.cabling:
            print("mouse")
            stroke(255, 0, 0)
            curve(1200, 900, 730, 190, mouseX, mouseY, 300, 460)
            if mouseX > 305 and mouseX < 395 and mouseY > 315 and mouseY < 335:
                curve(1200, 900, 730, 190, 350, 325, 300, 460)
                self.cabling = False
                self.cableP = "up"
            if mouseX > 305 and mouseX < 395 and mouseY > 340 and mouseY < 370:
                curve(1200, 900, 730, 190, 350, 355, 300, 460)
                self.cabling = False
                self.cableP = "down"
        elif self.cableColor == False and self.cabling:
            stroke(0)
            curve(1200, 0, 727, 440, mouseX, mouseY, 300, 460)
            if mouseX > 305 and mouseX < 395 and mouseY > 315 and mouseY < 335:
                curve(1200, 0, 727, 440, 350, 325, 300, 460)
                self.cabling = False
                self.cableN = "up"
            elif mouseX > 305 and mouseX < 395 and mouseY > 350 and mouseY < 370:
                curve(1200, 0, 727, 440, 350, 355, 300, 460)
                self.cabling = False
                self.cableN = "down"

        if self.cableP == "up":
            stroke(255, 0, 0)
            curve(1200, 900, 730, 190, 350, 325, 300, 460)
        if self.cableP == "down":
            stroke(255, 0, 0)
            curve(1200, 900, 730, 190, 350, 355, 300, 460)
        if self.cableN == "up":
            stroke(0)
            curve(1200, 0, 727, 440, 350, 325, 300, 460)
        if self.cableN == "down":
            stroke(0)
            curve(1200, 0, 727, 440, 350, 355, 300, 460)

        strokeWeight(1)
        stroke(0)
