Variables in Bash
===

1. Command Line Arguments
$1 $2 $3 ... $9 : bash script 실행시 넘겨 받은 arguments가 번호 순서로 지정되어 script 내에서 활용된다.  
myscript.sh가 있다고 가정하고, command line에서 다음과 같이 실행 한다면?
- $ ./myscript.sh apple pear watermellon  
myscript내에서 apple, pear, watermellon은 $1, $2, $3의 변수에 각각 저장되어 스크립트 내에서 활용할 수 있게 된다.  

2. Other Special Variables
- $0 : Bash script의 이름
- $# : 스크립트의 arguemnts의 총 개수
- $@ : 스크립트 모든 arguments의 values
- $? : 가장 최근에 실행된 run process의 exit status. 0 또는 이외의 숫자로 정상적인 종료였는지 에러였는지 등을 알 수 있다.
- $$ : 가장 최근 스크립트의 PID(Process ID)
- $USER : 스크립트를 실행하는 username
- $HOSTNAME : 스크립트를 실행하고 있는 머신의 hostname
- $SECONDS : 스크립트가 실행된 시간이 기록된 변수
- $RANDOM : 참조 될때마다 랜덤 숫자를 리턴
- $LINENO : 스크립트의 현재 라인을 리턴

3. Quotes
- "Bash uses a space to determine seperate items."  
Bash는 스페이스를 delimeter로 사용하기 때문에 하나의 변수에 single word가 아닌 좀 더 복잡한 값을 저장하기 위해서는 Quotes로 감싸야 한다.
- "Remember, commands work exactly the same on the command line as they do within a script."  
commands의 동작은 command line과 script내에서도 동일  
- Single quotes will treat every character literally  
- Double quotes will allow you to do substitution (that is include variables within the setting of the value.)

4. Command Substitution
Command subsutitution은 커맨드의 ouput을 다시 또 다른 변수의 값으로 저장할 수 있도록 해준다.  
사용법은 $로 시작하는 bracket으로 감싸주면 된다.  
- var=$( ls ./ | grep tomcat )  
만약 커맨드의 ouput이 goes over several lines 이라면, 라인 변환은 지워지고 모두 single line으로 모여서 출력된다.

5. Exporting Variables
다음의 키워드를 이용한다. **export**
- export  
example
- script1.sh
```Bash
#!/bin/bash
# demonstrate variable scope 1.
var1=blah
var2=foo
# Let's verify their current value
echo $0 :: var1 : $var1, var2 : $var2
export var1
./script2.sh
# Let's see what they are now
echo $0 :: var1 : $var1, var2 : $var2
```
- script2.sh
```Bash
#!/bin/bash
# demonstrate variable scope 2
# Let's verify their current value
echo $0 :: var1 : $var1, var2 : $var2
# Let's change their values
var1=flop
var2=bleh
# Let's verify their current value
echo $0 :: var1 : $var1, var2 : $var2
```
- 다음은 script1.sh 실행의 output이다
```
$ ./script1.sh
./script1.sh
./script1.sh :: var1 : blah, var2 : foo
./script2.sh :: var1 : blah, var2 :
./script2.sh :: var1 : flop, var2 : bleh
./script1.sh :: var1 : blah, var2 : foo
```
What actually happens when export a variable, we are telling Bash that every time a new process is created (to run another script or such) then make a copy of the variable and hand it over to the new process. _SO ALTHOUGH THE VARIABLES WILL HAVE THE SAME NAME THEY EXIST IN SEPERATE PROCESS AND SO ARE UNRELATED TO EACH OTHER._  

Exporting variables is a one way process. The original process may pass variables over to the new process but anything that process does with the copy of the variables has no impact on the original variables.  

