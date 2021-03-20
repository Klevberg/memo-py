class Card:

    def __init__(self, sides):
        self.sides = sides
    
    def getSides(self):
        return self.sides

    def getSide(self, key):
        return self.sides[key]