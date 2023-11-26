# Kotlin Equality
크게 두가지 타입으로 구분
- Structural Equality: `==`, a check for `eqauls()`
- Referential Equality: `===`, two references point to the same object

## Structural Equality

- Structural Equality is checked by == operation.
- `a?.equals(b) ?: (b === null)`
  - 명시적으로 null 비교시(a == null), 이는 a === null으로 자동 번역된다.
- to custom equals check implementation, override the 'equals(other: Any?): Boolean' function
  - same name but different signatures, like `equals(other: Foo)`, don't affect equality checks with the operators == and !=.
- Structural Equality has nothing to do with comparison defined by the `Comparable<...>` interface

## Referential Equality
- is checked by `===` operation.
- For values represented by primitive types at runtime (ex, Int), the === equality check is equivalent to the == check.


## Floating-point numbers equality 

## Array equality
두 어레이가 같은 순서와 요소인지 비교한다면 `contentEquals()` 사용하라.
어레이에 `==`를 사용하는 것은 referential equality를 의미.
