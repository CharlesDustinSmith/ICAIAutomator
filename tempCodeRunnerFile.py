import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt 


def getTimeList(data):
    times = []
    data = data.reindex(index=data.index[::-1])
    for index , row in data.iterrows():
        times.append(row['start'])
        times.append(row['end'])
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
        
    print(newList)
    for i in range(1,len(newList)):
        end = convertToSeconds(newList[i].split(':'))
        start = convertToSeconds(newList[i - 1].split(':'))
        x = end - start
        finalList.append(x)

    return expandData(finalList)
    

def plotWaveform(data, title):
    xs = np.repeat(range(len(data)), 2)
    ys = np.repeat(data, 2)
    xs = xs[1:]
    ys = ys[:-1]
    plt.plot(xs, ys)
    plt.yticks(np.arange(0,1.1,1))
    plt.title(title)

fileName = input("Enter file name : ")
df = pd.read_csv( fileName + '.csv', sep = ',', names = ['start', 'end', 'symbol', 'value', 'unknon', 'other'])

data = getTimeList(df)

# fig, plot = plt.plot()
# fig.text(0.5, 0.04, 'time (seconds)', ha='center', va='center')
# fig.text(0.06, 0.5, 'state', ha='center', va='center', rotation='vertical')


newValue = removeDate(data)
plotWaveform(newValue, fileName)

plt.show()