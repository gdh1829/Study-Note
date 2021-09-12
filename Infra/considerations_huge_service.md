# 대규모서비스
---

## 대규모서비스가 가져야할 특성

- Elastic
    - 확장성
    - 서비스의 확장과 축소가 자유롭고 쉬워야 함
- Resiliency
    - 장애회복성
    - 서비스 장애시 가능한 매뉴얼 처리가 없이 자동 회복되어야 함
- Automation
    - 자동화
    - 배포부터 장애처리 등 대부분이 자동화 되어 있어, 버튼 클릭만으로 진행되어야 함
- Monitoring
    - 모니터링
    - 서비스 상태는 항상 모니터링 되어야함.

## SPOF(Single Point of Failure)

- 어떤 지점에 장애가 발생하면 전체 서비스에 장애를 낼 수 있는 부분
    - ex. 
    - 단일 서버 운영시 
    - Switch, Route 등 서버 외의 하드웨어 부분
    - Network Bandwidth 한계
        - 10Gbps 스위치에 3개의 서버가 붙어있고 각각이 8G/2G/2G를 사용하여 10Gbps 이상의 데이터 전달이 발생 -> Capacity를 넘어가는 순간부터 Packet Drop이 발생
    - Switch의 장애