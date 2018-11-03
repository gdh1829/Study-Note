jq
===

JSON 포맷 데이터를 다루는 커맨드라인 유틸  
C언어로 작성된 프로젝트  


## JSON 데이터 입력
jq는 입력을 처리하는 기능을 갖고 있다.  
입력을 어떻게 처리할지에 대한 정보를 첫번째 인자로 받는다.
점(.)은 동일값(Identity)필터이다. 입력받은 내용을 그대로 출력하라는 의미
>jq '.'  
>{"foo":"bar"}  
<{  
<  "foo": "bar"  
<}  
입력 받은 내용을 그대로 출력하는 것은 아니고 JSON 구조를 파싱해서 저장한 다음 다시 출력하는 방식이기 때문에 원래의 입력이 복원되지는 않는다.  
json 파일포맷으로도 받을 수 있다.  
>jq '.' filename.json  
★pipe 연산자로 다른 프로세스의 출력을 넘겨받아 jq의 입력으로 보내는 방법★  
>echo '{"foo":"bar"}' | jq '.'  
특히 이 방법은 웹API에서 반환받은 JSON데이터를 별도의 과정을 거치지 않고 곧바로 처리가 가능.  
>curl -s 'https://api.github.com/users/octocat' | jq '.'  

## 동일값(Identity) 필터를 사용한 JSON 정형화
코드의 정형화를 Pretty Print라고 부르기도 한다.  
JSON은 스펙상 문자열 사이에 공백 문자나 개행이 들어갈 수 있다. 따라서 의미가 완벽히 같은 서로 다른 JSON 문서가 존재할 수 있다.  
예를 들어, {"foo":"bar"}와 {  "foo"  :  "bar"  }는 완전히 같은 의미를 가진 서로 다른 JSON문서이다.  
jq는 이를 사람이 보기 좋게 정형화하고 의미가 같다면 같은 구조로 출력해 준다.  
정형화를 위해 동일값 필터(.)를 사용할 수 있다.
>$ echo '{"foo" : "bar"}' | jq '.'  
```Bash
{
  "foo": "bar"
}
```

>$ echo '{    "foo"    : "bar"  }' | jq '.'  
```Bash
{
  "foo": "bar"
}
```
둘은 같은 output을 보여주고 있다.  
기계적으로는 이러한 차이에 특별한 의미가 있진 않지만 필요한 이유는 사용자가 직접 데이터를 읽기 위해서이다.  

## 오브젝트 속성 필터 Object Identifier-Index
오브젝트의 특정한 속성을 가져오려면 점(.) 뒤에 이름을 붙여준다.  
> echo '{"foo": "bar", "hoge": "piyo"}' | jq '.foo'  
output: "bar"  

속성 이름에 기호가 포함되어 있는 경우  
> echo '{"foo<": "bar", "hoge": "piyo"}' | jq '.foo<'  
이전의 방식 그대로 사용하면 에러  
```Bash
jq: error: syntax error, unexpected $end (Unix shell quoting issues?) at <top-level>, line 1:
.foo<
jq: 1 compile error
```

사실 위의 문법은 __.["속성 이름"]__ 의 축약 버전이기에, 본래의 문법을 적용하여 사용하면 문제 없이 동작
> echo '{"foo<": "bar", "hoge": "piyo"}' | jq '.["foo<"]'  
output: "bar"  

## Piple line in jq
>echo '"foobar"' | jq '.|.'

