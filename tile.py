# 2048 tile class

from graphics import *

class Tile:

    def __init__(self, win, center, fill, label, row, column):
        self.fill = fill
        self.label = label
        self.center = center
        self.row = row
        self.column = column
        width = 125
        height = 125
        self.xMin = center.getX() - width/2
        self.xMax = center.getX() + width/2
        self.yMin = center.getY() - height/2
        self.yMax = center.getY() + height/2
        pt1 = Point(self.xMin, self.yMin)
        pt2 = Point(self.xMax, self.yMax)
        self.outline = Rectangle(pt1, pt2)
        self.outline.setFill(self.fill)
        self.outline.draw(win)
        self.empty = True

    def getEmpty(self):
        return self.empty

    def getLabel(self):
        return self.label

    def changeLabel(self, new_value):
        self.label = new_value

    def doubleLabel(self):
        self.label = self.label * 2

    def changeText(self, win):
        try:
            self.text.undraw()
        except AttributeError:
            blank = 0            
        if self.label == 0:
            value = " "
        else:
            value = self.label
        self.text = Text(self.center, value)
        self.text.setSize(20)
        self.text.setStyle("bold")
        self.text.draw(win)

    def fillSquare(self):
        self.empty = False

    def emptySquare(self):
        self.empty = True

    def updateFill(self):
        if self.label == 0:
            self.fill = "white"
        elif self.label == 2:
            self.fill = "lightgray"
        elif self.label == 4:
            self.fill = "beige"
        elif self.label == 8:
            self.fill = "orange"
        elif self.label == 16:
            self.fill = "red"
        elif self.label == 32:
            self.fill = "yellow"
        elif self.label == 64:
            self.fill = "green"
        elif self.label == 128 or self.label == 256 or self.label == 512:
            self.fill = "blue"
        elif self.label == 1024 or self.label == 2048:
            self.fill = "purple"
        elif self.label > 2048:
            self.fill = "pink"
        self.outline.setFill(self.fill)
