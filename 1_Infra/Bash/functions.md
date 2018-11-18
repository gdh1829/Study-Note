Functions
===

## How to define functions  
괄호가 있고 없고에 어떠한 차이도 없다. 현장에 맞는 coding convention을 따르면 된다. 또한 function 선언 키워드도 optional이다.
```bash
function_name () {
    <commands>
}
```
or
```bash
function function_name {
    <commands>
}
```
## Passing Arguments
일반적인 다른 언어에서는 함수의 definition에서 괄호 안에 arguments를 정의 하지만, Bash의 경우 arguments 정의는 따로 없다.  
CLI에서 script를 실행할 때와 마찬가지로, 해당 function을 call할 때, white space로 구분해가며 arguments를 입력하여 전달한다.  
전달된 arguments는 해당 function 안에서 $1, $2 ... $n으로 할당된다.

## Return Values
일반적인 다른 언어와 달리 Bash는 function에 대한 concept of a return value for functions이 허락되지 않는다.  
하지만 status는 확인이 가능하다. **$?**, 이를 통해 해당 함수가 성공적으로 exit이 되었는지를 확인 가능하다.  
$?를 출력해보면 0이 출력된다.  
이는 $?가 갖고 있는 특성으로 $?는 직전에 실행된 command에 대하여 exit 상태 코드를 갖고 있으며 Typically a return status of 0 indicates that everything went successfully. A non zero value indicates an error occurred.
```bash
#!/bin/bash
# Setting a return status for a function
print_something () {
    echo Hello $1
}
print_something Mars
print_something Jupiter
# Remember that the variable $? contains the return status of the previously run command or function.
echo The previous function has a return value of $? # returns 0, which means that the previous command has succeeded in exit.
```
함수에 대하여 직접적으로 **return** 키워드를 사용하여 return status를 지시할 수 있다.
단, **숫자만** 가능하다. return status를 위한 return keyword이기 때문에 당연히 숫자 이외의 타입은 return이 불가능하다.
```bash
#!/bin/bash
# Setting a return status for a function
print_something () {
    echo Hello $1
    return 5
}
print_something Mars
print_something Jupiter
# Remember that the variable $? contains the return status of the previously run command or function.
echo The previous function has a return value of $? # returns 5
```
return keyword를 통하여 숫자를 output할 수 있기 때문에, 본래의 exit status 확인 용도가 아닌, 예를 들어, 계산의 결과 같은 숫자형 데이터의 return에도 활용이 가능하다.  
**One way to get around this it to use _Command Substituition_ and have the function print the result(and only the result).**
```bash
#!/bin/bash
# Setting a return value to a function
lines_in_file () {
    cat $1 | wc -l
}
# We use command substitution to take what would normally be printed to the screen and assign it to the variable num_lines
num_lines=$( lines_in_file $1 )
echo The file $1 has $num_lines lines in it.
```
Just be wary if you take this approach as if you don't call the function with command substitution then it will print the result to the screen. Sometimes that is ok because that is what you want. Other times that may be undesireable.  

## Variable Scope
Scope는 스크립트의 어느 부분이 어떤 변수를 볼 수 있는지를 나타내는데, 디폴트 설정으로 모든 변수는 global이다.  
물론, **local** keyword를 통해서 함수 내에서 지역 변수를 만들 수 있다.  
함수 내에서 global var와 같은 이름의 local var가 있다면, local var을 기준으로 사용되며, 서로 영향을 주지 않는다. 함수가 끝나고 다시 바깥에서 해당 global var은 이전의 값 그대로이다.
지역 변수를 만드는 것은 메모리 관리에도 좋고, 기다란 스크립트에서 중복된 변수 명으로 인하여 의도치 않은 값 변환의 위험도 줄일 수 있어 좋다.  
즉, Always use local variables within functions. Use global variables as a last resort and consider if there is a better way to do it before using them.
```bash
#!/bin/bash
# Experimenting with variable scope
var_change () {
    local var1='local 1'
    echo Inside function: var1 is $var1 : var2 is $var2 # Inside function: var1 is local 1 : var2 is global 2
    var1='changed again'
    var2='2 changed again'
}
var1='global 1'
var2='global 2'
echo Before function call: var1 is $var1 : var2 is $var2 # Before function call: var1 is global 1 : var2 is global 2
var_change
echo After function call: var1 is $var1 : var2 is $var2 # After function call: var1 is global 1 : var2 is 2 changed again
```

## Overriding Commands (Wrapper)
기존의 커맨드를 다시 같은 이름의 함수(wrapper)를 만듦으로써 흔히 사용하는 커맨드의 옵션을 매번 지정해야 하는 번거로운 작업을 줄일 수도 있다.  
단, 주의점으로 **command** keyword를 반드시 사용해야 한다. 그렇지 않으면 endless loop가 진행되어 버린다. 
```bash
#!/bin/bash
# Create a wrapper around the command ls
ls () {
    # When we have a function with the same name as a command we need to put the keyword command in front of the the name when we want the command as opposed to the function as the function normally takes precedence.
    command ls -lh
}
ls
```

## Design
함수를 만드는 것은 반복을 줄이고 maintenance의 cost를 줄인다. 때때로, 짧게 적은 함수가 나을 수도 또는 길더라도 좀 더 명확하다면 더 나은 코드일 수도 있다. 개발이란 혼자하는 것이 아니기에. 가장 재사용성이 높은 함수는 하나의 함수가 하나의 task만을 수행할 때이다. 커다란 함수를 갖기보다는, 여러 부분으로 나눠 재사용이 뛰어나도록 만들어보자. 물론, 너무 많이 나누다 보면 코드가 너무 길어지기도 바보 같아질 수 도 있으나 이러한 경험과 함께 적절한 sweet spot을 찾을 수 있기를.
