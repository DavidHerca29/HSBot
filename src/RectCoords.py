

class RectCoords:
    x1 = int
    y1 = int
    x2 = int
    y2 = int

    def __init__(self):
        pass

    def getPosition(self):
        return self.x1, self.y1, self.x2, self.y2

    def getx1(self):
        return self.x1

    def getx2(self):
        return self.x2

    def gety1(self):
        return self.y1

    def gety2(self):
        return self.y2

    def setUpperLeft(self, px1, py1):
        self.x1, self.y1 = px1, py1
        return

    def setBottomRight(self, px2, py2):
        self.x2, self.y2 = px2, py2
        return

    def setRect(self, px1, py1, px2, py2):
        self.x1, self.y1 = px1, py1
        self.x2, self.y2 = px2, py2
        return