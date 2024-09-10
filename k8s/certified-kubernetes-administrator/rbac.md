
## kube-apiserver authorization mode
- AlwaysAllow(default), AlwaysDeny, Node, ABAC, RBAC, Webhook
- how to check it out
  - cat /etc/kubernetes/manifests/kube-apiserver.yaml
  - ps aus | grep -i "authorization-mode"

## check access
> kubectl auth can-i create deployments
yes
> kubectl auth can-i delete nodes
no

### 타 유 권한 확인
> kubectl auth can-i create deployments --as dev-user
no
> kubectl auth can-i delete nodes --as dev-user
yes

### 타 유저의 test 네임스페이스에서의 권한 확인
> kubectl auth can-i create deployments --as dev-user --namespace test
no

## API groups and resource names 확인
> kubectl api-resources