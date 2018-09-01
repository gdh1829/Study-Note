awk and sed
===========================

awk는 유닉스에서 처음 개발된 스크립트 언어.
텍스트 형태로 되어있는 데이터를 필드로 구분하여 처리하는 기능을 기본으로 한다.
주로 패턴 검색과 조작을 통해 레포트를 만드는 등의 작업에 사용된다.

* Syntax
awk [option] '[pattern] {action}' filename

* Pattern
    BEGIN     입력파일을 읽어들이기 전 제시되는 문자열을 실행
    END       awk가 모든 입력을 처리한 후 옆에 제시되는 문자열을 실행
    /문자열/   문자열과 일치하는 라인을 찾아 액션을 실행

* operator
=   +=   -=  *=   /=   %=    배정연산자
+   –   *   /   %   ++   —   산술연산자
||   &&   !                  논리연산자(OR, AND, NOT)
>   >=   <   <=   ==   !=    비교연산자
v ~p                         변수 v가 패턴 P에 부합되면 참
v !~p                        변수 v가 패턴 P에 부합되지 않으면 참

* Action
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

* Variables already assigned
    * 변수        내용
    * FILENAME    현재 처리되고 있는 입력 파일의 이름
    * FS          입력 필드 분리문자
    * NR          현재 레코드(행)의 번호
    * NF          현재 레코드(행)의 필드의 갯수
    * OFS         출력되는 필드의 분리문자

* test samples

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

$ df -h | awk '/dev/ {print int($3/$2*100)}'
    /home 파티션의 사용 비율을 % 없이 정수표현 하고 싶을 때
    df -h output:
    Filesystem      Size  Used Avail Use% Mounted on
    rootfs          238G   83G  155G  35% /
    none            238G   83G  155G  35% /dev






