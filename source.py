import numpy as np
from matplotlib import pyplot as plt

positions = []
velocities = []
#  Initial values:
positions.append(10.0)
velocities.append(2.1)
h = 0.001
n = 10000


def force(x, a=1.5, V=1, m=1):
    return -2*(a**2)*V*x/(m*(a**2 + x**2)**2)


def Euler(x0, v0, h):
    nextv = v0 + h*force(x0)
    nextx = x0 + h*nextv
    return (nextx, nextv)


def Eulerloop(h, n, x0=positions[0], v0=velocities[0]):
    for i in range(n):
        position, velocity = Euler(x0, v0, h)
        positions.append(position)
        velocities.append(velocity)


def Verlet(x0, v0, h):
    intermediatev = v0 + h*force(x0)/2
    nextx = x0 + h*intermediatev
    nextv = intermediatev + h*force(nextx)/2
    return (nextx, nextv)


def Verletloop(h, n, x0=positions[0], v0=velocities[0]):
    for i in range(n):
        position, velocity = Verlet(x0, v0, h)
        positions.append(position)
        velocities.append(velocity)


Verletloop(h, n)
plt.plot([h*i for i in range(n+1)], positions)
