# awk
- awk는 유닉스에서 처음 개발된 스크립트 언어.
- 텍스트 형태로 되어있는 데이터를 필드로 구분하여 처리하는 기능을 기본으로 한다.
- 주로 패턴 검색과 조작을 통해 레포트를 만드는 등의 작업에 사용된다.
- Read: awk는 input stream(file, pipe, or stdin)으로부터 하나의 라인을 읽고 메모리에 저장한다.
- Execute: 모든 awk 커맨드는 input에 대하여 순차적으로 적용한다. 기본적으로 awk는 모든 line에 대해 커맨드를 실행한다. 이를 pattern을 제공함으로써 제한할 수도 있다.
- Repeat: 이 과정은 파일의 끝에 다다를 때까지 반복된다.

## Syntax
awk [option] '[pattern] {action}' filename
    * BEGIN block
        - BEGIN {awk-command}
        - BEGIN block은 awk가 시작할 때 딱 한 번 실행된다. 
        - 변수의 초기화에 좋은 타이밍이다.
        - BEGIN은 awk의 keyword이기 때문에 Upper-case이여야만 한다.
        - optional syntax
    * Body block
        - /pattern/ {awk-commands}
        - body block은 awk commands를 모든 input line에 적용시킨다.
        - By default, awk는 모든 lines에 커맨드를 실행한다.
        - pattern을 제공하여 이를 제한 할 수 있다.
        - body block을 위한 keyword는 따로 없다.
    * END block
        - END {awk-commands}
        - BEGIN과 반대로 END는 awk 프로그램의 끝에 실행된다.
        - END는 keyword이기 때문에 upper-case로 쓴다.
        - optional 

## Pattern
    BEGIN     입력파일을 읽어들이기 전 제시되는 문자열을 실행
    END       awk가 모든 입력을 처리한 후 옆에 제시되는 문자열을 실행
    /문자열/   문자열과 일치하는 라인을 찾아 액션을 실행

## Built-in Varibales
    * $0
        - entire input record
    * $n
        - FS에 의해 분리된 현재의 레코드에서 n번째 필드
    * ARGV        
        - 커맨드 라인 arguments를 저장해두고 있는 array
        - Valid Range is from 0 to ARGC-1
        - awk 'BEGIN {for (i=0; i<ARGC-1; i++) {printf "ARGV[%d] = %s\n", i, ARGV[i]})' a b c
        - output:
            ARGV[0] = awk
            ARGV[1] = one
            ARGV[2] = two
            ARGV[3] = three
    * ARGC        커맨드 라인에 제공된 args의 수를 나타낸다.
        awk 'BEGIN {print "Arguments =", ARGC} a b c'
        output: 4
        `why not 3 but 4 ? ARGV[0] 값으로 무조건 awk가 들어가기 때문에`
    * CONVFMT
        - conversion format for number
        - default value is %.6g
    * ENVIRON
        - associative array of environment variables
        - env 커맨드를 통해 나타나는 환경변수들을 지정하면 해당 값을 출력
        - awk 'BEGIN { print ENVIRON["USER"]}'
    * FILENAME
        - 현재 처리되고 있는 입력 파일의 이름
        - awk 'END {print FILENAME}' marks.txt
    * FS
        - input field seperator
        - default value is space
        - -F 옵션을 통해서 필드 분리 문자를 변경할 수 있음
        - awk 'BEGIN {print "FS = " FS}' | cat -vte
    * OFS
        - FS와 기본적으로 같으나 OFS는 Output 필드에 대한 분리 문자이다.
        - default value is space
    * RS
        - input record seperator
        - default value is newline
    * NR
        - 현재 레코드(행)의 번호
        - echo -e "One Two\nOne Two Three\nOne Two Three Four" | awk 'NR < 3'
            2번째 행 까지만 출력
            output:
                One Two
                One Two Three
    * FNR
        - NR과 같지만 현재의 작업 중인 파일에 대해서만 유효범위를 갖는다.
        - 즉, NR이용하여 멀티 파일을 실행할 경우 NR의 행 번호가 계속 쌓여가지만, FNR의 경우 파일 단위로 다시 reset된다.
    * NF
        - 현재 레코드(행)의 필드의 갯수 
        - echo -e "One Two\nOne Two Three\nOne Two Three Four" | awk 'NF > 2'
            필드가 2개 이상인 경우만 출력
            output:
                One Two Three
                One Two Three Four
    * ORS
        - output record seperatior를 나타낸다
        - default value는 newline
    * RLENGTH
        - match function과 match되는 string의 length를 나타낸다.
        - AWK의 match function은 input-string으로 주어진 문자열에 대하여 검색을 실행한다.
        - awk 'BEGIN { if (match("One Two Three", "re")) { print RLENGTH } }'
          output: 2

## operator
    =   +=   -=  *=   /=   %=    배정연산자
    +   –   *   /   %   ++   —   산술연산자
    ||   &&   !                  논리연산자(OR, AND, NOT)
    >   >=   <   <=   ==   !=    비교연산자
    v ~p                         변수 v가 패턴 P에 부합되면 참
    v !~p                        변수 v가 패턴 P에 부합되지 않으면 참
