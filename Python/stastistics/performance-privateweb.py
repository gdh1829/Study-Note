# native modules
import argparse
import datetime
from urllib.parse import unquote
import re
import math
import glob

# external modules
# import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description = 'aggregation of server performance')
parser.add_argument('--file', '-f', help = 'log file path and also multiple files is possible with delimeter comma(,) ex)access_hrbc-jp.porterscloud.com.log-20190904', type = str, required=True)
args = parser.parse_args()
base = '/home/daehyeop.ko/winhome/Source/ko-tools/stastistics/private-web/httpd/*/'
files = [f for f in glob.glob(base + args.file, recursive=True)]

def parseApacheLog(filePath):
    fieldsNames = ['host', 'identity', 'unknown1', 'unknown2', 'time_part1', 'time_part2', 'cmd_path_proto', 'http_code', 'response_bytes', 'referer', 'user_agent', 'processing_time', 'user_info', 'unknown3', 'unknown4']
    rawData = pd.read_csv(filePath, sep=' ', header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    time = rawData.time_part1 + rawData.time_part2
    timeTrimmed = time.map(lambda s: s.strip('[]').split('+')[0])
    rawData['time'] = pd.to_datetime(timeTrimmed, format='%d/%b/%Y:%H:%M:%S')
    rawData['method'], rawData['path'], rawData['protocol'] = zip(*rawData['cmd_path_proto'].str.split().tolist())
    rawData['path'] = rawData['path'].map(lambda s: unquote(s))

    framedData = rawData.drop(['host', 'identity', 'time_part1', 'time_part2', 'cmd_path_proto', 'response_bytes', 'unknown1', 'unknown2', 'user_info', 'unknown3', 'unknown4'], axis=1)
    return framedData.dropna(axis=1, how='all')
    # return framedData.dropna(axis=1, thresh=5)

def extractEndpoint(fullPath):
    if type(fullPath) != str:
        return "None"
    return fullPath.split('?')[0]

def isDetailView(path):
    if type(path) != str:
        return False
    p = re.compile(r'(^https\:\/\/hrbc-jp.porterscloud.com\/.+\/search)')
    result = p.search(path)
    return result is not None

def isMailSearch(path):
    if path == '/privateapi/mail/search-mails':
        return True
    return False

def returnRootPath(path):
    return path.split('?')[0]

def convertMicro2Sec(millis):
    sec = millis/1000000
    return sec

# files = filePath.split(',')
# print(files)

concatenatedDf = pd.concat([parseApacheLog(f) for f in files])
concatenatedDf.drop(concatenatedDf[concatenatedDf['http_code'] >= 400].index, inplace = True)
# print(concatenatedDf.shape)


## sampling data
# samplingData = pd.DataFrame(data={'time': concatenatedDf['time'], 'path': concatenatedDf['path'], 'processing_time': concatenatedDf['processing_time'], 'referer': concatenatedDf['referer']})
# samplingData['path'] = samplingData['path'].apply(lambda s : returnRootPath(s))
# samplingData['referer'] = samplingData['referer'].apply(lambda s : extractEndpoint(s))
# samplingData['processing_time'] = samplingData['processing_time'].apply(lambda s : convertMicro2Sec(s))

## filter
filteredDf = concatenatedDf.filter(['path', 'referer', 'processing_time'])
filteredDf.dropna(axis=1, how='any')
filteredDf['path'] = filteredDf['path'].apply(lambda s : returnRootPath(s))
filteredDf['referer'] = filteredDf['referer'].apply(lambda s : extractEndpoint(s))
filteredDf['processing_time'] = filteredDf['processing_time'].apply(lambda s : convertMicro2Sec(s))

## referer - mail
print(filteredDf[filteredDf['path'].str.contains(r'^\/privateapi\/mail\/search-mails')])
refererMailDf = filteredDf[filteredDf['referer'].str.contains(r'^https\:\/\/hrbc-jp.porterscloud.com\/mail')]
print(refererMailDf[refererMailDf['path'].str.contains(r'^\/privateapi\/mail\/search-mails')])

# result = samplingData.loc[samplingData['path'] == '/privateapi/mail/search-mails']
# result = result.groupby('referer')['processing_time'].describe()
# print(result.sort_values('count', ascending=False))
# print(result.count())

# print(samplingData.groupby('path')['processing_time'].quantile(.98))
# print(samplingData.groupby('path')['processing_time'].quantile(.996))
# print(samplingData.groupby('path')['processing_time'].quantile(.997))
# print(samplingData.groupby('path')['processing_time'].quantile(.998))
# print(samplingData.groupby('path')['processing_time'].quantile(.999))
# print(samplingData.groupby('path')['processing_time'].quantile(.9995))

# per second request数
# samplingData2 = pd.DataFrame(data={'timestamp': concatenatedDf['time'], 'path': concatenatedDf['path']})
# result2 = samplingData2.groupby(['timestamp'])['path'].count().reset_index(name="count")
# print(result2.sort_values('count', ascending=False).head(10))
# print(result.head(10))

# with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
#     print(result['referer'].unique())
#     print(concatenatedDf.tail(20))
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


