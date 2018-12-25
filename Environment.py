import numpy as np
import random
import matplotlib.pyplot as plt
from Flowers import Flowers
from BeeHives import BeeHives
from MyColorMap import myColorMap as rgb_color

class Environment:
    """ Environment is a window with width x height number of blocks """

    def __init__(self, width, height):
        # initialise the width and height of 2D environment
        self.width = width
        self.height = height
        self.cells = np.chararray((self.width, self.height), unicode=True)
        # self.cells = np.zeros((self.width, self.height), dtype=np.int32)
        self.beehives = []
        self.beehive_id = 0
        self.flowers = []
        self.fig = plt.gcf()
        self.fig.show()
        self.fig.canvas.draw()

        x = np.arange(self.width)
        y = np.arange(self.height)
        x, y = np.meshgrid(x, y)
        plt.scatter(x, y, c=rgb_color['green'])

    def add_beehives(self, x, y, colony_size=50):
        beehive = BeeHives(x, y, colony_size)
        self.beehives.append(beehive)
        self.cells[x, y] = beehive.tag
        plt.scatter(x, y, c=rgb_color['black'])

    def add_flowers(self, x, y, patch_radius=0, color='yellow'):
        flower = Flowers(x, y, color)
        self.flowers.append(flower)

        for i in range(x - patch_radius, x + patch_radius + 1):
            for j in range(y - patch_radius, y + patch_radius + 1):
                if (i >= 0) and (j >= 0) and (i <= self.width) and (j <= self.height):
                    plt.scatter(i, j, c=flower.color)
                    self.cells[i, j] = flower.tag

    def start(self):

        print(self.beehives[0].bees[0].heading)

    @staticmethod
    def compute_direction(flower_pos, bee_pos):
        heading_vertical = ''
        heading_horizontal = ''

        if flower_pos[0] - bee_pos[0] > 0:
            heading_horizontal = 'E'
        elif flower_pos[0] - bee_pos[0] < 0:
            heading_horizontal = 'W'

        if flower_pos[1] - bee_pos[1] > 0:
            heading_vertical = 'N'
        elif flower_pos[1] - bee_pos[1] < 0:
            heading_vertical = 'S'

        heading = heading_vertical + heading_horizontal
        return heading

    def bees_on_the_move(self):
        # print(len(self.flowers))
        # print(random.choice(self.flowers).color)
        # print(len(self.beehives[0].bees))
        bees = self.beehives[0].bees
        target_flower = random.choice(self.flowers)
        heading = self.compute_direction(target_flower.pos, self.beehives[0].pos)
        # print(heading)
        for bee in bees:
            bee.target_flower = random.choice(self.flowers)
            print(bee.target_flower.pos)

        while self.cells[bees[0].x, bees[0].y] != target_flower.tag:
            for bee in bees:
                bee.move(self.compute_direction(bee.target_flower.pos, (bee.x, bee.y)))
                # print(self.cells[bees[0].x, bees[0].y], target_flower.tag, bees[0].x, bees[0].y)
                # heading = self.compute_direction(target_flower.pos, (bees[0].x, bees[0].y))
                # bees[0].move(heading)
                plt.scatter(bee.x, bee.y, c=rgb_color[random.choice(['white'])])
                plt.pause(0.0001)

        # for i in range(len(bees)):
        #     print(i, bees[i].x, bees[i].y)



    #
    # def update_plot(self):
    #     plt.scatter(70, 70, c='#FF0000')
    #     plt.pause(20)

