Elastic Load Balancer
===

ELB는 고가의 L4/L7 장비(로드 밸런서)를 구입하거나 소프트웨어로 서버를 구축하지 않아도 부하 분산과 고가용성(High Availability)를 제공하는 서비스  
ELB는 외부 트래픽뿐만 아니라 인터넷이 연결되지 않는 내부 네트워크에서도 사용 가능  

## ELB 기본개념
- L4(OSI Layer4)
    - OSI 레이어에서 4번째 전송 계층을 의미
    - TCP, UDP 등의 프로토콜이 대표적
    - 보통 OSI 레이어에서 3번쨰 네트워크 계층의 IP와 묶어서 처리
    - L4 로드 밸런싱이라고 하면 IP 주소와 포트 번호를 기준으로 트래픽을 분배
- L7(OSI Layer7)
    - OSI 레이어에서 7번째 애플리케이션 계층을 의미
    - HTTP 프로토콜이 대표적
    - L7 로드 밸런싱이라고 하면 HTTP 헤더의 내용 기준으로 트래픽을 분배
- 로드밸런싱 알고리즘
    - 트래픽을 각 EC2 인스턴스로 분배할 때 사용하는 알고리즘
    - ELB는 Round Robin 알고리즘 사용
    - Round Robin: 우선 순위를 두지 않고 순서대로 분배하는 방식
- Health Check
    - ELB에 연결 중인 EC2 인스턴스가 정상적으로 가동 중인지 확인하는 기능
    - EC2 인스턴스가 중단(Unhealthy)되었다고 판단되면 해당 EC2 인스턴스는 트래픽 분배에서 제외
- Connection Draining
    - Auto Scaling이 사용자의 요청을 처리 중인 EC2 인스턴스를 바로 삭제하지 못하도록 방지하는 기능.
    - ELB에 연결 중인 EC2 인스턴스를 Target Group으로부터 제거하게 되면, 곧바로 제거 되는 것이 아니라 Deregistration Delay 시간을 갖고 Draining status로 변경됨. Draining인 중에는 새로운 Request를 ELB로부터 받지 않고 이미 연결 중인 In-flight request에 대하여 남은 처리를 마무리할 수 있는 시간을 갖게 된다.
- Sticky Sessions
    - 사용자의 세션을 확인하여 적절한 EC2 인스턴스로 트래픽을 분배하는 기능(Http Cookie를 이용한 세션)
    - L7의 로드밸런싱 기능
    - ex. 동일한 사용자가 서비스에 계속 접속할 때 처음 접속했던 EC2 인스턴스에 연결 시켜줌.
    - 이 기능을 사용하지 않으면 Round Robin 알고리즘에 따라 매번 다른 EC2 인스턴스에 연결되버린다.
- Latency
    - ELB 로드 밸런서와 EC2 인스턴스 간의 지연시간
- HTTP 2xx, 4xx, 5xx
    - EC2 인스턴스에서 리턴한 HTTP Response Code
- ELB HTTP 4xx, 5xx
    - ELB에서 리턴한 HTTP Error Code
- Surge Queue Length
    - ELB 로드 밸런서에서 EC2 인스턴스로 전달되지 못하고 Queue에 남아 있는 요청의 개수
- Spillover Count
    - Surge Queue가 가득 차서 ELB 로드 밸런서가 거부한 요청의 개수

## ELB Pre-warming
ELB는 하나의 장비가 아니라 내부적으로 여러 AWS 리소스가 조합된 서비스  
ELB는 IP주소가 아니라 도메인으로 접속  
따라서 ELB로 들어오는 트래픽이 급격히 늘어날 것으로 예상되면 미리 AWS에 ELB의 처리량을 늘려달라고 요청할 수 있다. 서비스 출시 전 테슽 상황에서도 가능.  
ELB Pre-warming은 AWS Support에 가입되어 있어야 신청 가능  

## Sticky Session
Classic ELB에서만 지원  
두 가지 종류
- Enable Load Balancer Generated Cookie Stickiness
    - ELB 로드 밸런서가 생성한 쿠기를 사용.
    - Expiration Period: 쿠기가 유지되는 시간 설정. 값을 설정하지 않을 시 쿠키를 삭제하지 않고 계속 유지 시킴.
    - 지정한 시간 동안은 계속 같은 EC2 인스턴스로 연결되며 Expiration Period가 끝나면 기존 Round Robin 방식으로 연결된다. 즉, 다른 인스턴스로 연결될 수 있다.
    - 웹 브라우저의 개발자 도구로 확인해보면 Cookie에 AWSELB가 생성한 값을 확인할 수 있다.
- Enable Application Generated Cookie Stickiness
    - 서버의 애플리케이션이 생성한 쿠키를 사용
    - Cookie Name: 서버의 애플리케이션이 생성한 쿠키 이름을 설정