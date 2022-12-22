# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0

    reset = True
    letter = ''
    first = 0
    others = 0
    for i in range(len(s)):
        if letter == '':
            letter = s[i]
            first += 1

        if i == len(s) - 1:
            if first > 0:
                answer += 1
            break

        if reset:
            letter = s[i]
            first = 1
            others = 0
            reset = False
            continue

        if letter == s[i]:
            first += 1
        else:
            others += 1

        if first == others:
            reset = True
            answer += 1
        
    return answer


case1 = "banana"
case2 = "abracadabra" # ab - ra - ca- da- br -a
case3 = "aaabbaccccabba"
case4 = "aaaaaaaaaaa" # aaaaaaaaaaa
case5 = "aaaaaaaaaab" # aaaaaaaaaab
case6 = "a" # a

print(solution(case1)) # 3
print(solution(case2)) # 6
print(solution(case3)) # 3
print(solution(case4)) # 1
print(solution(case5)) # 1
print(solution(case6)) # 1

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (1.70ms, 10.2MB)
# 테스트 3 〉	통과 (2.19ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.60ms, 10.4MB)
# 테스트 10 〉	통과 (1.14ms, 10.2MB)
# 테스트 11 〉	통과 (0.73ms, 10.2MB)
# 테스트 12 〉	통과 (0.91ms, 10.2MB)
# 테스트 13 〉	통과 (2.80ms, 10.2MB)
# 테스트 14 〉	통과 (1.77ms, 10.3MB)
# 테스트 15 〉	통과 (0.79ms, 10.2MB)
# 테스트 16 〉	통과 (2.93ms, 10.4MB)
# 테스트 17 〉	통과 (1.59ms, 10.2MB)
# 테스트 18 〉	통과 (1.42ms, 10.2MB)
# 테스트 19 〉	통과 (2.00ms, 10.3MB)
# 테스트 20 〉	통과 (1.52ms, 10.3MB)
# 테스트 21 〉	통과 (3.43ms, 10.3MB)
# 테스트 22 〉	통과 (2.35ms, 10.2MB)
# 테스트 23 〉	통과 (0.66ms, 10.2MB)
# 테스트 24 〉	통과 (0.66ms, 10.2MB)
# 테스트 25 〉	통과 (1.96ms, 10.2MB)
# 테스트 26 〉	통과 (1.67ms, 10.2MB)
# 테스트 27 〉	통과 (1.28ms, 10.2MB)
# 테스트 28 〉	통과 (1.49ms, 10.1MB)
# 테스트 29 〉	통과 (1.93ms, 10.2MB)
# 테스트 30 〉	통과 (0.89ms, 10.2MB)
# 테스트 31 〉	통과 (0.00ms, 10.3MB)
# 테스트 32 〉	통과 (0.01ms, 10.2MB)
# 테스트 33 〉	통과 (0.01ms, 10.2MB)
# 테스트 34 〉	통과 (0.01ms, 10.2MB)
# 테스트 35 〉	통과 (0.01ms, 10.3MB)
# 테스트 36 〉	통과 (0.01ms, 10.2MB)
# 테스트 37 〉	통과 (0.01ms, 10.3MB)
# 테스트 38 〉	통과 (0.01ms, 10.2MB)
# 테스트 39 〉	통과 (0.01ms, 10.3MB)
# 테스트 40 〉	통과 (0.03ms, 10.2MB)
# 테스트 41 〉	통과 (1.82ms, 10.2MB)
# 테스트 42 〉	통과 (1.84ms, 10.2MB)
