class Bees:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heading = 'N'
        self.tag = 'b'
        self.target_flower = None

    def forward(self):
        if self.heading == 'N':
            self.y += 1
        elif self.heading == 'S':
            self.y -= 1
        elif self.heading == 'E':
            self.x += 1
        elif self.heading == 'W':
            self.x -= 1
        elif self.heading == 'NE':
            self.x += 1
            self.y += 1
        elif self.heading == 'SE':
            self.x += 1
            self.y -= 1
        elif self.heading == 'NW':
            self.x -= 1
            self.y += 1
        else:
            self.x -= 1
            self.y -= 1

    def turn(self, heading):
        self.heading = heading

    def move(self, heading):
        self.turn(heading)
        self.forward()
