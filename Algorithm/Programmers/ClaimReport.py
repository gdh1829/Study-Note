# 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

import pprint
from typing import List, Set, Dict, Tuple
from collections import defaultdict


def solution(id_list: List[str], report_list: List[str], k: int):
    answer = []

    reporter_dict: Dict[str, Set[str]] = defaultdict(set)
    reportee_dict: Dict[str, Set[str]] = defaultdict(set)
    for report in report_list:
        values = report.split(" ")
        reporter, reportee = values[0], values[1]

        reportee_dict[reportee].add(reporter)
        reporter_dict[reporter].add(reportee)

    stopped_id = set()
    for reportee, reporters in reportee_dict.items():
        if len(reporters) >= k:
            stopped_id.add(reportee)

    for id in id_list:
        if id not in reporter_dict:
            answer.append(0)
            continue

        count = 0
        for reportee in reporter_dict[id]:
            if reportee in stopped_id:
                count += 1

        answer.append(count)

    return answer


def solution2(id_list: List[str], report_list: List[str], k: int):
    answer = [0] * len(id_list)
    reports: Dict[str, int] = {x: 0 for x in id_list}

    for r in set(report_list):
        reportee = r.split()[1]
        reports[reportee] += 1

    for r in set(report_list):
        reportee = r.split()[1]
        if reports[reportee] >= k:
            reporter = r.split()[0]
            answer[id_list.index(reporter)] += 1

    return answer

# [2,1,1,0]
case1 = (
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
    2
)
# [0,0]
case2 = (
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
)

print(solution(*case1))
print(solution(*case2))

print(solution2(*case1))
print(solution2(*case2))