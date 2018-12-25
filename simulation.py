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

env = Environment(100, 100)
env.add_flowers(80, 80, 2, 'i')
env.add_flowers(0, 0, 2, 'r')
env.add_flowers(0, 80, 2, 'o')
env.add_beehives(50, 50, 10)
env.bees_on_the_move()
# env.update_plot()

print(env.cells)








