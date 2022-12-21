"""
아이디어
- 완주자(completion)의 수를 dict로 치환.
- 문제의 조건이 참가자는 완주자보다 1명 더 많다고 했으므로 
    - 참가자(participant)를 loop 돌면서 완주자 수가 0이 되는 경우를 즉시 리턴.

복잡도
- O(N): 완주자 dict 치환 순환
- O(M): 참가자 loop를 돌면서 완주 참가자 dict 서치를 O(1)에 하므로 1*M -> M
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


case1 = (["leo", "kiki", "eden"],["eden", "kiki"])
case2 = (["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
case3 = (["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])

print(solution(*case1)) # "leo"
print(solution(*case2)) # "vinko"
print(solution(*case3)) # "mislav"

# 퍼포먼스     
# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.15ms, 10.4MB)
# 테스트 4 〉	통과 (0.42ms, 10.1MB)
# 테스트 5 〉	통과 (0.35ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (13.65ms, 21.8MB)
# 테스트 2 〉	통과 (28.55ms, 25.2MB)
# 테스트 3 〉	통과 (27.71ms, 27.5MB)
# 테스트 4 〉	통과 (23.49ms, 34MB)
# 테스트 5 〉	통과 (54.61ms, 33.9MB) 