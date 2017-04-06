#-*- coding:utf-8 -*-
'''
Linear Aggregation
NOTE: x_label should be `m * n` dataset.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def linear_aggregation(dataset, x_test):
    y_label = np.array([float(i) for i in dataset])
    x_label = np.linspace(1, y_label.size, y_label.size)

    model = LinearRegression()
    model.fit(x_label.reshape(-1, 1), y_label)
    y_test = model.predict(x_test)
    y_test = model.predict(x_label.reshape(-1, 1))

    plt.figure(figsize = (8, 4))
    plt.plot(x_label, y_label, label = "origin", color = "red", linewidth = 2)
    plt.plot(x_label, y_test, label = "predict", color = "blue", linewidth = 2)
    min_y = min(y_test.min(), y_label.min())
    max_y = max(y_test.max(), y_label.max())
    plt.ylim(min_y - 0.5 * abs(min_y), max_y + 0.5 * abs(min_y))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.title("Linear-Aggregation")
    plt.show()


dataset = [u'0.7965', u'0.8072', u'0.8342', u'0.8244', u'0.8000', u'0.8025', u'0.8119', u'0.8172', u'0.8109', u'0.8095', u'0.8161', u'0.8009', u'0.7911', u'0.7780', u'0.8197', u'0.8101', u'0.8280', u'0.8408', u'0.8390']
linear_aggregation(dataset, len(dataset) + 1)

