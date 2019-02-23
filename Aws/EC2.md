EC2
===

## Elastic IPs
EC 인스턴스를 생성 시 __Auto-assign Public IP__ 설정을 할 수 있어, Public IP를 지정받을 수 있다.  
하지만 이는 dynamic한 IP로서 매번 생성시 또는 중단 시에는 사라지고 재 시작시 변하게 된다.
즉, 인스턴스가 중지되면 Public IP가 반납되는 것이다. 이는 만약 도메인을 구입하여 EC2 인스턴스의 Public IP와 연결을 하였는데, 바뀌어 버리면 곤란하다.  

그래서 이때 필요한 것이 Elasitc IP이다. Elastic IP는 고정된 Public IP를 사용할 수 있게 해준다. Elastic IP와 associate되면 기존 Public IP는 없어진다.  
※ 주의사항: Public IP 발급 후 EC2에 연결 해 두지 않고, 미사용시 과금 발생!  
AWS에서 public IP 반납을 받기 위한 조치사항인 듯 하다.

