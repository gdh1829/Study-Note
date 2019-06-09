인스턴스 접속시 
ssh -A 옵션을 사용하기
i.e) ssh -A ec2-user@123.123.123.123
이 옵션은 ForwardAgent를 활성화해준다. 이 옵션을 통해 로컬 머신의 키를 SSH로 접속한 머신에서 다시 다른 머신에 접속할 떄 인증키로 사용하는 것이 가능해짐. 정상적으로 동작하지 않는 경우, 로컬 머신에서 인증에 사용하는 키를 미리 ssh-add <KEY_PATH> 명령어로 등록하고 ssh-add -l 명령어로 동록되어 있는지 확인해본다.

SSH Tunneling
Bastion host에서 ssh 접속을 proxy 하는 여러 방법이 있다.  
그 중 SSH Tunneling을 이용해 외부에서 Private instance에 접속하는 방법  
예를 들어, 아래와 같은 환경이 있다.
- Bastion host Public IP: 52.100.1.1
- Access Target instance Private IP: 10.10.101.225

먼저 Local PC에서 Bastion host에 SSH할 때, -L 옵션을 이용하여 접속
아래는 SSH를 이용해 Bastion host에 접속하는데 local 터널링으로 접속하는 명령어
> ssh -i key.pem -L 22:10.10.101.225:22 ec2-user@<Bastion Public IP>  
여기서 -L 옵션인 **22:10.10.101.255:22**는 "로컬 포트 22번으로 접속 타켓인 instance(10.10.101.225)의 22번 포트로 접속하겠다"는 의미

위의 접속을 해놓은 상태에서 새로운 터미널을 하나 더 열고
> ssh -i key.pem ec2-user@localhost  
위와 같이 접속하면 자동으로 타겟 instance로 SSH Tunneling 되어 접속된다.
위와 같은 방법으로 Private Subnet에 위치한 모든 서버에 접속 가능.