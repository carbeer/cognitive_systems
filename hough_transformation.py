#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x_vals = 5

def hough_transformation(pt, vals):
	return pt[0] * np.cos(x) + pt[1] * np.sin(x)


points = [(-1, 0), (0, -0.5), (1, -1)]
x = np.linspace(0, x_vals, x_vals*100)

f, ax = plt.subplots()
ax.set(xlabel='theta value')

for pt in points:
	ax.plot(x, hough_transformation(pt, x), label='Hough transformation of point ' + str(pt))
	ax.legend(loc='upper right')
    
plt.show()   