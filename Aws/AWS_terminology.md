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

## ELB(Elastic Load Balancer)
 * aws에서 제공하는 lb이다.
 * 사용량 증가에 대한 리퀘스트 부하를 elb에 등록시킨 서버로 분산의 역할을 담당
 * custom으로 설정한 주기적 health check로 연결된 서버의 상태를 계속 확인하며 부하가 적은 서버로 리퀘스트를 분산시키며 균형을 맞춰준다.
 * Scale out과 ELB 사용에 주의사항으로서 사용자 데이터에 대한 처리가 있겠다. 예를 들어, 어떤 사용자에 대한 정보를 session에 저정해 두게 될 시, 그 다음 같은 유저에 대한 리퀘스트를 ELB가 다른 웹서버로 연결시켰을 때, 해당 웹서버의 session에는 유저에 대한 정보가 없기 때문에, 올바르지 못한 Response를 보여줄 수가 있다. 이런한 점들을 고려하여 architect를 잘 설계해야하며, 유저 정보를 session이 아닌 database에 저장하는 방법으로 대응 하는 등 다른 방법에 대한 고려가 필요하다.
 * ELB 한대가 어느정도까지 리퀘스트 부하를 처리 가능한지는 ? 
 







