eval
===

 - 변수 치환의 기회가 한 번 더 필요 할 때 사용

```bash
set b=$a
set a=foo
echo $a #a
```
변수 치환은 한 번 일어난다. 재귀적으로 발생하지 않는다.

```bash
eval echo $b # foo
```
eval 명령어는 이 라인을 다시 한 번 더 해석하고 실행하라는 의미이다. eval 명령어를 사용하면 shell은 명령행 해석을 다시 한 번 수행하기 때문에 $b -> $a -> foo가 되는 것이다.  

__indirect expansion__ 과 비슷한 느낌? 이지만 약간의 exceptions가 있는 듯 하다.
```bash
echo ${!b} 
```