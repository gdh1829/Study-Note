# Kotlin Map

## Map<K, V>
- `Collection` 인터페이스를 상속하지 않지만 이 또한 kotlin collection 타입이다.
- key는 유니크하지만 서로 다른 키가 같은 value와 페어 가능.

## Map equality
- 두 맵이 동일한 페어로 구성되어 있다면 순서와 관계없이 동일하다고 본다.
```kotlin
val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key4" to 1)    
val anotherMap = mapOf("key2" to 2, "key1" to 1, "key4" to 1, "key3" to 3)

println("The maps are equal: ${numbersMap == anotherMap}") // true
```

## MutableMap의 디폴트 구현: LinkedHashMap
- 맵을 iteration시, 삽입 요소의 순서를 보존한다.
또 다른 구현인 HashMap
- 요소의 순서와 관계가 없다.
