# Kotlin ArrayDeque<T>

- double-ended 큐의 구현체로서 양 사이드로부터 삽입과 삭제를 허용한다.
- 이러한 성격으로 코틀린에서 Stack과 Queue 자료구조의 역할을 모두 수행한다.
  - 이면에는 필요에 따라 사이즈가 자동으로 조정되는 resizable array를 사용하고 있기 때문이다.
```kotlin
fun main() {
    val deque = ArrayDeque(listOf(1, 2, 3))

    deque.addFirst(0)
    deque.addLast(4)
    println(deque) // [0, 1, 2, 3, 4]

    println(deque.first()) // 0
    println(deque.last()) // 4

    deque.removeFirst()
    deque.removeLast()
    println(deque) // [1, 2, 3]
}
```
