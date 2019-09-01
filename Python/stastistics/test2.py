# native modules
import argparse
import datetime

# external modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# from pandas.plotting import register_matplotlib_converters
from urllib.parse import unquote

# register_matplotlib_converters()
# filePath = "./apache-sample.2019-08-09.log"
filePath = "./access_hrbc-jp.porterscloud.com.log-20190817"


def parseApacheLog(filePath):
    # 주의사항: 필드네임 설정시, 해당 파일의 필드 수에 딱 맞도록 설정하지 않으면, sep의 기준과 다르게 데이터프레임이 만들어짐
    fieldsNames = ['host', 'identity', 'unknown1', 'unknown2', 'time_part1', 'time_part2', 'cmd_path_proto', 'http_code', 'response_bytes', 'referer', 'user_agent', 'processing_time', 'user_info', 'unknown3', 'unknown4']
    rawData = pd.read_csv(filePath, sep=' ', header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    time = rawData.time_part1 + rawData.time_part2
    timeTrimmed = time.map(lambda s: s.strip('[]').split('+')[0])
    rawData['time'] = pd.to_datetime(timeTrimmed, format='%d/%b/%Y:%H:%M:%S')
    rawData['method'], rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split().tolist())
    rawData['path'] = rawData['path'].map(lambda s: unquote(s))

    framedData = rawData.drop(['time_part1', 'time_part2', 'cmd_path_proto', 'unknown1', 'unknown2', 'unknown3', 'unknown4'], axis=1)
    return framedData.dropna(axis=1, how='all')

data = parseApacheLog(filePath)
# print(data['processing_time'])

plotDf = pd.DataFrame(data={'processing_time':data['processing_time'], 'datetime':data['time']})
print(plotDf)
# fig = plt.figure(figsize=(15,15))
fig = plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('access log')
plt.xlabel('date')
plt.ylabel('processing time')
ax = plt.subplot()
plt.plot(plotDf['datetime'], plotDf['processing_time'])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%Y-%m-%d'))
_ = plt.xticks(rotation=45)
plt.grid(True)
fig.savefig('plot2.png')
# fig = plt.figure()
# axes = plt.subplot()
# axes.plot(plotDf)
# axes.grid(True)
# plt.show()


