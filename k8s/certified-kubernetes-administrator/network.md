네트워크
---
/etc/hosts
/etc/resolve.conf
/etc/nsswitch.conf

ping vs nslookup vs dig
- ping: local hosts 파일부터 찾아보며 제공된 도메인의 IP 어드레스를 찾아서 동작한다.
- nslookup: local hosts 고려하지 않으며 오로지 DNS 서버로부터 검색을 실시.
- dig: nslookup 보다 더 디텔한 DNS 서버에 저장된 내용을 알려줌.

ip netns add {new_ns_name}
- 새로운 네트워크 네임스페이스를 등록하는 커맨드.

ip netns exec {ns} ip link
- ns 네임스페이스에서 ip link 커맨드 실행
- = 'ip -n {ns} link'와 같음.

네트워크 스위치와 라우트테이블에 대해 이해가 필요.

네트워크 스위치
- 동일 네트워크 장치들간의 데이터 패킷을 전달하는 장치.
- OSI 2계층(데이터링크)에 속함
- MAC 주소를 기반으로 패킷을 전달.
- 주로 LAN(로컬 영역 네트워크)에서 사용됨.

IP addr vs MAC addr 차이는?
- 서로 다른 개념으로 네트워크에서 각각 다른 역할을 한다. 이 두가지 주소체계는 네트워크에 필수적.
- MAC 주소 (Media Access Control Address)
  - NIC(네트워크 인터페이스 카드)에 고유하게 할당된 하드웨어 주소. 제조과정에 할당되는 물리적 주소. MAC 주소는 globally unique.
  - MAC 주소는 네트워크 장치가 서로를 식별하고 통신할 수 있도록 하는 역할.
  - MAC 주소는 48비트(6바이트)로 구성되며 일반적으로 16진수로 표현
    - 00:1A:2B:3C:4D:5E
  - 로컬 네트워크(LAN) 내에서 장치를 식별하고, 스위치와 같은 네트워크 장치는 MAC 주소를 사용하여 장치 간에 데이터를 전달.
- IP 주소
  - 네트워크 상에서 장치의 위치를 식별하는 논리적 주소.
  - 네트워크 간 데이터 통신을 위해 사용. 
  - 네트워크 계층(OSI 3계층)에서 동작하며, 패킷을 목적지까지 라우팅하는데 사용됨.
  - 네트워크 간에 데이터를 전달하는 역할.
  - 라우터는 IP 주소를 사용하여 패킷을 올바른 네트워크로 전달.
- MAC 주소는 LAN 내에서 장치를 식별. IP 주소는 전세계 네트워크 간 장치를 식별.

데이터 패킷(Data Packet)
- 네트워크 통신의 기본 단위로 데이터를 작고 관리 가능한 크기로 나눈 것. 이를 통해 데이터 전송의 네트워크 효율과 안정성을 확보.
- 보통 Header와 Payload로 구성.
  - Header: 패킷에 대한 제어 정보를 담고 있음. ex. 발신지 주소, 수신지 주소, 패킷 번호, 프로토콜 정보 등
  - Payload: 실제 전송되는 데이터. 사용자 데이터가 이곳에 포함.
- 개별 패킷에는 에러 검출 정보가 포함될 수 있어서, 데이터 손실이나 오류가 발생했을 때 해당 패킷만 재전송할 수 있음.


---
docker network
---

NONE network
- 아무 네트워크도 붙어있지 않음.
- 컨테이너는 컨테이너 바깥 네트워크에 도달 불가. 역방향도 X. 당연히 같은 호스트 내의 컨테이너끼리도 통신 X

HOST network
- 동일 호스트 내부에서는 호스트와 컨테이너끼리 아무 제약 없음.
- 서로 다른 컨테이너가 동일 포트를 사용할 수 없음. 왜냐하면 동일 호스트 네트워킹을 공유하고 있기 때문.

BRIDGE network
- internal private network가 생성됨.
- 도커 호스트와 컨테이너가 붙을 수 있음.
- 브릿지 네트워크가 생성되면, 상세
  - docker network ls
    - bridge 드라이버로 도커 브릿지 네트워크가 생성됨
  - 도커 호스트에서 ip link를 실행해보면 `docker0` 라는 IP 링크가 생성된 것을 볼 수 있음.
    - ip addr 커맨드를 실행해보면 docker0 인터페이스에 172.17.0.1/24 IP가 할당되어 있을 것.
    - 마치 네트워크 네임스페이스를 만드는 것과 비슷.
      - ip netns 를 실행해보면 docker가 네임스페이스를 만들어 놓았을 것.
      - 도커가 만들어둔 네임스페이스의 ID를 확인하고 docker inspect 를 통해 해당 컨테이너의 NetworkSettings를 확인해보면 SandboxID, SandboxKey에 해당 네임스페이스가 셋팅되어 있음을 알 수 있음.
  - 즉, 매번 컨테이너가 생성될때마다 도커는 네임스페이스를 생성하고, 네트워크 인터페이스 페어를 만들고, 브릿지 네트워크와 컨테이너를 서로 연결
- 포트 맵핑/포트 퍼블리싱 옵션
  - 컨테이너 생성시 도커 호스트의 8080 포트와 컨테이너의 80포트를 맵핑하라는 옵션 제공하면, 유저는 호스트의 IP에 8080포트를 통하여 컨테이너의 80포트로 포워딩 되는 것.
  - 어떻게 도커는 가능하게 하는걸까?
    - NAT rule을 등록해주는 것과 동일한 것을 해주는 것.
      - iptables -t NAT -A PREROUTING -j DNAT --dport 8080 --to-destination 80
    - 도커가 NAT rule을 등록하는데 도착지를 컨테이너IP와 함께 셋팅해주게 됨.
      - iptables -t NAT -A DOCKER -j DNAT --dport 8080 --to-destination 172.17.0.3:80
    - 확인해보기
      - iptables -nvL -t NAT

---
container networking interface(CNI)
---


---
k8s에서 네트워크 점검에 유용한 commands 
---
ip link
ip addr
ip addr add 192.168.0.1/24 dev eth0
ip route
ip route add 192.168.0.1/24 via 192.168.2.1
cat /proc/sys/net/ipv4/ip_forward
arp
netstat -plnt
route 

