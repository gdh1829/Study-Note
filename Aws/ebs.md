EBS
===

## EBS
- `Elastic Block Storage` : EC2 Instance에 장착하여 사용할 수 있는 가상 저장 장치
EBS는 EC2 인스턴스에서 제공하는 기본 용량 보다 더 사용해야 할 때, 운영체제를 중단시키지 않고 용량을 자유롭게 늘리고 싶을 때, 영구적인 데이터 보관이 필요할 때, RAID 등의 고급 기능이 필요할 때 사용.  
- EBS는 EC2에 설치된 OS에서 그냥 일반적인 하드디스크나 SSD처럼 인식됨. 원하는 크기로 만들 수 있고, 성능(IOPS) 또한 원하는 수치로 설정 가능.   
- 사용자가 삭제하기 전까지는 데이터를 안전하게 유지.  
- Elastic Block Store에서 Block은 Block Device라고 하여 Unix/Linux 계열 OS에서 일정한 크기(Block) 단위로 읽고 쓰는 저장 장치를 부르는 용어. 자기테이프, 플로피디스크, 하드디스크, 광학디스크, SSD 등의 플래시메모리가 대표적.  

## EBS의 기본개념
- Volume: EBS의 가장 기본적인 형태로 OS에서 바로 사용 가능한 형태
- Image: AMI(Amazon Machine Image)를 줄여 부르는 말. OS가 설치된 형태이며 이 AMI로 EC2 instance를 생성
- Snapshot: EBS 볼륨의 특정 시점을 그대로 복사해 저장한 파일을 의미. snapshot을 이용하여 EBS volume과 AMI를 생성할 수 있음.
- IOPS(Input/Output Operation Per Second): 저장장치의 성능 측정 단위. AWS에 추가 비용을 지불하여 더 높은 성능(IOPS)의 EBS를 생성가능. IOPS는 16kb 단위로 처리됨. 따라서 작은 크기의 파일이 있다면 16kb 단위로 묶어서 처리하면 높은 성능을 낼 수 있음.

## EBS를 별도 생성 후, EC2 인스턴스에서 사용하기
1. AWS Console로부터 Create Volume  
-> attach할 인스턴스와 같은 availability zone으로 설정해야만 해당 인스턴스에 사용가능. 서로 다른 AZ인 경우 사용 불가
2. 생성한 volume의 stat이 in-use인지 확인
3. ec2 인스턴스에서 EBS volume format
    - EBS를 OS에서 사용하려면 알맞은 파일 시스템으로 포맷해줘야 한다. 
    - ssh로 ec2 instance에 접속
    - `sudo mkfs -t ext4 {attachment path}`를 실행  
    -> 콘솔에서 해당 볼륨의 Attachment information 필드 값을 확인하여 path를 지정
    ex. sudo mkfs -t ext4 /dev/xvda
4. EC2 인스턴스에 볼륨을 mount
    - linux에서는 저장 장치를 사용하려면 mount과정이 필요
    - `ls /dev/sdf -al` 명령어를 입력하여 /dev/xvda 장치(이전 단계에서 포맷한 볼륨)가 있는지 확인
    - `sudo mount /dev/xvda /mnt` 를 입력하여 mount.
5. 확인
    - `df -h` 명령을 통하여 현재 마운트된 저장 장치의 목록을 확인

## EC2 인스턴스로부터 EBS volume 제거하기
0. AWS Console로부터 detach를 실행하거나 instance 내부에서 아래와 같이 직접도 가능
1. 제거 명령
    - `sudo unmount {mounted volume path}` 이전에 mnt한 디렉터리를 지정하여 unmount
    ex.  `sudo unmount /mnt`
2. 확인
    - `df -h` 입력
3. AWS Console에서 해당 volume의 stat의 in-use -> available 변동

## 백업 이외의 Snapshot의 활용
- 스냅샷으로 EBS 볼륨 생성(다른 AZ에서도 생성 가능)
- AMI 생성  
※ 주의사항) Linux의 경우 HVM(t2 유형 등)이외에는 Kernel ID를 반드시 알고 있어야함. 밑에서 다시 설명
- 다른 Region으로 copy  
※ EBS volume 자체로는 다른 AZ로 이전할 수 없기 때문에 꼭 SNAPSHOT를 활용해야 한다.

## SNAPSHOT를 활용한 AMI 생성
* EBS SNAPSHOT으로 AMI를 생서할 때 주의 사항
- Linux의 경우 Kernel ID를 반드시 알고 있어야 한다. AMI를 만들 때, Kernel ID를 설정하게 되는데, 나중에 AMI로 EC2 Instance를 생성했을 때, Kernel ID가 맞지 않으면 부팅이 되지 않는다(Kernel Panic 발생). 단, HVM(t2 유형 등)은 Kernel ID를 설정하지 않아도 된다.
- Kernel ID 확인은 EC2 Instance의 Description에서 확인

## 요금
- 스냅샷 저장 요금은 S3 데이터 저장 요금에 합산




