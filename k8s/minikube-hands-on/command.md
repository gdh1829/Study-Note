# command collection

## kubectl

### shortforms
- replicaset -> rs
- deployment -> deploy

### command samples

#### kubectl explain
- kubectl explain rs
#### kubectl get 
- kubectl get pods
- kubectl get rs
- kubectl get deploy
- kubectl get all
  - deployments, replicaset, pods 모두 한번에 볼 수 있음.
#### kubcetl describe
- kubectl describe replicaset {replica-set-name}
  - namespace/selector condition/pods status/pod template/events 등 상세 확인 가능.
- kubectl describe {kind} {name}
  - kind: ex. pods/replicaset/deployments
  - name: 해당 타입으로 생성된 이름
#### kubectl create/delete/edit
- kubectl delete pod {pod-name}
- kubectl create 
  - kubectl create -f {definition-yaml-file} --record
    - record=true: deployment revision history change-cause 기록 on
  - kubectl create deployment --help
  - kubectl create deployment {name} --image={image} --replicas={number}
- kubectl edit rs {replica-set-name} 
  - replicaset의 definition.yml 문서를 오픈하여 직접 수정 가능.
- kubectl edit deployment {deployment-name} --record
#### kubectl scale
- kubectl scale rs {replica-set-name} --replicas={number}
  - replicaset의 스케일링 pods 수를 조정
  - 'kubectl edit rs {replica-set-name}'을 통해 definition yml 파일로 접근하여 spec.replicas를 조정하는 것과 같은 효과
#### kubectl rollout
- deployment의 revision을 만들고 deployment strategy에 따라 update/rollback을 가능하게 함.
- kubectl rollout status {deployment-name} 
- kubectl rollout history {deployment-name} 
  - 해당 deployment의 그 동안의 revision과 변경 이력을 보여줌
- kubectl rollout undo {deployment-name}
  - 이전 revision으로 rollback 시킴.
  - rollout undo 커맨드 실행 후 kubectl rollout history 커맨드를 실행해보면, undo로 돌아가게 된 revision은 히스토리에서 사라지고, 새로운 revision이 추가된 것을 확인할 수 있음. undo로 돌아간 revision과 새 revision은 완전히 동일하므로.
  - ex. revision 1,2,3(current)가 있을때, rollout undo 실행시 revision 2를 대상으로 rollback이 되는데, 그러면 history에는 revision 4가 새로이 등록되고 revision 2는 목록에서 사라져 보이게 됨.
#### kubectl apply
- kubectl apply -f {deployment-definition-yaml-file}
  - deployment-definition yaml 파일을 수정 후 deployment 적용한다.
  - apply -f는 definition 파일을 직접 수정 후 apply로 적용하는 과정인데, 이를 한번에 kubectl edit 커맨드는 통하여 definition yaml 파일을 바로 수정 후 자동 apply되는 것과 같다.
  - 새 rollout이 트리거 되고, new revision of the deployment가 생성됨.
  - 참고,
    - deployment-definition yaml 파일에서 container image를 수정하여 저장 후, apply로 적용한 것과 유사하게 `kubectl set image deployment {deployment-name} {container-name}={new-image-name}`의 커맨드를 통해서도 적용은 가능하다. 다만, 이런 방식을 사용할 경우, actual deployment configuration과 definition yaml파일에는 변경 사항이 반영되지 않아 불일치하는 괴리가 생긴다.



temp memo
deployment strategy
- recreate
  - 기존 deployment를 제거 후, 다음 deployment를 실행. 
  - old 모두 제거 후 new가 배포되는 사이, Application down 시간이 있어 end user가 사용 불가한 영향을 줌.
- rolling update
  - old/new를 하나씩 교체하면서 deploy
    - old one down first, then new one up each by each
    - 만약 old ones가 6대 돌아가는 상황에서 문제(기동 될 수 없는 설정)가 있는 new deployment를 했다면? 
      - rolling update이기 때문에 old 1대는 다운되어 5대인 상황이 되고, 다음 new 1대를 띄우게 되는데 그 1대가 기동이 불가하므로 더 진행되지 않고 old 5대인 상황이 유지되어 애플리케이션 운영에 문제가 되지 않음.
      - 이는 구체적으로 RollingUpdateStrategy가 어떻게 설정되어 있느냐에 따라 점진적으로 교체되는 컨테이너의 수가 결정된다.
        - ex. 25% max unavailable, 25% max surge
      - 이후 rollout undo 커맨드로 다시 이전 버전으로 롤백을 하게 되면, down되어 있던 old 1이 다시 기동되며 총 6대가 유지된다.
  - k8s deployment default strategy  

![screenshot](./image/deployment_strategy.png)  
kubectl describe deployment 커맨드를 통해 StrategyType과 Events 섹션의 차이를 살펴볼 것.