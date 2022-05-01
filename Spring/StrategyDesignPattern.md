# 전략 패턴

## 변하는 것과 변하지 않는 것의 분리
전편: [변하는 것과 변하지 않는 것의 분리 - 템플릿 메서드 패턴](./TemplateMethodPatern)   

변하는 것(핵심기능)과 변하지 않는 것(부가기능)의 분리로서,  
`템플릿 메서드 패턴`은 부모 클래스에 변하지 않는 템플릿을 두고,  
변하는 부분을 자식 클래스에 두어서 `상속`을 사용해 문제를 해결한다.

그러나 `상속`에 의한 단점들의 보완으로 `전략 패턴`을 고려해 볼 수 있다.
> 전략 패턴의 의도  
"알고리즘 제품군을 정의하고 각각을 캡슐화하여 상호 교환 가능하게 만든다. 전략을 사용하면 알고리즘을 사용하는 클라이언트와 독립적으로 알고리즘을 변경할 수 있다." - GoF

### 위임 디자인
전략 패턴은 변하지 않는 부분을 `Context`라는 곳에 두고, 변하는 부분을 `Strategy`라는 인터페이스를 만들어 해당 인터페이스를 구현하도록 하여 문제를 해결.    
`상속`이 아닌 `위임`으로 문제를 해결하는 것.    
전략패턴에서 `Context`는 변하지 않는 템플릿 역할을 하고, `Strategy`는 변하는 알고리즘 역할을 한다. Context(문맥)는 크게 변하지 않고, 그 문맥 속에서 Strategy를 통해 일부 전략이 변경되는 것. 
 
- Context 내부에 Strategy 필드를 갖고, 이 필드에 변하는 부분인 Strategy의 구현체를 주입. 
    - 전략패턴의 핵심은 Context는 Strategy 인터페이스에만 의존한다는 점. 덕분에 Strategy의 구현체를 변경하거나 새로 만들어도 Context 코드에는 영향을 주지 않는다.
    - **스프링으로 애플리케이션을 개발할 때 애플리케이션 로딩 시점에 의존관계 주입을 통해 필요한 의존관계를 모두 맺어두고 난 다음에 실제 요청을 처리하는 것과 같은 원리이다.**

### 단점
Context와 Strategy를 조립한 이후에는 전략을 변경하기가 번거롭다는 점.  
물론 Context에 setter를 제공하여 Strategy를 넘겨받아 변경하면 되지만, Context를 싱글톤으로 사용할 때는 동시성 이슈 등 고려할 점이 많다.  
때문에 차라리 Context를 하나 더 생성하고 그곳에 다른 Strategy를 주입할 수도 있겠다.

### 대안
그래서 전략을 실시간으로 변경해야 한다면,  
Context 내부에 Strategy 필드만으로서가 아닌 핵심 기능 함수에 파라미터로서 전달할 수도 있다.
    - 이럴 경우, 매 실행마다 전략을 넘겨주어야 하는 단점이 있지만, 전략을 자유롭게 바꿔가며 실행이 가능하다.
    - 이를 스프링에서는 `템플릿 콜백 패턴(Template Callback Pattern)`이라고 불리며, 스프링 사용중에 흔히 만나는 RedisTemplate, JdbcTemplate, etc이 템플릿 콜백 패턴을 따른다고 볼 수 있다.