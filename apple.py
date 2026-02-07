import random

class Apple:
    def __init__(self, x, y):
        self.coord = (x, y)

    def randomize(self, maxX, maxY):
        self.coord = (random.randint(0, maxX), random.randint(0, maxY))