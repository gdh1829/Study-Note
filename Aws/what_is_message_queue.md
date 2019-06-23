Message Queue
===

## Message Oriented Middleware (MOM)
- 비동기 메시지를 사용하는 다른 응용 프로그램 사이에서 데이터 송수신을 의미
- **Message Queue(MQ)** : MOM을 구현한 시스템
- **Broker**: Message Queue 시스템
- **AMQP(Advanced Message Queueing Protocol)**: 메시지 지향 미들웨어를 위한 프로토콜
- 메시지 큐는 별도의 공정 작업을 연기할 수 있는 유연성을 제공하여 SOA(Service-Oriented Architecture)의 개발에 도움을 줄 수 있다.
- 프로그래밍에서 MQ는 프로세스 또는 프로그램 인스턴스가 데이터를 서로 교환할 때 사용하는 방법. **이때 데이터를 교환할 때 시스템이 관리하는 메시지 큐를 이용하는 것이 특징**. 이렇게 서로 다른 프로세스나 프로그램 사이에 메시지를 교환할 때 **AMQP (Advanced Message Queuing Protocol)**을 이용. 
- AMQP는 메시지 지향 미들웨어를 위한 open standard application layer protocol이다. AMQP를 이용하면 다른 벤더 사이에 메세지를 전송하는 것이 가능한다 JMS (Java Message Service)가 API를 제공하는 것과 달리 AMQP는 wire-protocol을 제공하는데 이는 octet stream을 이용해서 다른 네트워크 사이에 데이터를 전송할 수 있는 포맷으로 이를 사용하게 된다.

## 동작: Producer(Sender) -> Queue(Message) -> Consumer(Receiver)
- Producer가 Message를 queue에 넣어두면 consumer가 message를 가져와 처리하는 방식

## 굳이 하나의 서버를 더 거치는 이 과정이 도움이 될까?
- 서버가 클라이언트와 동기 방식으로 많은 데이터 통신을 하게 되면 보틀넥 현상이 생기게 되고, 서버의 성능이 저하될 수 있기에, 이를 막고자 또 하나의 미들웨어에 메시지를 위임하여 순차적으로 처리하는 것.

## 무조건 좋은 것?
- 중간에 추가적인 미들웨어 서버를 거치기 때문에 즉각적인 서비스 처리가 불가능. 최대한 텀을 줄이기 위한 MQ 튜닝, Consumer를 스케일 아웃하던지, Consumer에서 병목 현상을 찾고 리팩토링으로 개선점을 찾아 서비스를 제공할 수도 있다. 반대로 Consumer 역할에서 서버사이드나 DB 사이드에서 제대로 받춰주지 못한다면, 브로커 자체 성능이 저하될 수 있음.