Latency
===
Latency -> 호출(대기) 시간
Throughput -> (일정 시간에 처리해야 하는)처리량

__Latency is the amount of time a message takes to traverse a system. In a computer network__, it is an expression of how much time it takes for a packet of data to get from one designated point to another. It is sometimes measured as the time required for a packet to be returned to its sender.
Latency는 메시지가 시스템을 가로지나는데 걸리는 시간의 양을 의미한다. 컴퓨터 네트워크에서는 한 지점에서 다른 지점으로 하나의 데이터 패킷을 얻는 데 걸리는 시간을 의미한다. 때때로, 패킷이 다시 보낸 곳으로 돌아오는데 요구되는 시간으로 측정되기도 한다.

Latency depends on the speed of the transmission medium(e.g., copper wire, optical fiber or radio waves) and the delays in the transmission by devices along the way (e.g., routers and modems). __A low latency indicates a high network efficiency.__
Latency는 전송 수단(구리선, 광선 또는 수신파 등)의 속도와 라우터와 모뎀 등의 방식에 따라 디바이스의 전송 지연과 관련이 있다. low latency는 높은 네트워크 효율을 의미한다.

__Latency and _throughput_ are the two most fundamental mesuares of network performance.__ They are closely related, but __whereas latency measures the amount of time between the start of an action and its completion, throughput is the total number of such actions that occur in a given amount of time.__
Latency와 throughput은 네트워크 성능의 가장 중요한 두가지 기본적 기준이다. 둘은 밀접한 관련이 있지만, latency는 action의 시작과 completion 사이의 시간의 정도인 반면, throughput은 주어진 시간에 얼마나 해당 action이 일어나는지 수량에 대한 것이다. 

__Sending data in large packets has a higher throughput than sending the same data in small packets both because of the smaller number of packet headers and because of reduced startup and queuing latency.__ If the data is streamed(i.e., sent in a continuous flow), propagation latency has little effect on throughput, but if the system waits for a acknowledgment after each packet before sending the next, the resulting high propagation latency will greatly reduce throughput.  
큰 패킷으로 데이터를 전송하는 것은 같은 데이터를 작은 패킷으로 데이터를 전송하는 것보다 더 적은 수의 패킷 헤더와 시작 및 큐 대기 시간이 짧기 때문에 처리량(throughput)이 높다. 데이터가 스트리밍되면, 전파(전달) 대기 시간은 처리량에 거의 영향을 미치지 않지만, 만약 시스템이 다음 전송 전에 각 패킷 이후에 수신 확인을 기다리는 경우, 높은 전파 지연(대기 시간)으로 처리량이 크게 감소한다.

__Latency is also important consideration with regard to other aspects of computer, particularly where _real time_(i.e., nearly instantaneous) response is requried.__ For example, in some Internet games, a high latency (also called _lag_) can add to the difficulty of determining which player performed an action first (such as shooting an opponent or answering a question). In playing computer-based musical instruments, latencies greater than 100 miliseconds make it difficult for players to get the nearly instantaneous feedback that they require.  
Latency는 또한 특히, 실시간 응답이 요구되는 컴퓨터의 다른 측면과 관련하여 중요한 고려사항이다. 예를 들어, 인터넷 게임에서 높은 대기 시간(렉)은 어떤 플레이어가 액션을 먼저 취했는지 정하는데 어려움을 더한다. 컴퓨터 기반 음악 장치에서, 100ms 이상의 latency는 플레이어가 원하는 즉각적인 피드백을 얻기 어렵게 한다.  

The __ping__ and __traceroute__ commands are widely used to identify latency problems on networks.  
ping과 traceroute는 네트워크 대기 시간 문제를 확인하는데 널리 쓰이는 커맨드이다.