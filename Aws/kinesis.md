Kinesis
===

## AWS Says, "Fully managed streaming data service".  
Easily collect, process, and analyze video and data streams in real time, so you can get timely insights and react quickly to new information.  

![Kinesis](./images/kinesis.png)
위의 그림은, 다양한 소스에서 데이터가 Kinesis 스트림에 추가되고, 스트림 데이터가 다양한 Kinesis 애플리케이션에서 사용된다. 한 애플리케이션(노랑)이 스트리밍 데이터에 대해 실시간 대시보드를 실행하고 있음. 다른 애플리케이션(빨강)에서는 간단한 집계를 수행하고 처리한 데이터를 S3로 내보내고 있음. S3데이터는 추가적인 처리 과정을 거친 후 복잡한 분석을 위해 Redshift에 저장됨. 세번째 애플리케이션(초록)은 S3로 원시 데이터를 내보내는데, 이 데이터는 좀 더 저럼한 장기 저장을 위해 Glacier에 보관. 이러한 세가지 유형의 데이터 처리 파이프 라인은 모두 동시에 병렬로 발생.  

여러 배치의 경우 실시간 보다는 30분, 1시간, 1일 등의 정해진 간격으로만 배치 작업을 하기 때문에 데이터 속도보다 빠르지 못하거나 데이터 분석을 할 수 없는 경우가 많아 만약 분석을 했다하더라도 이미 과거의 정보일 뿐. 그렇기 때문에 Kinesis는 스트리밍이고 그 스트리밍을 완전관리형으로 만든 것.  

즉, __Kinesis를 사용하면 모든 데이터가 수집된 후에야 처리를 시작할 수 있는 것(Batch와 같은)이 아니라 데이터가 수신되는 대로 처리 및 분석하여 즉시 대응이 가능__  

## What can I do with Amazon Kinesis Data Streams?
- Accelerated log and data feed intake
- Real-time metrics and reporting
- Real-time data analytics
- Complex stream processing:
    - You can create Directed Acyclic Graphs (DAGs) of Amazon Kinesis Applications and data streams.
    - In this scenario, one or more Amazon Kinesis Applications can add data to another Amazon Kinesis data stream for further processing, enabling successive stages of stream processing.  
![dag](./images/dag.png)
> Directed Acyclic Graphs (DAGs): 직역하면 '방향성 비 사이클' 그래프이며 방향을 가지되, 루프를 생성하지 않는 그래프를 말한다. 여기서 루프, 또는 사이클이란 자기 자신에서 출발해서 다시 자신에게 도아오는 경로를 말하며 비 사이클이므로 이러한 경로가 없어야 한다. DAG는 중요한 용도를 가지는데, 일반적으로 작업의 우선 순위를 표현할 때 DAG의 구조를 가지게 된다. 예를 들어, 집을 지을 때 기초 공사나 기둥 세우기, 인테리어 등을 해야한다. 이때, 기둥을 세우기 전에 인테리어를 할 수 없듯이 다른 것보다 선행되어야 하는 것들을 표현하기 위해 DAG가 유용하게 사용된다. 만약 이러한 우선 순위를 표현한 그래프에서 사이클이 존재한다면 해당 작업은 영원히 끝나지 않는다. DAG에서는 우선순위를 표현하기 위해 **위상 정렬**을 사용한다. 위상 정렬이란, 작업을 실제로 한번에 하나씩 순서대로 처리한다면 어떤 순서로 작업해야 하느냐를 표현한 것이다. 이러한 위상 정렬을 위해 조건이 있는데, 노드의 순서가 왼쪽에서 오른쪽 방향으로 향해야한다. 역방향 노드가 있다면 올바른 작업 순서가 될 수 없다. 위상 정렬은 시작값에 따라 여러 가지로 표현될 수 있고 결론적으로 답이 하나로 유효하지 않다.


## What can you build with Amazon Kinesis?  
![kinesis analytics](./images/kinesis_analytics.png)
- Evolve from batch to real-time analytics  
    -> Perform real-time data analytics on data that has been traditionally analyzed using batch processing in data warehouse or using Hadoop frameworks.  

![kinesis application](./images/kinesis_application.png)  
- Build real-time application  
    -> Create visibility into what your customers, applications, and products are doing right now by building real-time applications for application monitoring, fraud detection, and live leader-boards.  

![kinesis IoT](./images/kinesis_IoT.png)  
- Analyze IoT device data  
    -> Processing streaming data from consumer applications, embedded sensors, TV set-top boxes, and other IoT devices. Send real-time alerts or perform other actions programmatically based on data.  

## Benefits & Features
- Real-time  
    -> Ingest, buffer and process data instantly, so you derive insights in seconds or minutes instead of hours or days.  
- Fully managed  
    -> Run all your streaming applications without having to deploy and maintain costly infrastructure  
- Scalable  
    -> Handle any amount of streaming data, and process it from hundreds of thousands of sources with low latency  

