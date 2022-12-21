# 프로그래머스 완주하지 못한 선수 문제

link: https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3

## 내 솔루션

```python3
"""
아이디어
- 완주자(completion)의 수를 dict로 치환.
- 문제의 조건이 참가자는 완주자보다 1명 더 많다고 했으므로 
    - 참가자(participant)를 loop 돌면서 완주자 수가 0이 되는 경우를 즉시 리턴.

복잡도
- O(N): 완주자 dict 치환 순환
- O(M): 참가자 loop
=> O(N+M)

자료구조
- 동명이인이 포함된 완주자명:숫자의 dict

"""

import collections

def solution(participant, completion):
    answer = ''
    
    completion_dict = collections.Counter(completion)
    for p in participant:
        if completion_dict[p] > 0:
            completion_dict[p] -= 1
            continue

        if completion_dict[p] == 0:
            answer = p
            break

    return answer

```

## 다른 사람 풀이

### 1

- 아래와 같은 풀이가 있었다.
- Counter 함수끼리 - 연산이 가능할 줄이야.. 새로 알게 된 사실.
- 문제 조건에 completion이 participant보다 1명 적다고 하였으므로 퍼포먼스는 early return하는 내 코드가 더 빠르나,
- 코드 가독성 측면에서는 너무나 간결한 풀이같다.

```python3
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

### 2

- hash의 가감을 이용한 풀이 방식이었다.
- hash collision만 발생하지 않는다면 문제될 것은 없어 보인다.

```python3
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
```
