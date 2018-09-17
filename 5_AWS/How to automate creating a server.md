Process of how to automate creating a server(EC2 instance)

Chef programming

nodes(Base) <- grouping <- roles <- grouping <- site-cookbooks

상위 클래스?로부터의 파라미터가 자식 클래스?의 파라미터에 overwrite가 된다.

위의 프로세스로 AMI가 만들어지며 AWS에 등록이 된다.

AMI는 Amazon Machine Images일 뿐이므로 실질적인 서버가 만들어진 것은 아니다. Docker Images와 비슷한 느낌.

하지만 참고로 AMI가 만들어지는 프로세스에서 잠시 실제 Instance가 만들어지지만, 이는 AMI 생성이 되면 사라지는 일시적인 instance일 뿐이다.

그렇게 AMI가 만들어지면 AMI를 통해서 AWS UI를 통해 서버를 생성할 수도 있지만, 이는 수동적인 것일뿐.

자동화를 위해서는 Cloud Formation이 필요.

Cloud Formation을 통해서 AMI의 시큐리티 그룹, 타겟그룹, VPN지정 등등 여러 서버 생성 부수적인 연결과 infra 작업을 수행해준다.