## Kinesis Services  
- Kinesis Data Firehose  
    -> fully managed service for delivering real-time streaming data to destinations such as S3, Redshift, ES, and Splunk  
    -> You don't need to write applications or manage resources.  
    -> You configure your data producers to send data to Kinesis Data Firehose, and it automatically delivers the data to the destination that you specified.  
    -> __You can also configure Kinesis Data Firehose to transform your data before delivering it.__  
- Kinesis Data Streams  
- Kinesis Video Streams  
- Kinesis data Analytics  
    -> Enables you to quickly author SQL code that continuously reads, processes, and stores data in near real time.  
    -> Using standard SQL queries on the streaming data, you can construct applications that transform and provide insights into your data.  
    -> Followings are some of example scenarios for using Kinesis Data Analytics:  
        -> __Generate time-series analytics__: You can calculate metrics over time windows, and then stream values to S3 or Redshift through a Kinesis data delivery stream.  
        -> __Feed real-time dashboards__: You can send aggregated and processed streaming data results downstream to feed real-time dashboards.  
        -> __Create real-time metrics__: You can create custom metrics and triggers for use in real-time mornitoring, notifications, and alarms.  

## Scenarios
1. You are working as a Solutions Architect for a startup in which you are tasked to develop a custom messaging service that will also be used to train their AI for an automatic response feature which they plan to implement in the future. Based on their research and tests, the service can **receive up to thousands of messages a day**, and all of these data are to be **sent to Amazon EMR** for further processing. It is crucial that **none of the messages will be lost**, **no duplicates will be produced** and that they are **processed in EMR in the same order as their arrival**.
    - Solution is `to create an Amazon Kinesis Data Stream to collect the messages`.
        - important requirements above the scenario:
            - data should not go missing, is durable, and streams data in the sequence of arrival.
        - Kinesis can do the job just fine because of its architecture:
            - A Kinesis data stream is **a set of shards that has a sequence of data records**,
            - and **each data record has a sequence number** that is assigned by Kinesis Data Streams.
            - Kinesis can also easily handle the high volume of messages being sent to the service.
            - ![kinesis_data_streams](./images/kinesis_data_streams.png)
            - Kinesis Data Streams enables **real-time processing of streaming big data**. 
                - It provides ordering of records, as well as the ability to read and/or replay records in the same order to multiple Amazon Kinesis Applications.
                - The Amazon **Kinesis Client Library (KCL)** delivers all records for a given partition key to the same record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream (for example, to perform counting, aggregation, and filtering)

## Differences between Amazon Kinesis Data Streams and SQS
- Amazon Kinesis Data Streams
    - 빅데이터 스트리밍을 실시간으로 처리할 수 있다.
    - 레코드를 순서대로 정리하고 여러 개의 Kinesis applications에서 같은 순서대로 레코드를 읽거나 리플레이 할 수 있는 기능을 제공
    - Amazone Kinesis Client Library (KCL)는 주어진 파티션 키에 대한 모든 레코드를 동일한 레코드 프로세서에서 제공하므로 동일한 Amazon Kinesis 데이터 스트림의 데이터를 읽는 여러 개의 애플리케이션을 보다 손쉽게 구축 가능(예, 계산, 집계 및 필터링 수행)
- Amazon Simple Queue Service (SQS)
    - 컴퓨터 간에 송수신하는 메시지를 저장하기 위한 안정적이고 확장성 뛰어난 호스팅 대기열을 제공
    - SQS를 사용하면 배포된 애플리케이션 구성 요소 간 데이터를 손쉽게 이동하고 자동화된 워크플로우 같이 메시지가 독립적으로 처리(메시지 수준 확인/실패 의미 체계 사용)되는 애플리케이션을 구축 가능

## When should I use Amazon Kinesis Data Streams, when should I use Amazon SQS?
- Amazon Kinesis Data Streams will be better with following:
    - 관련 레코드를 동일한 레코드 프로세서로 라우팅하는 경우(MapReduce를 스트리밍 하는 경우와 유사)
        - 예를 들어, 주어진 키에 대한 모든 레코드가 동일한 레코드 프로세서로 라우팅되는 경우 계산 및 집계가 훨씬 간단해진다.
    - 레코드를 순서대로 정렬하는 경우
        - 예를 들어, 애플리케이션 호스트의 로그 데이터를 로그 명령문의 순서는 유지한 채로 처리/보관 호스트로 전송하려는 경우
    - 여러 개의 애플리케이션이 동일한 스트림을 동시에 사용할 수 있도록 하는 경우
        - 예를 들어, 실시간 대시보드를 업데이트하는 애플리케이션이 있고, Amazon Redshift에 데이터를 보관하는 다른 애플리케이션이 있을 때, 이 2개의 애플리케이션이 동일한 스트림의 데이터를 동시에 독립적으로 소비하길 원하는 경우
    - 몇 시간 후 동일한 순서대로 레코드를 사용할 수 있도록 하는 기능
        - 예를 들어, 결제 애플리케이션이 있고 결제 애플리케이션보다 몇 시간 뒤에 실행되는 감사 애플리케이션이 있는 경우
        - Amazon Kinesis Data Streams는 데이터를 최대 7일간 저장하므로(default 24h) 결제 애플리케이션보다 최대 7일 뒤에 감사 애플리케이션을 실행할 수 있음.
