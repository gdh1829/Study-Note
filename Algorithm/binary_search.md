# Binary Search

## Intuition
- 정렬된 배열이 필수 사용 조건
- Mid 위치의 값을 찾아 절반씩 narrow down하며 찾아가는 방식으로 시간복잡도: O(Log(N))

## Vanilla binary search implementation
```java
public static int binarySearch(List<Integer> arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    if (right == 0) return -1;
    
    // Not to miss edge case of a one-element array, equality comparison should be included.
    while (left <= right) {
        // Calculating mid to avoid potential integer overflow when the number of elements is even.
        final int mid = left + (right - left) / 2;
        
        if (arr.get(mid) == target) return mid;   
        
        // Discard the other side
        if (arr.get(mid) < target) {
                left = mid + 1;   
        } else {
                right = mid - 1;   
        }
    }
    
    return -1;
}
```

## Edge cases

### Finding the Boundary
- true/false 두 섹션으로 구분되는 arr가 있다.
- 왼쪽은 모두 false로, 오른쪽은 모두 true로 구성.
- false/true가 구분되는 경계의 true의 위치 찾기.

```java
// the leftmost true's index 방식.
public static int findBoundary(boolean[] arr) {
    int left = 0;
    int right = arr.length - 1;

    if (!arr[left] && !arr[right]) return -1;
    
    while (left <= right) {
        if (arr[left]) return left;
        
        final int mid = left + (right - left) / 2;
        
        // Edge case, you need current element!
        if (arr[mid]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    
    return -1;
}

// record boundary index 방식. 
// 장점) 바닐라 바이너리 검색 구현에서 기록을 위한 boundaryIndex 변수 선언 외에는 달라지는 점이 없다!
public static int findBoundary(boolean[] arr) {
    int left = 0;
    int right = arr.length - 1;
    int boundaryIndex = -1;

    if (!arr[left] && !arr[right]) return boundaryIndex;
    
    while (left <= right) {
        final int mid = left + (right - left) / 2;
        
        // No Edge case about the current element!
        if (arr[mid]) {
            boundaryIndex = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return boundaryIndex;
}
```
