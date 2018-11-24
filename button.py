# File: button.py
# Name: Alex Laubscher
# Date: 10/04/16
# This is to create a button

from graphics import *


class Button:

    def __init__(self, win, center, width, height, label):
        self.xMin = center.getX() - width/2
        self.xMax = center.getX() + width/2
        self.yMin = center.getY() - height/2
        self.yMax = center.getY() + height/2
        pt1 = Point(self.xMin, self.yMin)
        pt2 = Point(self.xMax, self.yMax)
        self.outline = Rectangle(pt1, pt2)
        self.outline.setFill('lightgray')
        self.outline.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, pt):
        wasClicked = False
        if self.xMin <= pt.getX() and self.xMax >= pt.getX():
            if self.yMin <= pt.getY() and self.yMax >= pt.getY():
                if self.active == True:
                    wasClicked = True

        return wasClicked

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.outline.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgrey')
        self.outline.setWidth(1)
        self.active = False
        

