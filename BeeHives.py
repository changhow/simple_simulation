from Bees import Bees

class BeeHives:
    def __init__(self, x, y, colony_size):
        self.tag = [255, 0, 0]
        self.colony_size = colony_size
        self.pos = (x, y)
        self.tag = 'B'
        self.bees = []

        for _ in range(colony_size):
            self.bees.append(Bees(self.pos[0], self.pos[1]))
