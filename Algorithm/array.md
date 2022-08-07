# Array

## 소개
- Array는 근접한 메모리 위치에서 같은 타입의 값들을 들고 있다.
- Array가 들고 있는 items의 memory locations를 element라고 한다.
- Array는 이 elements의 컨테이너이다.
- total number of elements를 length라고 한다.
- array의 details은 position에 의해 접근되는데, 이를 index 또는 subscript라 한다.

## array in python
- 파이썬에서 array와 list는 다르다. list는 여러 데이터 타입을 저장할 수 있으나 array는 일관된 한 가지 타입만 허용한다.
```python
import array
# integer 타입 어레이 선언 및 초기화.
balance = array.array('i', [300,200,100])
# accesss -> 200
balance[1]
# insertion by index and value -> [300, 200, 150, 100]
# destructive method. other elements after the index are shifted to right. 
balance.insert(2, 150)
# deletion by value -> [300, 200, 100]
# destructive method. both items and indices are re-assigned.
balance.remove(150)
# search by value -> 2
# non-destructive method. not affect the array values.
balance.index(100)
# update
balance[2] = 150
# traverse
for x in balance:
```

## 장점
- 동일 타입을 갖는 요소를 복수 저장 가능. 요소 중복 허용.
- 인덱스를 알고 있는 한 빠르게 원하는 요소로 접근 가능. 
    - head로부터 traverse해야하는 LinkedList는 반대.

## 단점
- Array의 중간에 요소를 넣거나 빼는 것은 느리다.
    - new/missing 요소를 수용하기 위해 남아있는 요소들이 shift되어야하기 때문
    - array의 제일 끝 위치에 insert/remove하는 경우는 예외
- Java와 같은 언어들은 array의 사이즈가 고정되어 있어, 초기화 이후에는 사이즈를 변경할 수 없음.
    - 새로운 insertion이 array의 사이즈를 초과하게 한다면, 새 array가 allocated 되고 기존 elements들은 새 array로 copy over된다. 
    - 새 array를 만들고 구 array의 elements을 옮기는 과정은 O(n)의 시간 소요.

## 용어 정리
Array 관련 common terms
- Subarray: array 내부에서 근접한 연속된 부분이라 할 수 있음 
    - a range of contiguous values within an array.
    - [2,3,6,1,5,4]: [3,6,1] is subarray. [3,1,5] is not!
- Subsequence: 순서의 변경없이 내부 요소들의 insert/removal에 의해 파생된 것이라 할 수 있음.
    - a sequnce that can be derived from the given sequence by deleting some or no elements wihtout changing the order of the remaining elements.(나머지 요소들의 순서를 변경하지 않고 일부를 삭제하거나 삭제하지 않고 주어진 시퀀스에서 파생된 것) 
    - [2,3,6,1,5,4]: [3,1,5] is sequence [3,5,1] is not!

## 시간복잡도
<table>
<tr>
    <th>op</th>
    <th>Big-O</th>
    <th>Note</th>
</tr>
<tr>
    <td>access</td>
    <td>O(1)</td>
    <td></td>
</tr>
<tr>
    <td>search</td>
    <td>O(n)</td>
    <td></td>
</tr>
<tr>
    <td>search(sorted array)</td>
    <td>OLog(n)</td>
    <td>바이너리 서치 이용시</td>
</tr>
<tr>
    <td>insert</td>
    <td>O(n)</td>
    <td>삽입은 오른쪽으로 subsequent 요소를 전부 쉬프팅 시켜야하므로 O(n)</td>
</tr>
<tr>
    <td>insert at the end</td>
    <td>O(1)</td>
    <td>맨 끝 삽입은 쉬프팅 시켜야할 요소가 없으므로 O(1)</td>
</tr>
<tr>
    <td>remove</td>
    <td>O(n)</td>
    <td>삽입과 마찬가지로 남은 요소들을 모두 쉬프팅 시켜야하므로</td>
</tr>
<tr>
    <td>remove at the end</td>
    <td>O(1)</td>
    <td>맨 끝 삭제 또한 쉬프팅 시켜야할 요소가 없으므로 O(1)</td>
</tr>

## 주의사항
- array에 중복 값이 존재하는지 확인. 중복 값의 존재가 정답에 영향을 주는가? 중복 값이 문제를 간단 또는 어렵게 만드는가?
- index를 이용하여 array를 순회할 때, bound를 넘어서지 않도록 주의
- array를 slicing하거나 concatenating을 할때 주의가 필요. O(n)의 시간이 걸리므로 가능하다면 subarray/rage의 시작과 끝 경계를 정해야 한다.

## 코너 케이스
- empty sequence
- sequence with 1 or 2 elements
- sequence with repeated elements
- duplicated values in the sequence

## 테크닉
- sliding window
    - 두 포인터는 항상 같은 방향으로 움직이며 서로를 차지하지 않는다.
    - 이 점은 각 값들이 최대 2번만 방문되고 시간 복잡도는 여전히 O(n)이다.
    - ex. Longest substring without repeating characters, Min size subarrary sum, min window subsring
- two pointers
    - 연속적이고 길이가 가변적인 부분 배열들을 활용하여 특정 조건을 일치시키는 알고리즘
    - 슬라이딩 윈도우와 비슷하나 구간의 넓이가 조건에 따라 유동적으로 변함
    - 문제에 주어진 배열이 연속된 부분 배열을 통하여 해결하라는 것이 아니라면 투포인터 알고리즘은 사용 X
- traversing from the right
    - 관습적인 왼쪽으로부터의 접근 대신에, 오른쪽으로부터 시작하는 array를 탐색하기
- sorting the array
    - array가 일부 또는 전체가 sorted라면, binary search가 가능
- precomputation
    - subarray의 곱이나 합계와 관련된 문제라면, hasing이나 prefix/suffix sum/product를 이용한 pre-computataion이 효과적일 수 있다.
- index has a hash key
    - 시퀀스가 주어지고 인터뷰어가 O(1)의 공간을 요한다면, array 자체를 hash table로서 사용할 수 있을지도 모른다.
    - 1부터 N까지의 값을 갖는 array가 있고 N은 array의 길이라면, 해당 인덱스의 값(minus one)은 해당 숫자의 존재를 의미한다.
- traversing the array more than once
    - array를 두번/세번 도는 것은 여전히 O(n)이다. 때로는 array를 한번 이상 도는 것이 문제를 푸는데 도움이 되고, 시간 복잡도는 O(n)을 유지한다.
