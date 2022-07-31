# Kotlin visibility modifier

Kotlin의 visibility modifier는 Java와 비슷하지만 조금 다르다.

## Java인 경우, 
1)same class, 2)same package subclass, 3)same package non-subclass, 4)different package subclass, 5)different package non subclass들이 있다면,
- public: for all
- protected: 1), 2), 3), 4)
- default: 1), 2), 3) <- 아무것도 선언하지 않았을 시
- private: 1) only

## Kotlin인 경우
### Package
functions, properties, classes, objects and interfaces는 패키지 내부의 top-level에 직접 선언될 수 있다.
```kotlin
// file name: example.kt
package foo

fun baz() { ... }
class Bar { ... }
```
이 경우 visibility modifer의 바운더리는, 
- public: visible from everywhere, which is default if you don't use a visibility modifer.
- protected: not visible for top-level declarations.
- internal: visible from the same module
- private: visible only in the same file that contains the declarations.

### Class members
- private: 클래스 내부에서만 접근 가능
    - __kotlin에서는 outer class는 inner class의 private member가 보이지 않음!__
- protected: private + subclass에서도 접근 가능
- internal: 같은 모듈 내에서 해당 클래스를 볼 수 있다면, internal members에도 접근 가능
- public: everywhere

### Constructors
kotlin은 기본적으로 모든 constructor는 default가 public이다.
단, primary constructor의 visibility를 지정하기 위하여 `constructor`라는 키워드를 명시적으로 사용해야 한다.
```kotlin
class C private constructor(a: Int) { ... }
```

### Local declarations
local variable, functions, and classes는 visibility modifiers를 갖을 수 없다.


---
ref) https://kotlinlang.org/docs/visibility-modifiers.html