import pandas as pd
from datetime import datetime
import 


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
    print(seconds)
    return seconds

def timeMinus(data):
    newTime = []
    for i in data:
        newTime[i] = data[i + 1] - data[1]
    return newTime


def convertToSeconds(data):
    seconds = int(data[0]) * 60 * 60 + int(data[1]) * 60 + int(data[2])
    return seconds


def removeDate(data):
    newList = []
    finalList = []
    for i in data:
        newList.append(i[9:18])
    # for i in newList:
    #     finalList.append(int(i.replace(":", "")))
    print(newList)
    print('*'*30)
    format = '%H:%M:%S'
    for i in range(1,len(newList)):
        end = convertToSeconds(newList[i].split(':'))
        start = convertToSeconds(newList[i - 1].split(':'))
        x = end - start
    # x = my_list[i] - my_list[i-1]
        # y = str(x)
        finalList.append(x)
    # print(finalList)

    # for i in finalList:
    #     finalList.append(i[5:6])

    print(finalList)
    return finalList
    




df = pd.read_csv('lab2-2.4.csv', sep = ',', names = ['start', 'end', 'symbol', 'value', 'unknon', 'other'])
newFunction = getTimeList(df)

newValue = removeDate(newFunction)


#getTimeList(df)


