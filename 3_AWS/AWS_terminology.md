AWS terminology
===

## EBS(Elastic Block Store)
 * 가상화 서비스 된 일종의 하드디스크
 * 파일 저장은 S3를 사용하고 EC2를 웹서버 용도로만 쓴다면 큰 용량 설정은 필요 없다. 1GB정도.
 * 사용한 만큼 과금되는 종량제 서비스
 * 내부적으로 데이터를 실시간 복제하고 있기 때문에 실제 HDD나 SSD에 비해서 데이터를 잃어버릴 확률이 현저히 낮다.
 * 스냅샷 기능을 제공해서 EBS의 현재 상태 그대로 보존 가능
 * Cloud Watch를 통해 EBS의 통계 열람 가능
 * EC2와 독립적이기 때문에, EC2 인스턴스를 제거해도 데이터 유지
   (※이는 옵션을 통해 조정된다. **Delete on Termination** 선택사항을 체크하면, 해당 EC2가 Termination 될 때, 함께 EBS도 제거된다는 의미.)
 * EBS는 하나의 Instance에서만 접근할 수 있다. 즉, 여러 instance가 하나의 같은 EBS volume을 사용할 수 없다는 것. 이런 경우 S3가 대체 방법이 될 수도 있다. 그렇지만 S3는 느리다.
 * EBS로 생성한 하나의 저장소(디스크)를 하나하나를 **volume**이라고 부름
 * Volume Type: 주로 General Purpose(SSD), Provisioned IOPS(SSD), Magnetic이 있다.
 * Provisioned IOPS: 디스크 장치의 성능을 조정할 수 있는 것을 말함. 즉, IOPS(Input/output Per Second)를 조정하여 디스크 성능 조정. 단, 높은 IOPS를 지정한 만큼 가격이 비싸진다.

## Tag Instance
 * 인스턴스에 대한 정보(이름은 무엇이고, 관리자는 누구이며, etc)를 case-sensitive key-value pair로 기록하여 두는 것.

## Security Group
 * 일종의 방확벽과 비슷한 무료 기능
 * 해당 Instance에 대하여 어떤 접근에 대하여 허용하겠는지에 대한 설정이 이루어진다.
 * Protocol type, Port range, Source(IP, CIDR, Security group etc)
 * Protocol 타입은 Linux OS라면 기본적으로 SSH로서 port 22번이, Windows라면 RDP로서 3389의 port가 default로 지정되어 있다. 
 * 이외에도 웹서버로 운영하고자 한다면 Http, Https, 또는 이외에도 여러가지 형태의 프로토콜을 지정 가능
 * Security Group이외에도 서버 보안을 위해 aws 유저가 key-pair name을 지정하면 AWS에서 RSA private key를 랜덤으로 생성하여 제공을 하고 파일로 독립 보관하게 된다.

 ## Scalability
  * 확장성이라는 의미로서 사용자 수의 증대에 유연하게 대응할 수 있는 정도를 의미
  * EC2에서는 서버 사용량 증대에 따른 instance type의 변경 또는 서버 수의 증감 등을 통해 유연하게 그때그때 상황에 따라 대처 가능성







