참조링크  
https://bluese05.tistory.com/45  
https://www.44bits.io/ko/post/communication_between_vpcs__aws_vpc 

VPC
===
 1. vpc 생성
 1. subnet 생성
 - 이중화를 원할 경우, Availability Zone을 다르게 하여 2개의 서브넷 생성
 1. Internet Gateway 생성
 - <Attach to VPC>를 통해 해당 VPC의 게이트웨이로 지정
 1. Route tables 설정
 - 처음 VPC를 만들 때, Route Table ID는 자동으로 생성되어 있음
 - 외부에서 오는 모든 접속에 대하여 오픈하기 위해서는 Routes를 default(0.0.0.0/0)로 설정

 VPC Peering connection
 ===
![vpc_peering](./images/vpc_peering.png)
VPC를 사용하면 격리된 네트워크 환경을 만들 수 있고, VPC 피어링을 사용하면 격리된 네트워크 간의 연결 통로를 생성할 수 있다. VPC 피어링은 같은 계정의 VPC 뿐만 아니라 다른 계정의 VPC에 대한 연결도 가능. 2018년 2월에는 AWS 백본을 기본으로 통신하는 멀티 리전 간 vpc 피어링 지원을 발표하기도 하였다. VPC 연결을 지원하지 않는 경우에는 VPN 연결을 사용할 수 있다.
AWS는 VPC의 기존 인프라를 사용하여 VPC 피어링 연결을 생성. 이는 Gateway, VPN 연결도 아니며 물리적 하드웨어 각각에 의존하지 않는다.

하지만 이러한 네트워크를 연결하는 기능이 만능은 아니다. IPv4의 경우 VPC 간에 CIDR이 겹치는 경우 피어링을 생성할 수 없다. 또한 VPC의 기본적인 기능인 네트워크를 격리하는데 있다는 면에서, 무분별한 피어링 생성은 VPC 본래의 의미를 퇴색시킬 수 있다. 따라서 가능하면 일찍부터 VPC 설계에 대해서 고민하는 것이 좋고 VPC 피어링을 사용하는 경우 정확히 필요한 범위만을 열어줄 필요가 있다.

피어링 연결을 위해서는 다음과 같은 각 단계가 필요
1. 피어링 연결 생성
    - 요청자 VPC(requester)에서 수락자 VPC(Accepter)로 요청을 하면, Accepter에서 연결을 수락해야만 실제 연결
    - 같은 계정, 같은 리전의 VPC 간의 연결을 생성할 떄는 요청자/수락자 순서가 크게 중요하지 않으나, 이 경우에도 Accepter VPC에서 요청을 수락해야만 한다.
2. 피어링 연결에 대한 규칙을 각 서브넷의 라우트 테이블에 추가
    - 연결된 피어링 pcx-xxxxxxx를 Target으로 설정하여 서로의 Destination을 추가한다.
    - 이를 통해 서로의 서브넷 리소스가 통신이 가능하게 된다.
3. VPC 시큐리티 그룹을 통해서 다른 VPC의 IP 대역에 대한 접근을 허용
    - 원칙적으로 inbound rule의 source에는 같은 VPC에 속한 시큐리티 그룹만 등록 가능하지만 Peering Connection 을 생성한 후라면 VPC의 시큐리티 그룹을 등록하는 것이 가능해짐.
    - VPC 피어링 커넥션이 생성되지 않았을 때, 다른 VPC 시큐리티 그룹을 소스로 강제로 추가하려고 하면 다음과 같은 에러 메시지를 볼 수 있다: You have specified two resources that belong to different networks.

다른 VPC의 인스턴스에 정상적으로 접근 가능한 것을 확인할 시에 traceroute 명령어로 다른 경로를 거치지 않고, 상대 인스턴스에 곧바로 연결되는 것을 모니터링 할 수 있다. 

VPC Peering Connection Life Cycle

Why it is better to use DNS rather than IP
===
VPC 외부에서는 public IP를 통해서만 인스턴스에 접근할 수 있다. 하지만 VPC 내부에서는 Private IP로 접속하는 것이 유리. IP를 사용하는 경우, 같은 인스턴스에 접근을 할 때 퍼블릭 IP와 프라이빗 IP를 구분해서 사용해야 한다.

하지만 PUBLIC DNS를 사용하면 VPC 외부와 내부에서 조회되는 IP가 자동적으로 달라진다. 
VPC 외부와 내부에서 같은 인스턴스의 DNS를 nslookup를 사용해 조회해보면 알 수 있다. 같은 DNS를 조회하지만 조회된 IP가 각각 다르게 나온다.

즉, VPC 외부에서는 Public IP를, 내부에서는 Private IP를 반환하는 것을 알 수 있다.