- Amazon SQS will be better with following:
    - 메시징 의미 체계(ex. 메시지 수준 확인/실패) 및 제한 시간 초과
        - ex, 작업 항목 대기열이 있으며 각 항목이 개별적으로 완료 되었는지 추적하려는 경우가 이에 속한다.
        - Amazon SQS는 확인/실패를 추적하므로 애플리케이션은 지속적인 체크포인트/커서를 유지할 필요가 없다.
        - Amazon SQS는 구성된 제한 시간 초과 후 확인된 메시지를 삭제하고 실패한 메시지를 다시 전송한다.
    - 개별 메시지 지연.
        - ex, 작업 대기열이 있으며 개별 작업에 지연 시간을 지정하려 하는 경우가 이에 속한다.
        - Amazon SQS를 사용하면 최대 15분간의 지연 시간을 갖도록 개별 메시지를 구성할 수 있다.
    - 읽기 작업 시 동시성(concurrency)/처리량(throughput) 동적으로 증가
        - ex, 작업 대기열(work queue)이 있으며 백로그가 지워질 때까지 더 많은 readers를 추가하려는 경우가 이에 속한다.
        - Amazon Kinesis Data Streams를 사용하면 샤드의 수를 충분히 늘릴 수 있다. 그러나 이 작업을 수행하기 전에 충분한 수의 샤드를 프로비저닝해야 한다는 점에 유의
    - 투명하게 확장할 수 있도록 Amazon SQS의 기능 활용
        - ex, 이따금 발생하는 load spikes 및 비즈니스의 자연스러운 성장으로 인한 requests와 로드 변경 사항을 버퍼링하려는 경우가 이에 속한다.
        - 버퍼링된 각 요청은 개별적으로 처리될 수 있으므로 Amazon SQS는 투명하게 확장하여 사용자의 프로비저닝 지침을 받지 않아도 로드를 처리할 수 있다.

## Key concepts
### What is Shard?
- 샤드는 Amazon Kinesis Data Streams의 기본 처리량 단위
- 샤드 1개는 초당 1MB의 데이터 입력 및 2MB의 데이터 출력 용량을 제공하며, 샤드 1개는 초당 최대 1,000개의 PUT 레코드를 지원
- 데이터 스트림을 생성할 때 필요한 샤드 수를 지정하게 됨.
    - ex, 샤드가 2개 있는 데이터 스트림을 생성할 수 있다. 이 데이터 스트림은 초당 2MB의 데이터 입력 및 초당 4MB의 데이터 출력을 처리할 수 있으며 초당 최대 2,000개의 PUT 레코드를 허용한다.
- Amazon Kinesis Data Streams에서 샤드 수준 지표(shard-level metrics)를 모니터링하고 데이터 스트림 resharding을 통해 데이터 처리량이 변경됨에 따라 샤드를 동적으로 스트림에 추가하거나 스트림에서 제거할 수 있다. 

### What is a record?
- 레코드는 Amazon Kinesis Data Streams에 저장되는 데이터의 단위
- 레코드는 시퀀스 번호, 파티션 키, 데이터 blob으로 구성
- 데이터 blob은 사용자의 데이터 생성자가 데이터 스트림에 추가한 대상 데이터.
- 데이터 blob의 최대 크기(Base64로 인코딩하기 전 데이터 페이로드)는 1MB

### What is a partition key?
- 파티션 키는 레코드를 데이터 스트림의 다른 샤드로 분리하고 라우팅하는 데 사용됨
- 파티션 키는 Amazon Kinesis Data Streams 데이터 스트림에 데이터가 추가되는 동안 데이터 생산자가 지정
    - ex, 샤드가 2개 있는 데이터 스트림이 있다고 가정해보자(샤드1과 샤드2). 파티션 키 2개(키 A와 키 B)를 사용하도록 데이터 생산자를 구성하여 키 A가 있는 모든 레코드는 샤드 1에 추가하고 키 B가 있는 모든 레코드는 샤드 2에 추가할 수 있다.

### What is a sequence number?
- 시퀀스 번호는 각 레코드에 대한 고유 식별자
- Amazon Kinesis Data Streams에 데이터를 추가하기 위해 데이터 생산자가 PutRecord 또는 PutRecords 작업을 호출할 때 Amazon Kinesis에서 시퀀스 번호를 할당한다. 동일한 파티션 키에 대한 시퀀스 번호는 일반적으로 시간이 지남에 따라 증가한다. PutRecord 또는 PutRecords 요청 사이의 시간 간격이 길어질수록 시퀀스 번호도 커진다.