Packet
===

In computer networks, a packet is a container or box that carries data over a TCP/IP network and internetworks. __A packet is the most fundamental logical arbitration of data that is passed over a network.__  
컴퓨터 네트워에서, 패킷은 TCP/IP 네트워크와 인터네크워크에서 데이터를 옮기는 컨테이너 또는 유닛이다. 패킷은 네트워크를 통해 전달되는 가장 기본적인 논리적 중재이다.

A packet normally represents the smallest amount of data that can traverse over a network at a single time. A TCP/IP network packet contains serveral pieces of information, including the data it is carrying, source destination IP addresses, and other constraints required for quality of service and packet handling.  
패킷은 일반적으로 한 번에 네트워크를 통해 전달할 수 있는 데이터의 가장 작은 양을 의미한다. TCP/IP 네트워크 패킷은 운반하는 데이터, 도착지 IP 주소 및 여타 서비스 품질과 패킷 처리에 관련된 여러 정보를 가지고 있다.  

Whenever a node on a network sends some data over the network, it passes the data frame to the switch, and later to the router. __The router, after looking at the destination IP addresses, encapsulates the data and routes it toward the recipient. This encapsulated data is the packet that is forwarded over the network.__  
네트워크 상의 하나의 노드가 네트워크를 통해 데이터를 전송할 때마다, 데이터 프레임을 스위치로 전달하고 후에 라우터로 전달한다. 도착지 IP 주소를 본 후 라우터는 해당 데이터를 캡슐화 시키고 이를 수신자에게 전달한다. 네트워크 상에서 전달되는 이 캡슐화된 데이터가 패킷이다.  

Packets contain two distinct types of information to reach the destination completely and correctly, namely control information and the data it is carrying. The control information includes source destination addresses, sequencing format, error detection and correction mechanisms, all of which help to ensure the optimal delivery of data. The control information usually resides in the header and trailer, encapsulating the user data in between them.  
패킷은 해당 도착점에 완전히 그리고 정확하게 도달하기 위해 두 뚜렷한 종류의 정보, 즉 제어 정보와 전송할 데이터를 가지고 있다. 제어 정보는 도착지 주소와 시퀀스 포맷, 에러 판명 그리고 수정 메커니즘 등을 가지고 있어, 이러한 모든 메커니즘은 데이터의 최적의 전송을 보장한다. 제어 정보는 보통 헤더와 트레일러에 있으며, 그 사이에서 유저 정보를 캡슐화 한다.
