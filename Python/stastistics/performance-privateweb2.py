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

def parseApacheLog(filePath):
    fieldsNames = ['company', 'user', 'timestamp', 'db', 'method', 'path', 'referer', 'dummy1', 'processing_time', 'dummy2', 'dummy3', 'version', 'ip']
    rawData = pd.read_csv(filePath, header=None, names=fieldsNames, na_values=['-'], encoding='utf-8')
    framedData = rawData.drop(['user', 'db', 'dummy1', 'dummy2', 'dummy3', 'version', 'ip'], axis=1)
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


concatenatedDf = parseApacheLog(args.file)
privateDf = concatenatedDf.loc[concatenatedDf['path'].str.startswith('/privateapi/')]
print(privateDf)


## sampling data
# samplingData = pd.DataFrame(data={'time': concatenatedDf['time'], 'path': concatenatedDf['path'], 'processing_time': concatenatedDf['processing_time'], 'referer': concatenatedDf['referer']})
# samplingData['path'] = samplingData['path'].apply(lambda s : returnRootPath(s))
# samplingData['referer'] = samplingData['referer'].apply(lambda s : extractEndpoint(s))
# samplingData['processing_time'] = samplingData['processing_time'].apply(lambda s : convertMicro2Sec(s))

## filter
filteredDf = privateDf.filter(['path', 'referer', 'processing_time'])
# filteredDf.dropna(axis=1, how='any')
filteredDf['path'] = filteredDf['path'].apply(lambda s : returnRootPath(s))
filteredDf['referer'] = filteredDf['referer'].apply(lambda s : extractEndpoint(s))
filteredDf['processing_time'] = filteredDf['processing_time'].apply(lambda s : convertMicro2Sec(s))

## referer - mail
searchMailsDf = filteredDf.loc[filteredDf['path'].str.startswith('/privateapi/mail/search-mails')]
print(searchMailsDf)
refererMailDf = searchMailsDf.loc[filteredDf['referer'].str.startswith('https://hrbc-jp.porterscloud.com/mail')]
print(refererMailDf)

# print(filteredDf[filteredDf['path'].str.contains(r'^\/privateapi\/mail\/search-mails')])
# refererMailDf = filteredDf[filteredDf['referer'].str.contains(r'^https\:\/\/hrbc-jp.porterscloud.com\/mail')]
# print(refererMailDf[refererMailDf['path'].str.contains(r'^\/privateapi\/mail\/search-mails')])

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


