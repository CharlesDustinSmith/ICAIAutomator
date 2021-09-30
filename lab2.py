import pandas as pd 

def getTimeList (data):
    times = []
    data = data.reindex(index=data.index[::-1])
    for index , row in data.iterrows():
        times.append(row['start'])
        times.append(row['end'])
        
    print (times)

    return times


df = pd.read_csv('lab2-2.4.csv', sep = ',', names = ['start', 'end', 'symbol', 'value', 'unknon', 'other'])
getTimeList(df)
