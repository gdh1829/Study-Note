# Kotlin Collection

## List equality
두 리스트가 같은 사이즈와 structural equal elements를 같은 포지션에 갖고 있다면, equal하다고 여긴다.
```kotlin
val bob = Person("Bob", 31)
val people = listOf(Person("Adam", 20), bob, bob)
val people2 = listOf(Person("Adam", 20), Person("Bob", 31), bob)
println(people == people2) // true
bob.age = 32
println(people == people2) // false
```
```