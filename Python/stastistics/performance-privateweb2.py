#!/usr/bin/python3

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

parser = argparse.ArgumentParser(description = "aggregation of server performance")
parser.add_argument("--file", "-f", help = "file path", type = str, required=True)
args = parser.parse_args()

def parseApache(filePath):
    fieldsNames = ["company", "user", "timestamp", "db", "method", "path", "referer", "dummy1", "processing_time", "dummy2", "dummy3", "version", "ip"]
    rawData = pd.read_csv(filePath, sep=",", header=None, names=fieldsNames, na_values=["-"], encoding="utf-8", engine="python")
    framedData = rawData.drop(["user", "db", "dummy1", "dummy2", "dummy3", "version", "ip"], axis=1)
    framedData["referer"].astype(str)
    framedData["processing_time"].astype(float)
    framedData["timestamp"] = pd.to_datetime(framedData["timestamp"], format="%Y-%m-%d %H:%M:%S")
    return framedData.dropna(axis=1, how="all")

def isDetailView(path):
    if type(path) != str:
        return False
    p = re.compile(r"(^https\:\/\/hrbc-jp.porterscloud.com\/.+\/search)")
    result = p.search(path)
    return result is not None

def isMailSearch(path):
    if path == "/privateapi/mail/search-mails":
        return True
    return False

def getPurePath(path):
    if type(path) != str:
        return "None"
    return path.split("?")[0]

def convertMicro2Sec(millis):
    sec = millis/1000000
    return sec

def execScriptMode():
    apacheDf = parseApache(args.file)
    privateDf = apacheDf.loc[apacheDf["path"].str.startswith("/privateapi/")]
    print(privateDf)

    # filter
    # filteredDf = privateDf.filter(["path", "referer", "processing_time"])
    # filteredDf["path"] = filteredDf["path"].apply(lambda s : getPurePath(s))
    # filteredDf["referer"] = filteredDf["referer"].apply(lambda s : getPurePath(s))
    # filteredDf["processing_time"] = filteredDf["processing_time"].apply(lambda s : convertMicro2Sec(s))

    # ## referer - mail
    # searchMailsDf = filteredDf.loc[filteredDf["path"].str.startswith("/privateapi/mail/search-mails")]
    # print(searchMailsDf)
    # refererMailDf = searchMailsDf.loc[filteredDf["referer"].str.startswith("https://hrbc-jp.porterscloud.com/mail")]
    # print(refererMailDf)

    # per second request数
    # samplingData2 = pd.DataFrame(data={"timestamp": apacheDf["time"], "path": apacheDf["path"]})
    # result2 = samplingData2.groupby(["timestamp"])["path"].count().reset_index(name="count")
    # print(result2.sort_values("count", ascending=False).head(10))
    # print(result.head(10))

    # with pd.option_context("display.max_rows", None, "display.max_columns", None, "display.width", None):
    #     print(result["referer"].unique())
    #     print(apacheDf.tail(20))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 2]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 3]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 5]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 10]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 25]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 50]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 60]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 75]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))
    #     result3 = samplingData.loc[samplingData["processing_time"] > 100]
    #     print(result3.groupby("path")["path"].count().reset_index(name="count"))

if __name__ == "__main__":
    execScriptMode()
else:
    print("It\'s not supported, other than script mode")
