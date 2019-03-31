Lambda
===

##Enclosing scope
Local variable defined in an enclosing scope must be final or effectively final  
람다식 구현부 안에서 사용한 변수는 수정할 수 없다는 제약.  
즉, final 변수로 취급되며 가독성을 위해 final로 명시적으로 작성하는 편이 좋다.
```java
List<String> list = Arrays.asList("Eric", "Elena", "Java");
int counter = 0; // 가독성을 위해 명시적으로 final을 넣어주자. final int counter = 0;
Stream<String> stream = list.stream()
                            .filter(ele -> {
                                counter++; // compile error: Local variable defined in an enclosing scope must be final or effectively final
                                System.out.println("filter was called.");
                                return ele.contains("a");
                            });
```
때문에, 로컬 변수가 아닌 전역 변수라면 사용이 가능하다.
```java
private int counter;

public void test() {
    List<String> list = Arrays.asList("Eric", "Elena", "Java");
    Stream<String> stream = list.stream()
                                .filter(ele -> {
                                    counter++;
                                    System.out.println("filter was called.");
                                    return ele.contains("a");
                                });
}
```