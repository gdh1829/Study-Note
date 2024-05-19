# K8s Networking
ref> https://kubernetes.io/docs/concepts/cluster-administration/networking/

- Docker는 Container에 IP Addr을 할당하는 것과 달리 K8s는 Pod에 할당
- 10.244.0.0
## Internal Networking

### Cluster Networking
- k8s는 네트워킹 구현에 있어서 다음의 근본적인 요구사항을 부과한다.(단 의도적인 네트워크 세분화 정책을 제외하고)
  - 모든 PODs는 NAT 없이 다른 어떤 Nodes의 어떤 Pods와도 통신할 수 있어야 한다.
  - Nodes의 agents(ex, system daemons, kubelet)은 해당 동일 Node의 모든 Pods와 통신할 수 있어야 한다.
- Note: 리눅스와 같은 호스트 네트워크에서 실행되는 Pods를 지원하는 플랫폼의 경우, Pod가 Node의 호스트 네트워크에 연결되면, NAT 없이도 모든 Nodes의 모든 Pods와 통신할 수 있어야 한다.
- K8s의 IP 주소는 Pod scope에서 존재한다
  - 동일 Pod 내에서의 컨테이너들은 그들의 network namespace를 공유한다.
  - IP address, MAC address 포함하여.
  - 이 말은 즉슨, 동일 Pod 내의 컨테이너들은 localhost 상에서 서로의 모든 ports에 접근할 수 있다.
  - 또한 즉슨, Pod 내의 컨테이너들은 port usage를 조정(coordinate) 해야한다는 것을 의미하지만, 이는 VM 에서의 프로세스와 다르지 않으며, 이를 "IP-per-pod" model이라고 한다.

## Services

### NodePort
- Cluster 외부의 유저가 클러스터 내부 POD의 애플리케이션과 통신을 이어주는 서비스. (마치 External Service로 만들어주듯)
- NodePort 서비스가 클러스터의 특정 포트를 리슨하고 있고, Cluster 외부 유저가 Cluster의 IP와 PORT를 목적지로 요청을 건내면 해당 PORT를 리스닝하고 있던 NodePort 서비스가 해당 요청을 POD의 애플리케이션에게 포워딩 해줌.

### ClusterIP
- 클러스터 내부에 버추얼 IP를 만들어 서로 다른 서비스간 일관된 인터페이스의 통신을 도움.
- 사용 환경에서 복수의 서버/티어 환경으로 구성되어 있으며 상시 up/down이 발생하므로 POD IP는 수시로 바뀌게 된다.
- ClusterIP는 원하는 서버끼리 하나의 인터페이스로 묶을 수 있는 기능을 제공한다.

### LoadBalancer
- 