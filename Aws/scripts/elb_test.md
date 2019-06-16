시나리오

1. Opsgenie로부터 타겟그룹 unhealthy 알람이 온다

2. 타겟그룹의 instance health 상태 조희
    describe-target-health
    --target-group-arn <value>
    [--targets <value>]
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]

3. jq를 통해서 unhealthy 인스턴스의 instance id 뽑아내기

4. 타겟그룹으로부터 unhealthy 인스턴스 remove
    deregister-instances-from-load-balancer
    --load-balancer-name <value>
    --instances <value>
    [--cli-input-json <value>]
    [--generate-cli-skeleton <value>]

5. 해당 인스턴스로 접속

6. 오늘 날짜의 catalina 조회 및 에러 내용 확인

7. 재기동을 진행 할 것인지 질의 y/n

8. yes -> access log tail -f 하여 1분이상 log가 추가되지 않는지 확인

9 tomcat 재기동 실행

10. jmex 재기동

11 catalina 로그 확인

12 jmex 파일 사이즈 및 내용 확인

13 해당 인스턴스가 ELB TG로부터 완전히 제거 되었는지 재차 확인 

14 제거 되어 있다면 재기동된 해당 인스턴스를 다시 TG에 Register

15 ELB TG를 조회하여 initial 상태 확인

완료