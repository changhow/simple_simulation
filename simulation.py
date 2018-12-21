"""
Simulation of Bees choosing from 2 directions based on scent/color

What is required:
Environment
    X,Y Plane
BeeHives
    Bees
        X, Y Plane
Flowers
    Scent
    Color
    X, Y Plane
"""
from Environment import Environment

env = Environment(800, 800)
env.add_beehives(1, 1, 1)
env.add_flowers(1, 2, 1, 1)

print(env.beehives[0].tag, env.flowers[0].tag)
print(env.cells[1, 1])





