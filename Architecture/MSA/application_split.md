# 애플리케이션 분리를 위한 패턴
- Event decoupling
- Strangler pattern
- Domain-driven design

## Event decoupling

## Strangler pattern
- 전체 시스템은 정상적으로 돌아가면서 모놀리식 아키텍처에서 점진적으로 마이크로 서비스 기반으로 코드와 API를 분리해나가는 패턴

## Domain-driven design
- 경계 맥락(Bounded contexts)을 통해 서비스와 팀을 분리하는 방법. 어떤 일을 수행하기 위해, 알아야 할 정보를 최소화하는 방식.
- 
- 


1. 실험 업무를 분리: 마이크로서비스로 분리 가능한 독립적인 기능 정의
1. 빠른 서비스 배포: 고객의 피드백에 따라 빠르게 기능 개발 및 재배포 진행
- MSA 기반 배포에서는 각 서비스간 API를 통한 느슨한 연결이 이루어짐. 느슨한 연결 속에서 언제든 실패/장애가 일어날 수 있음을 가정해야 한다.
- 실패에 대한 대비책: 
    - Circuit breaker: 회로 차단. 장애 전파 방지.
    - Side car: 서비스와 통신 부분을 분리
        - 오픈소스 엔보이
        - Service Mesh(오픈소스 istio, aws app mesh)
        - Canary Deployment