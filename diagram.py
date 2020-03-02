'''
    Example how to use scientific modules like numpy for numeric calculations 
    and matplotlib for graphing. 

    remember to install numpy and matplotlib

    pip install numpy
    pip install matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()