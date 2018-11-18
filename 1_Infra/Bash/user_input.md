User Input
===

## Ask the User for Input: **read** command
- simle read
```bash
#!/bin/bash
echo -n 'username: ' # echo -n option은 echo의 줄바꿈을 없애준다.
read username
echo $username
# 위의 코드를 아래와 같이 read의 -p옵션을 이용해 prompt를 echo처럼 띄울 수 있다.
read -p 'username: ' username
echo $username
# -s 옵션을 추가하면 비밀번호와 같은 입력에 대하여 보이지 않게 해준다. input scilent
read -sp 'password: ' password
```
- multiple read
whitespace를 기준으로 여러 입력을 한 번에 받을 수 있다. 
Number of user input > number of variable to read => 여분이 남는 user input은 모두 마지막 변수에 함께 할당 된다.
Number of user input < number of variable to read => 여분이 남는 variable은 blank or null
```bash
#!/bin/bash
echo -n 'What colors do you like? ' #user input: red yellow green blue
read color1 color2 color3
echo $color1 # red
echo $color2 # yellow
echo $color3 # green blue
```

## Reading from STDIN
Bash accomodates piping and redirection by way of special files. Each process gets it's own set of files (one for STDIN, STDOUT and STDERR respectively) and they are linked when piping or redirection is invoked. Each process gets the following files:  
* STDIN - /proc/<processID>/fd/0
* STDOUT - /proc/<processID>/fd/1
* STDERR - /proc/<processID>/fd/2  

To make life more convenient the system creates some shortcuts for us:  
* STDIN - /dev/stdin or /proc/self/fd/0
* STDOUT - /dev/stdout or /proc/self/fd/1
* STDERR - /dev/stderr or /proc/self/fd/2  
**fd** in the paths above stands for file descriptor.  

다음과 같은 파일이 있다고 가정해보자.  
$ cat sample.txt  
Fred apples 20 November 4  
Susy oranges 5 November 7  
Mark watermelons 12 November 10  
Terry peaches 7 November 15  
다음과 같은 test.sh 스크립트가 있다.  
```bash
#!/bin/bash
echo Here is a summary of the sales data:
cat /dev/stdin | cut -d' ' -f 2,3 | sort
```
다음과 같이 실행해 보았다.  
$ cat sample.txt | ./test.sh  
[cat sampel.txt]를 실행하여 cat의 stdout이 pipeline을 통하여 다음 커맨드를 위한 linux /dev/stdin에 redirect되고, test.sh를 실행하며 [cat /dev/stdin | cut -d' ' -f 2,3 | sort]에서 다시 그 /dev/stdin의 내용을 읽어 cut과 sort를 진행하게 되는 것이다.  

## So which should I use?
세 가지 방법이 있겠다.  
- Command line arguments
- Read input during script execution
- Accept data that has been redirected into the Bash script via STDIN

Command line arguments의 경우 사용하기 가장 편리한 방법이며 history에도 저장되며 쉽게 가져올 수 있겠다. 하지만 id나 password같은 credentials의 경우 history에 남아버리기 때문에 security문제가 있는데, 이럴 경우엔 script가 실행되는 동안 read input이 좋은 예가 될 수 있다. 기타 등등, 상황에 맞게 사용해야 하는데, 다음의 세 가지를 고려해야 할 것이다.  

- **Ease of user** - which of these methods will make it easiest for users to use my script?
- **Security** - Is there sensitive data which I should handle appropriately?
- **Robustness** - Can I make it so that my scripts operation is intuitive and flexible and also make it harder to make simple mistakes?

