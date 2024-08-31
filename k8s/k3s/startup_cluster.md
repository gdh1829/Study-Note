# VM 환경 구성을 위한 툴 설치 및 alias 등록
```
brew install multipass
alias mp="multipass"
```

# 지원 우분투 버전 조회
```
mp find
```

# VM node 론칭
-- jammy -> Ubuntu 22.04 LTS
```
mp launch --name master --cpus 1 --memory 1G --disk 5G jammy
mp launch --name node1 --cpus 1 --memory 1G --disk 5G jammy
mp launch --name node2 --cpus 1 --memory 1G --disk 5G jammy
```

# vm 결과 확인
```
mp list
```
➜  Study-Note git:(master) ✗ mp list
Name                    State             IPv4             Image
master                  Running           192.168.64.3     Ubuntu 22.04 LTS
                                          10.42.0.0
                                          10.42.0.1
node1                   Running           192.168.64.4     Ubuntu 22.04 LTS
                                          10.42.1.0
                                          10.42.1.1
node2                   Running           192.168.64.5     Ubuntu 22.04 LTS
                                          10.42.2.0
                                          10.42.2.1

# 마스터 노드 K3S 설치
K3S_KUBECONFIG_MODE="644" => k3s installer 에게 kubectl 이 클러스터에 접근하기 위해 사용하는 설정 파일을 생성 허용.
'--' => multipass 명령어와 실제 컨테이너 안에서 실행할 명령어를 구분
```
mp exec master -- /bin/bash -c "curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE=644 sh -"
```

# 마스터노드와 워커 노드의 클러스티링을 위한 마스터 IP 정보 및 토큰 정보 준비
워커노드들을 같은 클러스터에 포함시키기 위해 마스터에 저장된 ip 주소와 k3s token 정보 전달.
```
K3S_NODEIP_MASTER="https://$(mp info master | grep "IPv4" | awk -F' ' '{print $2}'):6443"
K3S_TOKEN="$(mp exec master -- /bin/bash -c "sudo cat /var/lib/rancher/k3s/server/node-token")"
```

# 워커 노드 k3s 설치 및 클러스티링을 위한 마스터 노드 URL 및 토큰 전달
```bash
mp exec node1 -- /bin/bash -c "curl -sfL https://get.k3s.io | K3S_TOKEN=${K3S_TOKEN} K3S_URL=${K3S_NODEIP_MASTER} sh -"
mp exec node2 -- /bin/bash -c "curl -sfL https://get.k3s.io | K3S_TOKEN=${K3S_TOKEN} K3S_URL=${K3S_NODEIP_MASTER} sh -"
```

# 마스터 노드에서 워커 노드와 클러스팅 확인
```bash
mp exec master kubectl get nodes
```
ex. 
➜  Study-Note git:(master) ✗ mp exec master kubectl get nodes
NAME     STATUS   ROLES                  AGE   VERSION
master   Ready    control-plane,master   9m    v1.30.4+k3s1
node1    Ready    <none>                 69s   v1.30.4+k3s1
node2    Ready    <none>                 30s   v1.30.4+k3s1

# 파드 동작 확인
```bash
mp exec master -- kubectl run web --image=nginx
mp exec master -- kubectl get po -o wide
# 10.42.2.3 -> web pod에 할당된 내부 IP
mp exec master -- curl 10.42.2.3
```

➜  Study-Note git:(master) ✗ mp exec master -- kubectl get po -o wide
NAME   READY   STATUS    RESTARTS   AGE   IP          NODE    NOMINATED NODE   READINESS GATES
web    1/1     Running   0          15s   10.42.2.3   node2   <none>           <none>

➜  Study-Note git:(master) ✗ mp exec master -- curl 10.42.2.3        
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...skip...
