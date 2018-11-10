#!/bin/bash

app=("grep" "awk" "cut" "tr" "sed") #배열 선언
echo ${app[3]} #output: tr
echo ${app[@]} #output all of elements: "grep" "awk" "cut" "tr" "sed"
echo ${app[*]} #same output as ${app[@]}: "grep" "awk" "cut" "tr" "sed"
echo "${#app[@]}" #output size of the array
echo ${#app[*]} #위와 같음

echo {3..0} #output: 3 2 1 0
echo {3..7} #output: 3 4 5 6 7

echo $$ #쉘의 프로세스 번호
echo $0 #쉘스크립트 이름
# $1 ~ $9 쉘 실행 input parameters
echo $* # $*: 모든 input parameter list
echo $# # input params 개수
# $() 실행의 결과를 변수화

#비교
# 문자끼리 또는 문자와 패턴 비교는 == !== -z -n 
# 숫자 비교는 -eq -ne -lt -le -gt -ge

#논리 연산
조건1 -a 조건2 #AND
조건1 -o 조건2 #OR
조건1 && 조건2 #양쪽 조건이 모두 참이면 참
조건1 || 조건2 #한쪽만 참이라도 참
!조건 #조건이 성립하지 않으면 참
true
false

#파일 검사
#-e 파일명: 파일이 존재하면 참
#-d 파일명: 디렉토리면 참
#-h 파일명: 심볼릭 링크면 참
#-f 파일명: 일반 파일이면 참
#-r 파일명: 읽기 가능한 권한이면 참
#-w 파일명: 쓰기 가능이면 참
#-x 파일명: 실행 가능이면 참
#-s 파일명: 파일 크기가 0이 아니면 참
#-u 파일명: 파일이 set-user-id가 설정되면 참

종료상태
쉘에서는 이전 실행한 명령이 성공하였는지를 ? 변수에 저장한다. 때문에 $?가 0인 경우는 성공 그렇지 않으면 비정상 종료를 의미

Tip
조건문의 [ ]는 좌ㅏ우로 공백이 있어야 한다.
[]에서 &&, || <, > 연산자들이 에러가 나는 경우 [[]]를 사용하면 OK

$RANDOM
bash 내장형 함수로서 0에서 32767 사이의 임의의 숫자를 생성
echo $RANDOM
