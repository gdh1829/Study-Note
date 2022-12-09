# 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

import pprint
from typing import List, Set, Dict, Tuple
from collections import defaultdict

def solution(id_list: List[str], report_list: List[str], k: int):
    answer = []

    reporterDict: Dict[str, Set[str]] = defaultdict(set)
    reporteeDict: Dict[str, Set[str]] = defaultdict(set)
    for report in report_list:
        values = report.split(" ")
        reporter, reportee = values[0], values[1]

        reporteeDict[reportee].add(reporter)
        reporterDict[reporter].add(reportee)

    stoppedId = set()
    for reportee, reporters in reporteeDict.items():
        if len(reporters) >= k:
            stoppedId.add(reportee)

    for id in id_list:
        if id not in reporterDict:
            answer.append(0)
            continue

        count = 0
        for reportee in reporterDict[id]:
            if reportee in stoppedId:
                count += 1
        
        answer.append(count)

    return answer

# [2,1,1,0]
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) 