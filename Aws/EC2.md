EC2
===

## Elastic IPs
EC 인스턴스를 생성 시 __Auto-assign Public IP__ 설정을 할 수 있어, Public IP를 지정받을 수 있다.  
하지만 이는 dynamic한 IP로서 매번 생성시 또는 중단 시에는 사라지고 재 시작시 변하게 된다.
즉, 인스턴스가 중지되면 Public IP가 반납되는 것이다. 이는 만약 도메인을 구입하여 EC2 인스턴스의 Public IP와 연결을 하였는데, 바뀌어 버리면 장애발생  

그래서 이때 필요한 것이 Elasitc IP이다. Elastic IP는 고정된 Public IP를 사용할 수 있게 해준다. Elastic IP와 associate되면 기존 Public IP는 없어진다.  
※ 주의사항: Public IP 발급 후 EC2에 연결 해 두지 않고, 미사용시 과금 발생!  
AWS에서 public IP 반납을 받기 위한 조치사항인 듯 하다.

## instance 생성 관련
* Instance Storage
- m1.small부터 사용가능
- EBS와 달리 Instance Storage는 Intance를 정지하면 데이터가 사라진다. 대신 EBS(Magnetic)보다 속도가 빠르다.

## instance 생성 후 접속
* chmod 600 awskeypair.pem
- aws의 keypair를 root만 rw로 설정해두기
* ssh -i awskeypair.pem ec2-user@{publicIP}
* 매번 keypair를 설정하기 번거로울 때
- sudo vi /etc/ssh/ssh_config
- IdentityFile /home/devko/awskeypair.pem을 입력

## Placement Group
- 물리적으로 인접한 곳에 EC2 인스턴스를 생성하여 네트워크 퍼포먼스를 극대화할 수 있다.
- 10Gbps 네트워크를 제공. 단, 인스턴스도 10Gbps를 지원하는 유형이어야 한다.
- EC2 instance를 생성할 때, Placement Group를 설정해야 하며 이미 생성된 EC2 인스턴스는 Placement Group에 포함시킬 수 없다.
- 클러스터링, 고성능 컴퓨팅(HPC, High Performance Computing)에 적합
- 추가 요금 없음

## Bundle Instance (instance store AMI)
- 인스턴스 스토리지를 Root 장치로 사용하는 Windows EC2 인스턴스의 내용을 S3 버킷에 저장하는 기능
- Bundle Tasks: Bundle instance 기능이 처리되는 과정을 칭함. Bundle task가 완료되면 s3버킷에 저장된 이미지 파일로 AMI를 생성 가능

## Network Interfaces
- ENI(Elastic Network Interface)를 생성하고 EC2 인스턴스에 장착
- EC2 인스턴스에 ENI를 여러 개 장착할 수 있고, 장착과 제거를 유동적으로 할 수 있음
- Ec2 인스턴스가 속하지 않은 다른 VPC와 통신을 하고 싶을 때 ENI를 사용
    -> 공개망과 사설망을 함꼐 사용하고 싶은 경우
    -> EC2 인스턴스에서 대역폭이 다른 네트워크를 2개 가지고 싶을 때