import pandas as pd
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt 


def getTimeList(data):
    times = {}
    data = data.reindex(index=data.index[::-1])
    for index , row in data.iterrows():
        if row['symbol'] not in times.keys():
               times[row['symbol']] = []
               
        times[row['symbol']].append(row['start'])
        times[row['symbol']].append(row['end'])
    return times

def timeSplitter(data):
    seconds = []
    for i in data:
        seconds.append(i.split(' '))
    return seconds

def timeMinus(data):
    newTime = []
    for i in data:
        newTime[i] = data[i + 1] - data[1]
    return newTime


def convertToSeconds(data):
    seconds = int(data[0]) * 60 * 60 + int(data[1]) * 60 + int(data[2])
    return seconds


def expandData(data):
    x = 1
    lst = []
    for i in range(len(data)):
        lst += data[i] * [x]
        x = (x + 1) % 2
    
    return lst


def removeDate(data):
    newList = []
    finalList = []
    for i in data:
        newList.append(i[9:18])
        
    for i in range(1,len(newList)):
        end = convertToSeconds(newList[i].split(':'))
        start = convertToSeconds(newList[i - 1].split(':'))
        x = end - start
        finalList.append(x)

    # print(finalList)
    return expandData(finalList)
    

def plotWaveform(data, title, plot, index):
    xs = np.repeat(range(len(data)), 2)
    ys = np.repeat(data, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plot[index].plot(xs, ys)
    plot[index].set_yticks(np.arange(0,1.1,1))
    plot[index].set_title(title)



df = pd.read_csv('TASK1.4.4.csv', sep = ',', names = ['start', 'end', 'symbol', 'value', 'unknon', 'other'])
data = getTimeList(df)

fig, plot = plt.subplots(len(data))
fig.text(0.5, 0.04, 'time (seconds)', ha='center', va='center')
fig.text(0.06, 0.5, 'state', ha='center', va='center', rotation='vertical')

i = 0
for key, values in data.items():
    newValue = removeDate(values)
    plotWaveform(newValue, key, plot, i)
    i += 1

plt.show()