# CS299
# HW 2
# @author Michael

import matplotlib.pyplot as plt
import random as rand
import collections
import pandas as pd


def scale_digits_nine(listOfNums):
    maximumValue = max(listOfNums)
    for index, i in enumerate(listOfNums):
        listOfNums[index] = round(9 * ((i - min(listOfNums)) / (maximumValue - min(listOfNums))))

    print(listOfNums)
    print("Occurrences: ", end="")
    print(collections.Counter(listOfNums))

    return collections.Counter(listOfNums)


data1 = [rand.randint(1, 555) for i in range(100)]
data2 = [rand.randint(1, 555) for i in range(100)]
data3 = [rand.randint(1, 555) for i in range(100)]

count_1 = scale_digits_nine(data1)
count_2 = scale_digits_nine(data2)
count_3 = scale_digits_nine(data3)

s = pd.Series(count_1, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
s2 = pd.Series(count_2, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
s3 = pd.Series(count_3, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

plot_1, = plt.plot(s, label='data 1', marker='+', color='red')
plot_2, = plt.plot(s2, label='data 2', marker='x', color='green')
plot_3, = plt.plot(s3, label='data 3', marker='*', color='blue')

plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.xlabel('values')
plt.ylabel('frequency')

plt.legend(handles=[plot_1, plot_2, plot_3], loc='upper right', bbox_to_anchor=(1.25, 1))
plt.show()
