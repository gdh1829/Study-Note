# minikube

ref> https://minikube.sigs.k8s.io/docs/start/

## how to start minikube for mac m1
- minikube install by homebrew
> brew install minikube
- start cluster
> minikube start
- kubectl access test
> kubectl get po -A
- set up alias
> alias kubectl="minikube kubectl --"

## control minikube
- pause/resume minikube 
> minikube pause/unpause
- stop
> minikube stop
- list up addons
> minikube addons list
