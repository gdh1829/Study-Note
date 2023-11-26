# Kotlin Set

## Set equality
두 셋이 동일 사이즈와 각 elements들이 모두 동일하다면, equal하다고 여긴다.
셋의 특성이 순서가 없으므로 정의된 요소의 순서는 동일성에 영향이 없다.
```kotlin
val numbers = setOf(1, 2, 3, 4)
val numbersBackwards = setOf(4, 3, 2, 1)
println("The sets are equal: ${numbers == numbersBackwards}") // true

```

## MutableSet의 디폴트 구현: LinkedHashSet
- 요소 삽입의 순서를 보존한다.
- 따라서 first(), last()와 같은 함수는 순서에 의존하여 예측가능한 값을 리턴한다.

## HashSet
- 요소의 순서와는 전혀 관계가 없기에 first(), last() 함수는 예측불가한 값을 리턴한다.
- 상대적 장점은 순서를 보존하지 않기에 같은 데이터에 더 적은 메모리를 사용한다.
