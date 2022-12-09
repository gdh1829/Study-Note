# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086
import pprint

def solution(s: str):
    answer = []
    
    # sList = list(s)

    # for i, v in enumerate(sList):

    #     answer.append(-1)

    #     step = -1
    #     movingCount = 0
    #     for pointer in range(i + step, 0 + step, step):
    #         movingCount += 1
            
    #         if sList[pointer] == v:
    #             answer[i] = movingCount
    #             break

    dic = dict()
    for i, v in enumerate(list(s)):
        if v not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[v])
        dic[v] = i    

    return answer

print(solution("banana")) # [-1, -1, -1, 2, 2, 2]
