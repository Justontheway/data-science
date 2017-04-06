#-*- coding:utf-8 -*-
'''
Normal Distribution, also called Gaussian Distribution
'''

import numpy as np
import matplotlib.pyplot as plt

def simple_plot():
    x = np.linspace(0, 10, 10000)
    y = np.random.normal(0, x)
    z = np.cos(x**2)

    plt.figure(figsize = (8, 4))
    plt.plot(x, y, label = "sin(x)", color = "red", linewidth = 2)
    plt.plot(x, z, "b--", label = "cos(x^2)")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PyPlot First Example")
    plt.ylim(-1.2, 1.2)
    plt.legend()
    plt.show()

def normal_plot(mu = 0, sigma = 1, num = 1000):
    y = np.random.normal(mu, sigma, num)

    plt.figure(figsize = (8, 4))
    plt.plot(y, label = "norm", color = "red", linewidth = 2)
    plt.xlabel("X")
    plt.ylabel("Distribution")
    plt.title("Normal-Distribution")
    plt.legend()
    plt.show()

def normal_distribution(mu = 0, sigma = 1, start = None, end = None, num = 1000):
    if start and end:
        x = np.linspace(start, end, num)
    else:
        x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, num)
    # gaussian density function
    y = np.e ** ((x - mu)**2 / (-2 * sigma ** 2)) / np.sqrt(2 * np.pi * sigma)

    plt.figure(figsize = (8, 4))
    plt.plot(x, y, color = "red", linewidth = 2)
    plt.xlabel("X")
    plt.ylabel("density")
    plt.title("Normal-Distribution")
    plt.show()


#simple_plot()
#normal_plot()
normal_distribution()


