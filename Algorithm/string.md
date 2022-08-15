# String

## Introduction
- is a sequence of characters.
- common data structures for looking up strings
    - `Trie/Prefix Tree`
    - `Suffix Tree`
- Common string algorithms
    - `Rabin karp` for efficient searching of substring using a rolling hash.
    - `KMP` for efficient searching of substring.

## 시간 복잡도
String은 characters의 array이므로, 기본적 문자열 operation은 array와 닮았다.
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Remove: O(n)

Operations involving another string: n, m은 각각 다른 문자열의 길이
- Find substring: O(n.m) - 가장 날 것의 방법일 경우. KMP나 Rabin Karp와 같은 알고리즘 사용시 더 빠름.
- Concatenating strings: O(n + m)
- Slice: O(m)
- Split (by token): O(n + m)
- Strip (remove leading and trailing whitespaces): O(n)

## 코너 케이스
- 빈 문자열
- 1 또는 2 캐릭터의 문자열
- 반복된 캐릭터의 문자열
- only distinct characters 문자열

## 테크닉
- Counting characters
    - 문자열에서 특정 문자의 빈도를 측정하는 문제를 자주 보게 되는데, 가장 흔한 해결 방식은 해쉬 테이블/맵을 이용하는 방법이다. 
- String of uniqe characters
- Anagram
- Palindrome
