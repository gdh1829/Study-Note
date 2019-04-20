IAM
===

- Identity and Access Management(식별 및 접근 관리)의 약어  
- 사용자와 그룹을 생성하고 AWS의 각 리소스에 대해 접근 제어와 권한 관리를 제공  
과금없음  
- Region 별로 설정할 수 없고, 모든 region에서 동일하게 작동  
- AWS 계정에는 다른 AWS 계정의 요금을 합쳐서 지불하는 통합 결제(Consolidated Billing) 기능이 존재  
- AWS 콘솔의 Billing&Cost Management에서 설정 가능.
- Payer Account가 AWS 리소스를 사용하는 Linked Account에 연결 요청을 보내는 방식  

## IAM Role
- IAM 그룹과 사용자에게 권한을 설정하는 것과 달리 EC2 인스턴스 전용으로 권한 설정을 할 수 있음. 
- 이를 IAM Role이라고 하며, EC2 인스턴스뿐만 아니라 다른 AWS 계정(또는 다른 AWS계정의 IAM 사용자), Facebook, Google, Amazon 계정 전용으로 권한 설정도 가능
- EC2인스턴스에서 API로 AWS Resource에 접근하려면 항상 엑세스 키와 시크릿 키를 설정해야만 한다. Auto Scaling 기능으로 EC2 인스턴스를 자동으로 늘려나갈 때 엑세스 키와 시크릿 키를 일일이 설정해주려면 상당히 번거롭다. 이런 부분을 따로 자동화하지 않아도 IAM Role을 사용하면 EC2 인스턴스 생성 즉시 API로 AWS Resource에 접근할 수 있다.

## IAM Role
IAM roles are a secure way to grant permissions to entities that you trust. Examples of entities include the following:
- IAM user in another account
- Application code running on an EC2 instance taht needs to perform actions on AWS resources
- An AWS service that needs to act on resources in your account to provide its features
- Users from a corporate directory who use identity federation with SAML
IAM roles issue keys that are valid for short durations, making them a more secure way to grant access

## IAM Role 주의사항
- EC2 Instance 전용 IAM Role은 EC2 인스턴스를 생성할 때 설정해줘야 한다. 이미 만들어진 EC Instance에 IAM Role을 설정할 수는 없음
- EC2 생성시에 role로서 s3 full access를 갖고 있도록 설정하였다면, 해당 EC2 instance 내부에서 aws s3 cli를 통하여 접근이 가능하게 되는 것. 생성시 IAM role를 사용하도록 설정하였기 때문에, access key와 secret key를 따로 설정하지 않아도 aws s3 명령이 잘 동작하는 것.
- EC2 instance에서 IAM role를 사용 중에 있을 때, IAM role 삭제를 하면, 그 즉시 해당 instance는 AWS Resource 접근 권한이 사라지게 되므로 주의.
- 권한이 없는 경우 xxx is not authorized to perform 관련 에러가 발생

## 기타 기능
- Identity Providers: SAML Provider를 생성
- Password Policy: IAM 사용자의 비밀번호 정책을 설정. 대소문자, 숫자, 특수문자 포함 여부를 설정할 수도 있고, IAM 사용자가 자기 자신의 비밀번호를 변경하는 것을 허용할지 등 설정가능.
- MFA : IAM 사용자가 로그인할 때 비밀번호와 OTP(One time password)를 동시에 사용하도록 설정하여 보안성을 높이는 설정. 