## options
    * -f : awk 형식의 파일 실행 옵션
        - awk -f command.awk sample.txt
        - command.awk 파일의 내용이 {print} 라고 되어 있다면, awk는 마치 sample.txt에 대하여 기존 body block을 실행하듯 command.awk의 내용을 읽어들여 실행한다.
    * -v : awk program이 실행되기 전, value를 변수에 할당해준다.
        - awk -v name=Ko 'BEGIN{printf "Name = %s\n", name}'
        - 실행결과 Name = Ko
    * --dump-variables[=file]
        - awk --dump-variables ''
        - 정렬된 global variables를 프린트하고 그것들의 final values를 파일로 옮겨준다.
        - 파일 이름을 지정하지 않았을 경우 by default, awkvar.out의 형태로 저장된다.
    * --lint[=fatal]
        - awk --lint '' /bin/ls
        - non-portable or dubious constructs를 체크해준다.
        - argument fatal를 제공하면 warning 메시지를 띄워준다.
    * --posix
        - strict POSIX compatibility를 사용한다.
        - 모든 common 그리고 gawk-specific extentions들은 disabled된다.
    * --profile[=file]
        - awk --profile 'BEGIN{printf"---|Header|--\n"} {print} END{print"---|Footer|---\n"}' marks.txt > /dev/null
        - pretty-printed 버전의 프로그램을 파일로 생성해준다. 
        - by default, awkprof.out으로 이름이 지정된다.
    * --traditional
        - 모든 gawk-specific extentions를 disabled 시킨다.
    * --version
        - awk의 버전을 출력

## Action
    * print
    * printf
    * if (expr) statement else statement
    * while (expr) statement else statement
    * for (expr; expr; expr) statement
    * for (var in array) statement
    * break
    * continue
    * next
    * exit


## test samples
```bash
$ awk 'BEGIN{printf "date\tcompany count\ttotal user\tlogged user\n"} {print}' re
source-count_P000001.cs
    - awk는 BEGIN block을 먼저 실행하고서 body block을 stdin에 대하여 stdin의 끝에 다다를때까지 실행하게 된다.
    - 실행 결과 예시
date    company count   total user      logged user
2018/08/23,1,9,7,1001,0,1154,1,7,20867,11009,5217,10
2018/08/24,1,9,7,1002,0,1155,2,8,20884,11040,5242,20

$ date | awk '{print "day: "$1 "\nMonth : "$2}'
    데이트의 출력값중 요일과 달만 출력
    date output:Sat Aug 25 18:52:11 DST 2018
    $1 => Sat
    $2 => Aug
    result:
    day: Sat
    Month : Aug

$ cat /etc/passwd | awk -F: '$3 > 500 {print $1}'
    지정 파일을 ':' 구분자로 나누어 세번째 필드 uid가 500 이상인 경우 첫번째 필드 출력
    -F 옵션: --field-seperator=fs 구분자를 콜론(:)으로 하겠음
    '$3 > 500 {print $1}' 콜론으로 나눠진 필드에서 세번째 필드의 값이 500 보다 큰 경우에 출력하겠다

$ cat test.txt
Infected files: 3
Infected files: 0
Infected files: 5
Infected files: 1
Infected files: 0
Infected files: 1
$ awk '{sum += $3} END {printf "SUM : " sum"\n"}' ./test.txt
    test파일의 감염 파일의 총합을 출력
    세번째 필드의 값을 sum 변수에 누적 합을 하고서 sum값을 출력한다

$ find ./ -name '0*.txt' | xargs cat | awk '$1 == "Infected" {sum += $3 } END {printf "SUM : " sum"\n"}'
    복수의 여러 파일에서 한번에 합계를 구하기
    0*.txt를 찾는다.
    xargs cat: 표준입력stdIn으로부터 cat 실행
    $1 == "infected" 패턴과 일치하는 라인 찾고
    sum += $3: 세번째 필드의 값을 sum에 누적합계
    END: 모두 끝나면 최종적으로 다음 명령 실행
    printf "SUM : " sum"\n": 합계 출력

$ last | awk '$1 =="root" && $3 != "boot" {print}'
    로그인 정보 중 root가 로그인한 로그 중 부팅시 발행한 로그를 제외하고 출력
    sampele output
    root     pts/0        192.168.11.6     Tue Jan 20 09:03   still logged in
    root     tty1                          Tue Jan 20 09:02   still logged in
    root     pts/0        192.168.11.6     Tue Jan 20 01:02 - down   (00:24)
    root     tty1                          Tue Jan 20 09:02   still logged in
    root     pts/0        192.168.11.6     Tue Jan 20 01:02 - down   (00:24)

$ df -h | awk '/dev/ {print int($3/$2*100)}'
    /dev/ 패턴이 일치하는 라인의 내용을 지정한 표현식으로 출력
    /home 파티션의 사용 비율을 % 없이 정수표현 하고 싶을 때
    df -h output:
    Filesystem      Size  Used Avail Use% Mounted on
    rootfs          238G   83G  155G  35% /
    none            238G   83G  155G  35% /dev

$ 비교 표현
    $ awk '$3 > 7000{print $1, $2}' 
    세번째 컬럼의 값을 비교하고 참인 경우 컬럼1과 2만을 출력한다.

$ Counting and Printing Matched Pattern
    $ awk '/a/{++cnt} END {print "Count = ", cnt}' marks.txt
    패턴 /a/와 일치하는 라인을 찾을 때마다 cnt를 늘려 최종 카운트를 출력해줌
    결과: Count = 4

$ Printing Lines with More than 18 Characters
    $ awk 'length($0) > 18' marks.txt
    18 characters 이상을 포함한 lines를 출력
    awk는 해당 string의 길이를 return하는 built-in length function을 제공한다. $0 변수는 라인 전체를 저장한다.
    body block이 없을 때에는 default action이 취해지는데, print action이 이에 해당한다. 
    그러므로 만약 해당 라인이 18 characters 초과면, 비교 연산이 true가 되고 라인이 출력되는 것이다.
```






