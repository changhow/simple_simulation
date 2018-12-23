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
env.add_flowers(10, 70, 1, 2, 'i')
env.add_flowers(10, 20, 2, 2, 'r')
env.add_flowers(30, 60, 3, 2, 'o')
env.update_plot()








