CloudWatch
===
CloudWatch has available Amazon EC2 Metrics for you to use for mornitoring.

## Default Metric
- CPU Utilization
    - identifies the processing power required to run an application upon a selected instance.
- Network Utilization
    - identifies the volume of incoming and outgoing network traffic to a single instance.
- Disk Reads
    - is used to determine the volume of the data the application reads from the hard disk of the instance. 
    - This can be used to determine the speed of the applcation.  

※ However, there are certain metrics that are note readily available in Cloudwatch such as memory utilization, disk space utilization, and many others which can be collected by setting up a custom metric.

## Custom Metric
- To make custom metric available, you need to prepare a custom metric using __CloudWatch Mornitoring Scripts__ which is written in Perl. You can also install __CloudWatch Agent__ to collect more system-level metrics from Amazon EC2 instances.
- List of custom metrics that you can set up
    - Memory Utilization
    - Disk swap utilization
    - Disk space utilization
    - Page file utilization
    - Log collection

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