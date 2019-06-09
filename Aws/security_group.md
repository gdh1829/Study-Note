Security Group
===

AWS에서 제공하는 서버 보안 방화벽 설정 서비스

![Security Diagram](./images/security-diagram.png)

default(VPC) security group
기본 제공되고 있는 secutiry group으로서 모든 트래픽에 대하여 Inbound가 열려 있지만 접속 가능한 IP 대역(Source)은 default가 자기 자신으로 설정되어 있음.
즉, 같은 default(VPC) Security Group 설정 안에서만 접속이 허용되므로 외부에서는 접속 할 수 없음.

