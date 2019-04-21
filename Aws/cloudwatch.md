CloudWatch
===

## CloudWatch Custom Metric
`Custom Metric`: CloudWatch가 기본적으로 제공하는 측정치 이외에 사용자가 측정한 값을 사용하도록 하는 것.  
서버 애플리케이션, 로그 파일, 언어 레벨에서 측정치를 생성하고, 이 값들을 모니터링하거나 CloudWatch 액션을 제어하고 싶을 때 사용  

## Pre-requirement
- Instance 내부에서 aws cli를 사용하기 위해, Access Key와 Private Key를 설정  
>    $ `aws configure`  
    AWS Access Key ID [None]: xxxxxxxxxxxxxxxx  
    AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
    Default region name [None]: ap-northeast-1  
    Default output format [None]:  
- Instance로부터 아래와 같은 aws cloudwatch 명령어를 실행
>$ `aws cloudwatch put-metric-data --namespace "Hello" --metric-name "World" --value 10`  
아래와 같이 새로운 Custom Namespaces에 설정 내용이 등장하게 된다.
![AWS Services](./images/cloudwatch_custom_metric1.png)
![AWS Services](./images/cloudwatch_custom_metric2 .png)
- 실무에서는 위와 같은 Manual 방법이 아닌 각 OS의 cron/scheduler 또는 Node.js의 child_process.exec.를 사용하여 5분 혹은 1분 단위로 위와 같은 cloudwatch 명령을 실행하는 방법이 될 것