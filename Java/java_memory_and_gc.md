# 자바 메모리와 GC

## 자바 메모리 구조
- 크게 5가지 영역으로 구분
    - 쓰레드마다 PC 레지스터, JVM stack, native method stack
    - 쓰레드공통 Heap, Method area
- PC 레지스터: 현재 수행중인 JVM 명령어가 들어감
- JVM 스택: 호출된 메소드의 매개변수, 지역변수, 리턴 정보들이 저장
- 네이티브 메소드 스택: 자바 외의 언어인 C, C++ 같은 것들을 수행하기 위한 영역
- method area: 클래스별 전역변수, 정적변수, 메소드 정보들 저장
- heap: 런타임 중 생성된 객체들이 동적으로 할당되는 곳

## 자바 GC(Garbage Collector)
- 모든 자바 애플리케이션은 JVM 환경에서 작동.
- JVM의 Runtime Data Area의 메모리 구조와 마찬가지로 GC 역시 자바 애플리케이션의 응답 시관과 성능에 밀접한 영향.
- JVM에서 메모리를 관리해주는 모듈
    - Heap 메모리를 재활용하기 위해서 더 이상 참조되지 않는 객체들을 메모리에서 제거.
    - 자바의 GC가 메모리 관리를 자동으로 해주지만, Mark and Sweep(사용하고 있지 않은 메모리 할당 탐색 제거) 과정은 STW(Stop the world - GC 쓰레드외에 모든 쓰레드가 pause)을 발생시켜 퍼포먼스에 영향을 주게 됨. 
        - Mark: GC root로부터 모든 변수를 스캔하면서 각각 어떤 객체를 참조하고 있는지 찾아서 마킹하는 과정
        - Sweep: Unreachable(참조X)한 객체를 Heap에서 제거하는 과정
        - Compact: GC 알고리즘에 따라 포함 유무가 다름, Sweep 후에 분산된 객체들을 Heap의 시작주소로 모아 메모리가 할당된 부분과 그렇지 않은 부분으로 나눔
- 구조
    - young gen(Eden, survivor0, survivor1), old Gen, meta space(GC 시에 필요한 클래스와 메소드의 요약 정보가 존재하는 영역)로 구성된다.
- GC 과정
    - 새로운 객체가 Eden 영역에 쌓이며, Eden 영역이 부족해지면 Minor GC가 발생
    - Reachable한 객체들만 Survivor 영역으로 옮겨지고 나머지 객체는 지워짐
    - 객체들이 살아남을 때마다 age +1 을 얻음
    - 다시 Eden 영역이 가득차고 minor gc가 발생하면 다른 Survivor 영역으로 살아남은 객체들이 채워짐.
    - 또 다시 age +1 의 과정이 반복됨
    - age가 특정 age threshold에 도달하면 old gen 영역으로 이동됨(Promotion이라 함)
    - old gen 영역마저 가득 찬다면 Major GC가 발생하며, 이는 minor GC에 비해 10배 이상의 시간을 사용하므로 성능에 큰 영향을 줌.
- GC 종류
    - Serial GC
        - 가장 단순 기본 GC
        - GC 처리 쓰레드 1개 -> stw가 김
        - Mark-Compact 알고리즘
    - Parallel GC
        - 자바 8 기본 GC
        - young gen의 GC를 멀티쓰레드로 진행
        - 전 세대 대비 stw 시간 감소
    - Parallel Old GC
        - 전세대 GC 개선 버전
        - old gen에서도 멀티쓰레드 GC 진행
        - mark - summary - compact 알고리즘
        - sweep: 단일 쓰레드가 old 영역 전체 스캔
        - summary: 멀티 쓰레드가 old 영역 분리 스캔
    - CMS GC (Concurrent Mark Sweep)
        - stw 시간을 줄이기 위해 고안
        - compact 과정 없음(기회비용: 메모리 단편화 문제)
    - G1 GC (Garbage first)
        - CMS GC 개선
        - java 9 기본 GC
        - Heap을 논리적으로 일정한 크기의 Region으로 나누고, 전체 Heap이 아닌 region 단위로 탐색
        - compact 진행
- APM(Application Performance monitor) ex. Scouter

