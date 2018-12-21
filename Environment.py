import numpy as np

from Flowers import Flowers
from BeeHives import BeeHives

class Environment:
    """ Environment is a window with width x height number of blocks """

    def __init__(self, width, height):
        # initialise the width and height of 2D environment
        self.width = width
        self.height = height
        self.cells = np.chararray(shape=(self.width, self.height), itemsize=10)
        self.cells[:] = ''
        self.beehives = []
        self.beehive_id = 0
        self.flowers = []

    def add_beehives(self, x, y, colony_size=50):
        beehive = BeeHives(x, y, self.beehive_id, colony_size)
        self.beehives.append(beehive)
        self.cells[x, y] += beehive.tag
        self.beehive_id += 1

    def add_flowers(self, x, y, ID, patch_radius=0, color='black'):
        flower = Flowers(x, y, ID, color)
        self.flowers.append(flower)

        for i in range(x - patch_radius, x + patch_radius + 1):
            for j in range (y - patch_radius, y + patch_radius + 1):
                if (i >= 0) and (j >= 0) and (i <= self.width) and (j <= self.height):
                    self.cells[i, j] = str(self.cells[i, j]) + flower.tag

