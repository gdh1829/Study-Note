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