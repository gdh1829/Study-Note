# Kotlin Collection

## Collection Copy
- 컬렉션의 카피 함수는 동일 요소에 대한 Shallow copy로 구성된 요소로 만들어진 복사 컬렉션을 만든다.
- 즉 각 요소에 반영되는 변경사항은 모든 복제 컬렉션에도 반영된다. 
- 컬렉션 카피 함수: toList, toMutableList, toSet, etc
  - 원본 컬렉션의 특정 순간의 스냅샷으로 동일 요소로 구성된 새 컬렉션이다.
  - 원본 컬렉션에 insert, remove가 발생하더라도 복제본에 영향을 주지 않는다. 원본과 독립적으로 변화한다.
```kotlin
val alice = Person("Alice")
val sourceList = mutableListOf(alice, Person("Bob"))
val copyList = sourceList.toList()
sourceList.add(Person("Charles"))
alice.name = "Alicia"
// First item's name is: Alicia in source and Alicia in copy
// 요소는 shallow copy로서 원본과 복제 컬렉션 모두에 영향 
println("First item's name is: ${sourceList[0].name} in source and ${copyList[0].name} in copy")
// List size is: 3 in source and 2 in copy
// 복제 컬렉션 자체는 원본과 독립으로 새 요소의 추가나 삭제에 영향 받지 않음
println("List size is: ${sourceList.size} in source and ${copyList.size} in copy")
```