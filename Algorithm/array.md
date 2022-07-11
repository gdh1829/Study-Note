# Array

## 장점
- 동일 타입을 갖는 요소를 복수 저장 가능. 요소 중복 허용.
- 인덱스를 알고 있는 한 빠르게 원하는 요소로 접근 가능. head로부터 traverse해야하는 LinkedList와는 반대.

## 단점
- Array의 중간에 요소를 넣거나 빼는 것은 느리다.
    - new/missing 요소를 수용하기 위해 남아있는 요소들을 위해 shift되어야하기 때문
    - array의 제일 끝 위치에 insert/remove하는 경우는 예외

## common terms
Array 관련 common terms]
- Subarray: array 내부에서 연속된 부분이라 할 수 있음 
    - a range of contiguous values within an array.
    - [2,3,6,1,5,4]: [3,6,1]은 subarray라 할 수 있음. [3,1,5]는 subarray가 아님
- Subsequence: 순서의 변경없이 내부 요소들의 insert/removal에 의해 파생된 것이라 할 수 있음.
    - a sequnce that can be derived from the given sequence by deleting some or no elements wihtout changing the order of the remaining elements.(나머지 요소들의 순서를 변경하지 않고 일부를 삭제하거나 삭제하지 않고 주어진 시퀀스에서 파생된 것) 
    - [2,3,6,1,5,4]: [3,1,5]는 subsequence이지만 [3,5,1]은 아님.

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
    <td>바이너리 서치 이용.</td>
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

## 테크닉
- sliding window
    - 투포인터와 유사하나 subarray의 크기가 고정적.
    - 사이즈가 고정적이기 때문에 배열의 구간을 정할 포인터 변수가 하나로 OK
    - 교집합의 정보를 공유하고, 차이가 나는 양쪽 끝 원소만 갱신
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
