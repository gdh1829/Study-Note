Basic Concepts of Elasticsearch
===
※Elasticsearch hereinafter referred to as ES  
이 문서는 이하의 ES 공식사이트의 영문 문서를 번역해 본 문서입니다.
Reference [Elasticsearch Basic concepts](https://www.elastic.co/guide/en/elasticsearch/reference/current/_basic_concepts.html)

## Near Realtime(NRT)
Elasticsearch is a near real time search platform. What this means is there is a slight latency (normally one second) from the time you index a document until the time it becomes searchable.
ES는 실시간 검색 플랫폼에 가깝다. 문서를 색인할 때부터 검색 가능할 때까지 약간의 대기 시간(일반적으로 1초)이 있다는 것이다.

## Cluster
A cluster is a collection of one or more nodes (servers) that together holds your entire data and provides federated indexing and search capabilities across all nodes. A cluster is identified by a unique name which by default is "elasticsearch". This name is important because a node can only be part of a cluster if the node is set up to join the cluster by its name.  
클러스터는 모든 데이터를 함께 보유하고 모든 노드에서 연합 인덱싱 및 검색 기능을 제공하는 하나 이상의 노드 (서버) 모음이다. 하나의 클러스터는 하나의 유니크한 이름으로 구별되고 기본값은 "elasticsearch"이다. 이 이름은 만약 노드가 클러스터 이름으로 조인되도록 셋업되어 있다면, 그 노드가 해당 클러스터의 일부 일 수 있기 때문에 클러스터의 이름은 중요하다.  

Make sure that you don’t reuse the same cluster names in different environments, otherwise you might end up with nodes joining the wrong cluster. For instance you could use logging-dev, logging-stage, and logging-prod for the development, staging, and production clusters.  
다른 환경에서 같은 클러스터 이름을 재사용하지 않도록 명심해야 한다. 그렇지 않으면, 노드가 잘못된 클러스터에 조인되어버릴 수도 있다. 예를 들어, 개발, 스테이징, 프로덕션 클러스터에서 logging-dev, logging-stage 및 logging-prod를 사용할 수 있다.

Note that it is valid and perfectly fine to have a cluster with only a single node in it. Furthermore, you may also have multiple independent clusters each with its own unique cluster name.  
노드가 하나 뿐인 클러스터를 보유하는 것도 문제 없이 완벽히 괜찮다. 또한, 고유한 클러스터 이름을 갖는 각각의 독립 클러스터에 갖는 것도 OK다.

## Node
A node is a single server that is part of your cluster, stores your data, and participates in the cluster’s indexing and search capabilities. Just like a cluster, a node is identified by a name which by default is a random Universally Unique IDentifier (UUID) that is assigned to the node at startup. You can define any node name you want if you do not want the default. This name is important for administration purposes where you want to identify which servers in your network correspond to which nodes in your Elasticsearch cluster.  
하나의 노드는 클러스터의 일 부분이고, 데이터를 저장하며, 클러스터의 인덱싱과 검색 기능에 참여하는 하나의 서버이다. 클러스터처럼, 노드는 이름으로 식별되고, 노드의 이름은 시작 시에 노드에 할당되는 UUID가 기본값이다. 디폴트 UUID를 원하지 않는다면, 원하는 이름으로 노드의 이름을 정의할 수도 있다. 이 이름은 네트워크 상에서 엘라스틱 클러스터의 노드에 해당하는 서버를 식별하려는 관리 목적에서 중요하다.  

A node can be configured to join a specific cluster by the cluster name. By default, each node is set up to join a cluster named elasticsearch which means that if you start up a number of nodes on your network and-assuming they can discover each other—they will all automatically form and join a single cluster named elasticsearch.  
노드는 클러스터 이름으로 특정 클러스터에 조인되도록 설정되어 있다. 디폴트로, elasticsearch라는 클러스터에 조인되도록 되어 있으며, 즉 네트워크 상에서 다수의 노드를 시작하고 서로를 발견할 수 있다고 가정하면 자동으로 elasticsearch라는 단일 클러스터를 형성하고 조인한다.  

In a single cluster, you can have as many nodes as you want. Furthermore, if there are no other Elasticsearch nodes currently running on your network, starting a single node will by default form a new single-node cluster named elasticsearch.  
싱글 클러스터에서, 원하는 만큼 많은 노드를 가질수 있다. 또한, 현재 네트워크상에서 움직이고 있는 다른 엘라스틱서치 노드가 없다면, 하나의 싱글 노드를 시작하는 것은 디플트로 elasticsearch라는 이름의 싱글 노드 클러스터를 형성된다.

## Index
An index is a collection of documents that have somewhat similar characteristics. For example, you can have an index for customer data, another index for a product catalog, and yet another index for order data. An index is identified by a name (that must be all lowercase) and this name is used to refer to the index when performing indexing, search, update, and delete operations against the documents in it.
Index는 다소 유사한 특성을 갖는 문서의 모음이다. 예를 들어, 고객 데이터에 대한 인덱스, 제품 카탈로그에 대한 인덱스, 또 다른 데이터에 대한 인덱스를 가질 수 있다. 인덱스는 이름으로 구별되며(반드시 모두 소문자) 그리고 이 이름은 색인된 해당 문서에 대하여 색인, 검색, 갱신, 그리고 삭제를 수행할 때 참조하는데 사용된다.

In a single cluster, you can define as many indexes as you want.
하나의 클러스터에 대하여 원하는 만큼 많은 색인이 가능하다.

## Type (※ deprecated in 6.0.0)
A type used to be a logical category/partition of your index to allow you to store different types of documents in the same index, eg one type for users, another type for blog posts. It is no longer possible to create multiple types in an index, and the whole concept of types will be removed in a later version. See Removal of mapping types for more.
타입은 같은 인덱스에서 다른 타입의 문서를 동일한 인덱스에 저장할 수 있도록 인덱스의 논리적 카테고리/파티션으로 사용된다. 

## Document
A document is a basic unit of information that can be indexed. For example, you can have a document for a single customer, another document for a single product, and yet another for a single order. This document is expressed in JSON (JavaScript Object Notation) which is a ubiquitous internet data interchange format.
Document는 색인을 생성할 수 있는 기본 정보 단위이다. 예를 들어, 한 명의 고객에 대한 document, 한 제품에 대한 document, 그리고 여러 다른 것을 위한 또 다른 document를 가질 수 있다. 이러한 document는 JSON 형태로 표현된다.

Within an index/type, you can store as many documents as you want. Note that although a document physically resides in an index, a document actually must be indexed/assigned to a type inside an index.
index/type 내에서, 원하는 만큼 많은 수의 document를 저장할 수 있다. document는 물리적으로 index에 상주하지만, document는 index안의 type에 indexed/assigned 되어야 한다. 

## Shard & Replica
An index can potentially store a large amount of data that can exceed the hardware limits of a single node. For example, a single index of a billion documents taking up 1TB of disk space may not fit on the disk of a single node or may be too slow to serve search requests from a single node alone.  
index는 잠재적으로 단일 노드의 하드웨어 제한을 넘어설 수 있는 많은 양의 데이터를 저장할 수 있다. 예를 들어, 1TB의 디스크 공간을 차지하는 10억개의 document의 하나의 인덱스는 단일 노드의 디스크에 맞지 않거나 단일 노드의 검색 요청만을 처리하기에는 너무 느릴 수도 있다.

To solve this problem, Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.  
이러한 문제를 해결하기 위해서는, ES는 index를 shard라 불리는 여러 조각으로 세분할 수 있는 기능을 제공한다. 하나의 index를 생성할 때, 간단히 원하는 shard의 수를 정의할 수 있다. 각 shard 자체는 클러스터의 모든 노드에서 호스트될수 있는 완전히 기능적이고 독립적인 index이다.  

Sharding is important for two primary reasons:  

* It allows you to horizontally split/scale your content volume  
Sharding은 내용의 보륨을 수평적으로 분할 할 수 있도록 한다.  
* It allows you to distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput  
(잠재적으로 여러 노드에 분산되어 있는)shards 전역에 걸쳐서 operation을 분산시키거나 병렬로 만들 수 있도록 하여, 성능/처리량을 증가시킬 수 있다.  

The mechanics of how a shard is distributed and also how its documents are aggregated back into search requests are completely managed by Elasticsearch and is transparent to you as the user.  
어떻게 shard가 분산되고 또한 어떻게 documents가 검색 요청에 대하여 다시 집계되는지에 대한 메카니즘은 ES에 의해 완전히 관리되며 유저에게도 투명하다.

In a network/cloud environment where failures can be expected anytime, it is very useful and highly recommended to have a failover mechanism in case a shard/node somehow goes offline or disappears for whatever reason. To this end, Elasticsearch allows you to make one or more copies of your index’s shards into what are called replica shards, or replicas for short.  
언제든지 실패가 발생할 수 있는 네트워크/클라우드 환경에서 만약 shard/node가 어떤 이유로 오프라인이 되거나 또는 어떤 이유로든 사라져버렸을 경우, failover 메커니즘을 취하는 것이 매우 유용하며 추천된다. 이를 위해, ES는 replica shards 또는 replicas라 불리는 하나 이상의 index's shard를 만들 수 있도록 한다.

Replication is important for two primary reasons:

* It provides high availability in case a shard/node fails. For this reason, it is important to note that a replica shard is never allocated on the same node as the original/primary shard that it was copied from.  
Replica는 Shard/Node가 실패할 경웨 높은 가용성을 제공한다. 이러한 이유로, replica를 절대 복사된 original/primary shard와 동일한 노드에 할당되지 않는다.  
* It allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel.  
모든 Replica에서 병렬적으로 검색이 수행될 수 있기 때문에, 검색 볼륨/처리량을 수평 확장(scale out)할 수 있다.

To summarize, each index can be split into multiple shards. An index can also be replicated zero (meaning no replicas) or more times. Once replicated, each index will have primary shards (the original shards that were replicated from) and replica shards (the copies of the primary shards).  
요약하면, 각 index는 여러 개의 shards로 나눠질 수 있다. 하나의 index는 또한 replica가 없거나 하나 이상으로 복제될 수 있다. 한 번 replicated되면, 각 index는 primary shards(original/primary shards)과 replica shards(primary shards의 복제본)을 갖게 된다.  

The number of shards and replicas can be defined per index at the time the index is created. After the index is created, you may also change the number of replicas dynamically anytime. You can change the number of shards for an existing index using the _shrink and _split APIs, however this is not a trivial task and pre-planning for the correct number of shards is the optimal approach.  
shards와 replicas의 수를 해당 index가 생성될 때 index마다 정의할 수 있다. index가 생성되면, 언제든지 동적으로 replica의 수를 변경할 수 있다. _shrink와 _split APIs를 사용하여 이미 존재하는 index에 대해서도 shard의 수를 변경할 수 있으나, 이는 사소한(작은) 작업이 아니며 올바른 shard의 수에 대한 사전의 계획이 최적이 방법이다.  

By default, each index in Elasticsearch is allocated 5 primary shards and 1 replica which means that if you have at least two nodes in your cluster, your index will have 5 primary shards and another 5 replica shards (1 complete replica) for a total of 10 shards per index.  
디폴트로, ES의 각 index는 5개의 primary shards와 1개의 replica가 지정되어 있다. 이는 만약 최소 두 개의 노드를 갖고 있는 클러스터를 갖고 있다면, index에는 5개의 primary shards와 5개의 replica shard(1개의 전체 복제본)가 있으며 index당 총 10개의 shards가 있게 된다.  

### Note
Each Elasticsearch shard is a Lucene index. There is a maximum number of documents you can have in a single Lucene index. As of [LUCENE-5843](https://issues.apache.org/jira/browse/LUCENE-5843), the limit is 2,147,483,519 (= Integer.MAX_VALUE - 128) documents. You can monitor shard sizes using the _cat/shards API.  
각 ES shard는 Lucene index이며 하나의 Lucene index에 대하여 최대 document의 수가 있다. LUCENE-5843에 따르면, 해당 limit은 21.47억여개(maximum positive value for a 32bit signed binary integer in computing)이다. _cat/shards API를 통하여 shard size를 모니터링할 수 있다.