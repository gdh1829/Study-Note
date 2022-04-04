# BeanPostProcessor - 빈후처리기

빈후처리기는 빈을 조작/변경할 수 있는 Hooking 포인트.
빈 객체를 조작하거나 심지어 다른 객체로 바꿔 버릴 수 있을 정도로 강력.
여기서 조작이라는 의미는 해당 객체의 특정 메서드를 호출하는 것을 뜻함.
일반적으로 스프링 컨테이너가 등록하는, 특히 컴포넌트 스캔의 대상이 되는 빈들은 중간에 조작할 방법이 없는데, 빈 후처리기를 사용하면 개발자가 등록하는 모든 빈을 중간에 조작 가능. 이 말은 **빈 객체를 프록시로 교체**하는 것도 가능하다는 의미.

스프링이 제공하는 인터페이스
```java
public interface BeanPostProcessor {
    Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException;
    Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException;
}
```

BeanPostProcessor를 구현하고 스프링 빈으로 등록하면 스프링 컨테이너가 빈 후처리기로 인식하여 동작.
일반적인 Bean 클래스보다 우선적으로 스프링 컨테이너에 등록된다.

만약 빈후처리기의 역할이 postProcessAfterInitialization에서 빈을 바꿔치기(A -> ProxyA)하는 기능이라면, A라는 빈이 initialization이 되어 스프링에 등록될때, ProxyA라는 클래스로 맵핑하여 스프링 컨테이너에 등록하게 된다.
고로, Bean A는 스프링 컨테이너에 등록조차 되지 않는다. A 빈을 조회시 ProxyA 빈이 반환됨.


## @PostConstruct, @PreDestory
@PostConstruct는 스프링 빈 생성 이후에 빈을 초기화 하는 역할을 한다.
생성된 빈을 한 번 조작하는 것.

스프링은 CommonAnnotationBeanPostProcessor라는 빈후처리리기를 자동 등록함. 여기에서 @PostConstruct 어노테이션이 붙은 메소드를 호출한다.
따라서 스프링 스스로도 내부의 기능을 확장하기 위해 빈 후처리기를 사용.

```java
public class CommonAnnotationBeanPostProcessor extends InitDestroyAnnotationBeanPostProcessor implements InstantiationAwareBeanPostProcessor, BeanFactoryAware, Serializable {

    //...

    public CommonAnnotationBeanPostProcessor() {
        this.setOrder(2147483644);
        this.setInitAnnotationType(PostConstruct.class);
        this.setDestroyAnnotationType(PreDestroy.class);
        this.ignoreResourceType("javax.xml.ws.WebServiceContext");
    }

    //...
```


org.springframework.boot:spring-boot-starter-aop lib 추가
lib를 추가하면, `aspectjweaver`라는 `aspectJ`관련 라이브러리를 등록하고, 스프링부트가 AOP 관련 클래스를 자동으로 스프링 빈에 등록. 스프링부트가 없던 시절에는 @EnableAspectJAutoProxy를 직접 사용해야 했는데, 이 부분을 스프링부트가 자동 처리. 스프링부트가 활성화 하는 빈은 `AopAutoConfiguration`을 참조.

AutoProxyCreator 자동 프록시 생성기
aop 라이브러리를 추가함으로써 스프링 부트 자동설정으로 `AnnotationAwareAspectJAutoproxyCreator`라는 빈 후처리기가 스프링 빈에 자동 등록됨.
이 빈 후처리기는 스프링 빈으로 등록된 `Advisor`들을 자동으로 찾아서 프록시가 필요한 곳에 자동으로 프록시를 적용해줌. Advisor 안에는 Pointcut과 Advice가 이미 포함되어 있으므로, Advisor만 알고 있으면 그 안에 있는 Pointcut으로 어떤 스프링 빈에 프록시를 적용해야 할지 알 수 있음. 그리고 Advice를 부가기능으로 적용하면 끝.

`AnnotationAwareAspectJAutoproxyCreator`는 @AspectJ와 관련된 AOP 기능도 자동으로 찾아서 처리해줌.
Advisor는 물론이고, @Aspect도 자동으로 읺식해서 프록시를 만들고 AOP를 적용해준다. 

## 포인트컷은 2가지에 사용된다.
1. 프록시 적용 여부 판단 - 생성 단계
    - 스프링 빈 후처리기가 모든 어드바이저 빈을 조회하여 포인트 컷을 기준 삼아 해당 스프링 빈 클래스의 클래스 + 모든 메서드와 포인트컷 조건에 하나하나 매칭 비교하여 프록시 적용 대상 체크. 하나라도 해당한다면 하나라도 해당시 프록시 생성 등록. 그렇지 않으면, 당연히 프록시가 굳이 필요없으므로 프록시 생성 X.
2. 어드비이스 적용 여부 판단 - 사용 단계
    - 프록시가 호출되었을 때, 부가 기능인 어드바이스를 적용할지 말지 포인트컷을 보고 판단

프록시를 모든 곳에 생성하는 것은 비용 낭비. 꼭 필요한 곳에 최소한의 프록시를 적용해야 함. 그래서 자동 프록시 생성기는 모든 스프링 빈에 프록시를 적용하는 것이 아니라 포인트컷으로 한번 필터링해서 어드바이스가 사용될 가능성이 있는 곳에만 프록시를 생성.