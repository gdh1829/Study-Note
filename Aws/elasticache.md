ElastiCache
===

In-Memory Cache는 모든 데이터를 메모리에만 올려 놓고 사용하는 데이터베이스의 일종. Memcahced, Redis, etc  
일반적인 RDBS는 디스크에 데이터를 영구적으로 저장해 놓고, 필요한 데이터만 메모리에 읽어서 사용. MySQL, Oracle, PostgreSQL, etc

In-Memeory Cache는 모든 데이터를 메모리에 올려 놓는 것이 특징.  
디스크에 접근하지 않고 메모리로만 모든 처리를 하기 때문에 데이터 저장 및 검색 속도가 매우 빠름.  
단, 데이터는 딱 메모리 크기까지만(운영체제 사용량 제외) 저장 가능.  
또한, 메모리에만 저장되어 있기 때문에 서버의 전원 공급이 중단되면 데이터는 소멸.  

## ElastiCache의 두 가지 캐시 엔진
 - Memcached
    - Region의 AZ 별로 생성 가능
    - Memcached cluster는 노드를 계속 추가 할 수록 데이터를 저장할 수 있는 공간이 늘어남.
    - Snapshot과 Read Replica 지원 X
 - Redis
    - Memcached와 달리 클러스터 구성 불가. 따라서 노드를 추가한다고 해서 저장할 수 있는 전체 메모리 용량이 늘어나지는 않음
    - 데이터를 저장 할 수 있는 메모리 용량은 각 캐시 노드가 제공하는 메모리 용량에 한함.
    - Snapshot과 Read Replica 지원 O
    - Read Replica는 마스터 캐시 노드(Primary)에 장애가 발생하면 자동으로 Read Replica가 마스터 캐시 노드로 승격되는 Failover 기능 작동
    - Read Replica는 Replication Group이라는 논리적인 개념이 안에 위치
    - Read Replica는 한 Region 안에서 여러 AZ에 생성 가능.
    - Redis 캐시 노드가 제공하는 메모리 용량을 넘어서는 데이터를 저장하기 위해서는 애플리케이션 레벨에서 데이터를 여러 캐시 노드에 분산하여 저장하는 Sharding을 구현해야 함.

※Sharding
일반적인 데이터베이스와 마찬가지로 인 메모리 캐시도 샤딩을 구현할 수 있음. 데이터 종류별로 서버를 분할하는 방식, 사용자 이름 순, 날짜 순 등으로 분할하는 방식, 해시 키를 기준으로 분할하는 방식 등 다양한 방식이 존재.

## ElastiCache 캐시 노드 유형
ElasticCache에서는 EC2나 RDS와는 달리 인스턴스를 캐시 노드라고 부름.   
이 캐시 노드도 EC2나 RDS처럼 여러 사양으로 나눠져 있음.  
RDS는 생성된 DB 인스턴스의 인스턴스 클래스를 변경할 수 있지만, ElasticCache는 생성된 캐시 노드의 캐시 녿 유형을 변경할 수 없음.  
한 번 생성하면 캐시 노드 유형은 고정되며 캐시 노드 유형을 바꾸려면 삭제 후 다시 생성해야 함.  

## ElastiCache Memcached and Redis' Security Group
Memcached Port: 11211  
Redis Port: 6379  
RDS의 데이터베이스 엔진은 AWS 외부(인터넷)에서 접속이 허용되어 있지만, ElastiCache의 캐시 엔진은 AWS외부에서 접속할 수 없음.  
Security Group을 설정하여 모든 IP 대역에 대해 접근을 허용하더라도 동일한 VPC에 속한 EC2 인스턴스에서만 접속 가능.  
Memcached와 Redis는 telnet으로 접속 가능  
>telnet \<enpoint\> \<port\>   
>stat #현재 캐시 노드의 정보가 표시  

redis의 경우 [redis-cli](http://redis.io/download)라는 전용 클라이언트가 있음.  
노드 타입이 cache.m1.small 이상인 경우에 한하여 Automatic Backups를 지원. 최장 35일  

## ElastiCache Failover
ElastiCache Replication Group을 생성하여 Add Read Replica를 하면 Cluster에 Primary와 Read Replica가 나타난다.  
평소에는 Primary 엔드포인트 주소가 마스터인 Primary를 가리키고 있다. 그래서 쓰기 작업은 Primary 엔드포인트 주소에 접속하여 실시.  
Failover 기능이 동작하면 자동으로 Primary 엔드포인트 주소는 Slave를 가리키게 되고 쓰기 작업을 수행한다. 따라서 Failover를 위한 작업을 따로 하지 않아도 됌.  

## Demote, Promote
- Demote: 마스터 Redis 클러스터를 다른 마스터 Redis 클러스터의 Read Replica로 만드는 기능.
- Promote: Read Replica Redis 클러스터를 새로운 마스터 Redis 클러스터로 승격시키는 기능. 
  - 이 기능을 사용하면 이전 마스터 Redis 클러스터와의 복제 관계는 끊어지고, 별개의 Redis 클러스터가 됨.  
  - Prmote기능은 서비스되고 있는 캐시 클러스터와 동일한 데이터를 가진 개발 및 테스트용 캐시 클러스터를 생성하고 싶을 때, 지역이나 언어별로 서비스를 분리할 때 활용 가능.
