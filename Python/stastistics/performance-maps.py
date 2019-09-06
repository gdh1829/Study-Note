# native modules
import argparse
import datetime
from urllib.parse import unquote
import re

# external modules
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description = 'aggregation of server performance')
parser.add_argument('--filePath', '-f', help = 'log file path and also multiple files is possible with delimeter comma(,) ex)./apache-sample.2019-08-09.log,./apache-sample.2019-08-10.log', type = str, required=True)
args = parser.parse_args()
filePath = args.filePath
frameList = []


def parseApacheLog(filePath):
    fieldsNames = ['host', 'identity', 'unknown1', 'unknown2', 'time_part1', 'time_part2', 'cmd_path_proto', 'http_code', 'response_bytes', 'referer', 'user_agent', 'processing_time', 'user_info', 'unknown3', 'unknown4']
    rawData = pd.read_csv(filePath, sep=' ', header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    time = rawData.time_part1 + rawData.time_part2
    timeTrimmed = time.map(lambda s: s.strip('[]').split('+')[0])
    rawData['time'] = pd.to_datetime(timeTrimmed, format='%d/%b/%Y:%H:%M:%S')
    rawData['method'], rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split().tolist())
    rawData['path'] = rawData['path'].map(lambda s: unquote(s))

    framedData = rawData.drop(['time_part1', 'time_part2', 'cmd_path_proto', 'unknown1', 'unknown2', 'unknown3', 'unknown4'], axis=1)
    return framedData.dropna(axis=1, how='all')

def parseMapsTomcatAccessLog(filePath):
    fieldsNames = ['host', 'identity', 'user', 'time_part1', 'time_part2', 'cmd_path_proto', 'http_code', 'response_bytes', 'processing_time']
    rawData = pd.read_csv(filePath, sep=' ', header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    time = rawData.time_part1 + rawData.time_part2
    timeTrimmed = time.map(lambda s: s.strip('[]').split('+')[0])
    rawData['time'] = pd.to_datetime(timeTrimmed, format='%d/%b/%Y:%H:%M:%S')
    # rawData['method'], rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split().tolist())
    rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split(' H').tolist())
    rawData['path'] =  rawData['path'].map(lambda s: unquote(s))

    framedData = rawData.drop(['identity', 'user', 'time_part1', 'time_part2', 'cmd_path_proto'], axis=1)
    return framedData.dropna(axis=1, how='all')

def returnRootPath(path):
    p = re.compile(r'(\/?\d+)+')
    arr = p.split(path)
    return arr[0]

def convertMilli2Sec(millis):
    sec = millis/1000
    return sec

files = filePath.split(',')
print(files)

concatenatedDf = pd.concat([parseMapsTomcatAccessLog(f) for f in files])
concatenatedDf.drop(concatenatedDf[concatenatedDf['http_code'] >= 400].index, inplace = True)
print(concatenatedDf.shape)




## percentile
samplingData = pd.DataFrame(data={'time': concatenatedDf['time'], 'path': concatenatedDf['path'], 'processing_time': concatenatedDf['processing_time']})
# samplingData = pd.DataFrame(data={'path': concatenatedDf['path'], 'processing_time': concatenatedDf['processing_time']})
samplingData['path'] = samplingData['path'].apply(lambda s : returnRootPath(s))
samplingData['processing_time'] = samplingData['processing_time'].apply(lambda s : convertMilli2Sec(s))
# result = samplingData.groupby('path')['processing_time'].describe()
# print(result.sort_values('count', ascending=False))
# print(samplingData.groupby('path')['processing_time'].quantile(.98))
# print(samplingData.groupby('path')['processing_time'].quantile(.996))
# print(samplingData.groupby('path')['processing_time'].quantile(.997))
# print(samplingData.groupby('path')['processing_time'].quantile(.998))
# print(samplingData.groupby('path')['processing_time'].quantile(.999))
print(samplingData.groupby('path')['processing_time'].quantile(.9995))

# per second request数
# samplingData2 = pd.DataFrame(data={'timestamp': concatenatedDf['time'], 'path': concatenatedDf['path']})
# result2 = samplingData2.groupby(['timestamp'])['path'].count().reset_index(name="count")
# print(result2.sort_values('count', ascending=False).head(10))
# print(result.head(10))

# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#     result3 = samplingData.loc[samplingData['processing_time'] > 2]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 3]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 5]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 10]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 25]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 50]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 60]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 75]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))
#     result3 = samplingData.loc[samplingData['processing_time'] > 100]
#     print(result3.groupby('path')['path'].count().reset_index(name="count"))


