Comparison ES & RD
===

Elasticsearch는 Lucene을 바탕으로 개발된 분산 검색엔진  
설치와 서버 확장이 매우 편리하기 떄문에 개발하고 있는 시스템에 검색 기능이 필요하다면 Elasticsearch가 추천된다.  
분산 시스템이기 때문에 대상 용량이 증가했을 때 대응하기가 무척 수월한 것이 장점

Elasticsearch와 Relational Database 용어 비교
| Relational Database  | Elasticsearch  |
|:-:|:-:|
| Database  | Index  |
| Table  | Type  |
| Row  | Document  |
| Column  | Field  |
| Schema  | Mapping  |
| Index  | Everything is indexed  |
| SQL  | Query DSL  |

## JSON 기반의 스키마 없는 저장소
Elasticsearch는 검색엔진이지만, NoSQL처럼 사용할 수 있다. 데이터 모델을 JSON으로 사용하고 있어서, 요청과 응답을 모두 JSON 문서로 주고받고, 소스 저장도 JSON형태로 저장한다. 스키마를 미리 정의하지 않아도, JSON 문서를 넘겨주면 자동으로 인덱싱한다. 숫자나 날짜 등의 타입은 자동으로 매핑한다.

## Multi-tenancy
Elasticsearch는 multi-tenancy를 지원. 하나의 elasticsearch 서버에 여러 인덱스를 저장하고, 여러 인덱스의 데이터를 하나의 쿼리로 검색할 수 있다.
예를 들어, 날짜별로 인덱스를 분리해 로그를 저장하고 있고, 검색 시에는 검색 범위에 있는 날짜의 인덱스를 하나의 쿼리로 요청할 수 있다.
log-2018-11-03, log-2018-11-04 인덱스에 대해 한번에 검색 요청
```Bash
curl -X GET http://localhost:9200/ log-2018-11-03, log-2018-11-04_search
```

## 확장성과 유연성
플러그인을 이용해 기능 확장을 할 수 있다. 예를 들어, Thrift 플러그인이나 Jettty 플러그인을 사용하면 전송 프로토콜을 변경할 수 있다. BigDesk나 Head를 설치하면 elasticsearch 모니터링 기능을 사용할 수 있다.

## 분산 저장소
elasticsearch는 분산 검색엔진이다. 키에 따라 여러 샤드가 구성되는 방식으로 데이터를 분산한다. 인덱스는 각각의 샤드마다 구성된다. 각각의 샤드는 0개 이상의 복제본을 가진다. elasticsearch는 클러스터링을 지원하며 클러스터가 가동될 때 여러 노드 중 하나가 메타데이터 관리를 위한 마스터 노드로 선출된다. 마스터 노드가 다운되면 자동으로 클러스터 내의 다른 노드가 마스터가 된다. 노드 추가 또한 간단하다. 같은 네트워크에 노드를 추가하는 경우 추가된 노드가 멀티캐스트를 이용해 자동으로 클러스터를 찾아 자신을 추가한다. 같은 네트워크를 이용하지 않을 경우 유니캐스트로 마스터 노드의 주소를 명시해 주어야 한다.

## REST API 사용
Elasticsearch은 아래와 같은 식의 REST API 를 제공.    
> http://host:port/{index}/{type}/{action|id}  
문서 생성
> curl -xPUT http://localhost:9200/log2018-12-27/hadoop/1
> curl -xGET http://localhost:9200/log2018-12-27/hadoop/1
> curl -xDELETE http://localhost:9200/log2018-12-27/hadoop/1
검색
> curl -xGET http://localhost:9200/log2018-12-27/hadoop/_search
> curl -xGET http://localhost:9200/log2018-12-27/_search
> curl -xGET http://localhost:9200/_search
인덱스 상태 보기
> curl -xPUT http://localhost:9200/log2018-12-27/_status

인덱스 생성과 삭제, 매핑 생성과 삭제, 검색, 설정 변경 등 대부분의 기능을 REST API를 통해 제공. REST API 이외에도 Java, Python, Ruby 등의 언어별 클라이언트도 제공  

## 성능 최적화 Tip
메모리와 오픈 파일 수  
검색할 데이터가 많아질수록 많은 메모리가 필요. elasticsearch를 운영하다 보면 메모리 사용으로 인한 문제를 많이 겪게 된다.  
elasticsearch 커뮤니티에서 권장하는 운영 방법에 따르면, elasticsearch 전용 서버를 운영할 때는 메모리 용량의 절반만 elasticsearch에 할당 하고, 나머지 메모리 용량은 운영체제가 시스템 캐시 목적으로 사용할 수 있도록 하는 것이 좋다.  
메모리 크기는 ES_HEAP_SIZE 환경 변수를 설정하거나 JVM의 -Xms와 -Xmx 값을 사용해서 설정할 수 있다.
> Heap 크기를 지정한 실행  
> bin/ElasticSearch -Xmx=2G -Xms=2G  
Elasticsearch를 사용할 때는 OOME(Out Of Memory Error)가 발생하는 경우가 많다. 필드 캐시가 최대 Heap 크기를 넘어서면서 발생하는데, index.cache.field.type 설정을 기본값인 resident 대신 soft로 설정하면 soft reference를 활용하므로 캐시 영역에 대해 우선 Garbage Collection을 실행해 문제를 해결할 수 있다.
> 필드 캐시 타입 설정  
> index.cache.field.type: soft  
데이터가 많아지면 인덱스 파일 개수 또한 증가하게 된다. elasticsearch가 사용하고 있는 Lucence에서 인덱스를 세그먼트 단위로 관리하기 때문이다. 경우에 따라 MAX_OPEN 파일 개수를 넘어서는 일도 발생한다. ulimit 명령으로 최대 오픈 파일 제한을 변경해야 한다. 권장되는 값은 32000 ~ 64000이지만, 시스템 규모나 데이터의 양에 따라 더 큰 값으로 설정해야 할 수 도 있다.

## Index Optimization
날짜별로 인덱스를 관리하면 밑에서 보는 것처럼 관리가 필요 없는 오래된 로그를 쉽고 빠르게 삭제할 수 있어서, 문서별로 TTL 값을 설정해 삭제하는 것 보다 시스템에 주는 오버헤드가 적다.
> curl -XDELETE 'http://localhost:9200/log-2018-11-03/'  
Index Optimization을 수행하면 세그먼트를 병합시킨다. 이러한 방식으로 검색 성능을 향상시킬 수 있다. 다만 시스템에 부담을 주므로 시스템 사용이 적은 시간대에 작업하도록 해야 한다.
> Index Optimization  
> curl -XPOST 'http://localhost:9200/log-2018-11-03/_optimize'  

## Shard와 Replica


