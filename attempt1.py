



import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
import matplotlib 
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import pandas as pd
import glob

p = fetch_stored_data(2, None, True)



num_lines = 39
num_points = 2200
x = np.linspace(-.5, 10.5, 2200)
y = p
X, Y = np.meshgrid(x, y)
Z = np.zeros((num_lines, num_points))


    
    #Start of function
def waterfall(p):
    x_data = np.linspace(-.5, 10.5, 2200)
    blm_iterator_list = np.linspace(1,38,39, dtype=int)
    #Graph colours
    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, yticks):
        print (c,k)
        
    blm_iterator_list = np.linspace(1,38,39, dtype=int)

    fig = plt.figure(figsize=(10,11), tight_layout = True)
    ax = fig.add_subplot(111, projection='3d')

    for i in blm_iterator_list:
    
    # fetch_stored_data(n, None, False) = R5IM loss data, n = glob file index not BLM index
    # fetch_stored_data(n, None, True) = cycle data, n = glob file index not BLM index
    #y data variable
        y=p[i]
        ax.plot(x_data,y , zs=i, zdir='y', alpha=0.8)



    lines = [ax.plot([], [], [], '-', lw=0.5)[0] for i in range(num_lines)]
    def update(frame):
        for m in blm_iterator_list:
            Z[1:, :] = Z[:-1, :]
            Z[0, :] = ax.plot(x_data,y , zs=m, zdir='y', alpha=0.8)

            reversed_data = Z[::-1, :]
        lines_data = []
        for i in range(num_lines):
            lines_data.append(list(zip(x, [i]*num_points, reversed_data[i, :])))

        for i, line in enumerate(lines):  
            line.set_data(x, [y[i]]*num_points)
            line.set_3d_properties(Z[i, :])

        ax.set_xlim3d(-0.5, 2200)
        ax.set_ylim3d(0, num_lines)
        ax.set_zlim3d(0, 0.50)   



waterfall(p)
anim=FuncAnimation(fig, update, frames=range(num_lines-1), interval=1000)
f = r"C:\Users\44777\Desktop\animation.gif"
writergif = animation.PillowWriter(fps=30)
anim.save(f, writer=writergif)
plt.show()