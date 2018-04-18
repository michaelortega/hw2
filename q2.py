# CS299
# HW 2
# @author Michael
import matplotlib.pyplot as plt
import numpy as np
import random as rand
import pandas as pd
from collections import OrderedDict


def generate_data_set():
    return summary_statistics([rand.randint(1, 555) for i in range(100)])


def plot():
    data_set_1 = generate_data_set()
    data_set_2 = generate_data_set()
    data_set_3 = generate_data_set()

    data_frame1 = pd.DataFrame(data_set_1, columns=['max', 'min', 'mean', 'stdev', 'median', 'perc75', 'perc25'],
                     index=['data1'])
    data_frame2 = pd.DataFrame(data_set_2, columns=['max', 'min', 'mean', 'stdev', 'median', 'perc75', 'perc25'],
                      index=['data2'])
    data_frame3 = pd.DataFrame(data_set_3, columns=['max', 'min', 'mean', 'stdev', 'median', 'perc75', 'perc25'],
                      index=['data3'])

    list_of_data_frames = [data_frame1, data_frame2, data_frame3]

    for plots in list_of_data_frames:
        plt.plot(plots.iloc[:, 0], marker='+', color="red")
        plt.plot(plots.iloc[:, 1], marker='x', color="red")
        plt.plot(plots.iloc[:, 2], marker='x', color="blue")
        plt.plot(plots.iloc[:, 3], marker='^', color="orange")
        plt.plot(plots.iloc[:, 4], marker='v', color="green")
        plt.plot(plots.iloc[:, 5], marker='>', color="blue")
        plt.plot(plots.iloc[:, 6], marker='<', color="blue")

    plt.xlabel('Data Set')
    plt.ylabel('Values')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.35, 1.02))

    plt.show()


def summary_statistics(listOfNums):
    maxVal = max(listOfNums)
    minVal = min(listOfNums)
    meanVal = np.mean(listOfNums)
    stdev = np.std(listOfNums)
    median = np.median(listOfNums)
    perc75 = np.percentile(listOfNums, 75)
    perc25 = np.percentile(listOfNums, 25)
    return {'max': maxVal,
            'min': minVal,
            'mean': meanVal,
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}


plot()
