# native modules
import argparse
import datetime

# external modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
from urllib.parse import unquote



filePath = "./apache-sample.2019-08-09.log"
filePath = "./access_hrbc-jp.porterscloud.com.log-20190817"


def parseApacheLog(filePath):
    fieldsNames = ['host', 'identity', 'user', 'time_part1', 'time_part2', 'cmd_path_proto', 'http_code', 'response_bytes', 'referer', 'user_agent', 'unknown']
    rawData = pd.read_csv(filePath, compression='infer', sep=' ', header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    time = rawData.time_part1 + rawData.time_part2
    timeTrimmed = time.map(lambda s: s.strip('[]').split('-')[0])
    rawData['time'] = pd.to_datetime(timeTrimmed, format='%d/%b/%Y:%H:%M:%S')
    rawData['method'], rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split().tolist())
    rawData['path'] = rawData['path'].map(lambda s: unquote(s))

    framedData = rawData.drop(['time_part1', 'time_part2', 'cmd_path_proto'], axis=1)
    return framedData.dropna(axis=1, how='all')

data = parseApacheLog(filePath)
print(data)

plotDf = pd.DataFrame(data['response_bytes'], index=data['time'])

register_matplotlib_converters()
plt.title('access log')
plt.plot(data['time'], data['response_bytes'])
# plt.show()
fig = plt.figure()
ax = plt.subplot()
ax.plot(data['time'], data['response_bytes'])
ax.grid(True)
fig.savefig('plot.png')


