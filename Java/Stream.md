Stream
===

## 동작 순서
모든 요소가 첫 번째 중간 연산을 수행하고 남은 결과가 다음 연산으로 넘어가는 것(X)  
현 요소가 모든 파이프 라인을 거쳐서 결과를 만들어내고 다음 요소로 넘어가는 것(O)  

```java
List<String> list = new List("cb", "cba");
list.stream()
    .filter(ele -> {
        System.out.println("filter was called.");
        return ele.contains("a");
    })
    .map(ele -> {
        System.out.println("map was called.");
        return ele.toUpperCase();
    })
    .findFirst();
// <output>
// filter was called.
// filter was called.
// map was called.
```



## 성능향상
위에서 처럼 스트림은 한 요소씩 수직적으로 실행되기 때문에, 요소의 범위를 줄이는 작업(`skip`, `filter`, `distinct` 등)을 먼저 선행시키면 불필요한 연산을 예방하여 성능을 향상 시킬 수 있다.

```java
list.stream()
    .map(ele -> {
        wasCalled();
        return ele.substring(0,3);
    })
    .skip(2)
    .collect(Collectors.toList());

System.out.println(counter); // 3

list.stream()
    .skip(2)
    .map(ele -> {
        wasCalled();
        return ele.substring(0,3);
    })
    .collect(Collectors.toList());

System.out.println(counter); // 1
```

## 스트림의 재사용  
스트림의 종료 작업을 하지 않는 한 하나의 인스턴스로서 지속적 사용이 가능   
하지만 종료 작업을 하는 순간 스트림이 닫히기 때문에 재사용 불가  
스트림은 저장된 데이터를 꺼내서 처리하는 용도이지 데이터를 저장하려는 목적으로 설계되지 않았기 때문  

```java
Stream<String> stream = Stream.of("Eric", "Elena", "Java").filter(name -> name.contains("a"));

Optional<String> firstElement = stream.findFirst();
Optional<String> anyElement = stream.findAny(); // IllegalStateException: stream has already been operated upon or closed
```

`findFirst`은 스트림의 terminal operation이므로 이미 스트림이 닫혔기 때문에 `findAny`를 호출하는 순간 runtime exception이 발생.  
이러한 점은 Compiler가 캐치 불가 하기 때문에 주의가 필요.  

개선 코드로서 데이터를 List에 저장하고 필요할 때마다 stream을 생성
```java
List<String> names = Stream.of("Eric", "Elena", "Java")
                            .filter(name -> name.contains("a"))
                            .collect(Collectors.toList());

Optional<String> firstElement = names.stream().findFirst();
Optional<String> anyElement = name.stream().findAny();
```

## 지연 처리(Lazy Invocation)
스트림은 terminal operation이 호출되지 않으면, 스트림 연산은 실행되지 않는다.
```java
List<String> list = Arrays.asList("Eric", "Elena", "Java");
int counter = 0; // let's assume that it's a global variable in order to avoid lambda enclosing scope problem.
Stream<String> stream = list.stream()
                            .filter(ele -> {
                                counter++;
                                return ele.contains("a");
                            });
System.out.println(counter); // 0

stream.collect(Collectors.toList());
System.out.println(counter); // 3
```

## Null-safe 스트림
아래는 `collectionToStream` 메소드의 정의이다.  
인자로 받은 collection 객체를 이용해 Optional object를 만들고 스트림을 생성 후 리턴한다. 만약 collection이 비어있다면 빈 스트림을 리턴한다.
```java
public <T> Stream<T> collectionToStream(Collection<T> collection) {
    return Optional
      .ofNullable(collection)
      .map(Collection::stream)
      .orElseGet(Stream::empty);
}
```
아래의 경우처럼 null인 collection을 이용하여 stream을 생성하게 되면 NPE가 발생
```java
List<String> nullList = null;
nullList.stream()
    .filter(str -> str.contains("a"))
    .map(String::length)
    .forEach(System.out::println); // Null Pointer Exception
```
Null-safe stream을 생성하기 위해 `collectionToStream`을 이용하면 NPE를 예방가능
```java
collectionToStream(nullList)
    .filter(str -> str.contains("a"))
    .map(String::length)
    .forEach(System.out::println); // []
```

## Simplified
Stream을 사용하는데 있어, 생략하여 표현 할 수 있는 대표적 케이스 모음이다.
```java
collection.stream().forEach() 
  → collection.forEach()
  
collection.stream().toArray() 
  → collection.toArray()

Arrays.asList().stream() 
  → Arrays.stream() or Stream.of()

Collections.emptyList().stream() 
  → Stream.empty()

stream.filter().findFirst().isPresent() 
  → stream.anyMatch()

stream.collect(counting()) 
  → stream.count()

stream.collect(maxBy()) 
  → stream.max()

stream.collect(mapping()) 
  → stream.map().collect()

stream.collect(reducing()) 
  → stream.reduce()

stream.collect(summingInt()) 
  → stream.mapToInt().sum()

stream.map(x -> {...; return x;}) 
  → stream.peek(x -> ...)

!stream.anyMatch() 
  → stream.noneMatch()

!stream.anyMatch(x -> !(...)) 
  → stream.allMatch()

stream.map().anyMatch(Boolean::booleanValue) 
  → stream.anyMatch()

IntStream.range(expr1, expr2).mapToObj(x -> array[x]) 
  → Arrays.stream(array, expr1, expr2)

Collection.nCopies(count, ...) 
  → Stream.generate().limit(count)

stream.sorted(comparator).findFirst() 
  → Stream.min(comparator)
```
하지만, 특정 케이스에서 조금 다르게 동작 할 수 있어 주의가 필요
```java
// stream()을 생략
collection.stream().forEach()
  → collection.forEach()
// not synchronized
Collections.synchronizedList(...).stream().forEach()
// synchronized
Collections.synchronizedList(...).forEach()
```
```java
// collect 생략
stream.collect(maxBy()) 
  → stream.max()
```
하지만, 스트림이 비어서 값을 계산 할 수 없는 때의 동작은 다르다.
```java
collect(Collectors.maxBy()) // Optional 객체를 리턴
Stream.max() // NPE 발생 가능성이 있음
```
