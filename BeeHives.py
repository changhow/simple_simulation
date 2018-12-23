class BeeHives:
    def __init__(self, x, y, ID, colony_size):
        self.tag = [255, 0, 0]
        self.colony_size = colony_size
        self.id = ID
        self.pos = (x, y)
