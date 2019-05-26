IAM
===

- Identity and Access Management(식별 및 접근 관리)의 약어  
- Controls who is authenticated (signed in) and authorized (has permission) to use resources.  
- AWS account __root user__ is a single sign-in identity that has complete access to all AWS services and resources in the account.  
- 과금없음  
- Region 별로 설정할 수 없고, 모든 region에서 동일하게 작동  
- AWS 계정에는 다른 AWS 계정의 요금을 합쳐서 지불하는 통합 결제(Consolidated Billing) 기능이 존재  
- AWS 콘솔의 Billing&Cost Management에서 설정 가능.
- Payer Account가 AWS 리소스를 사용하는 Linked Account에 연결 요청을 보내는 방식  

## Features
- You can grant other people permission to administer and use resources in your AWS account without having to share your password or access key.  
- You can grant different permissions to different people for different resources.
- You can use IAM features to securely provide credentials for applications that run on EC2 instances which provide permissions for your applications to access other AWS resources.  
- You can add two-factor authentication to your account and to individual users for extra security.  
- You can allow users to use __identity federation__ to get temporary access to your AWS account.  
- You receive AWS CloudTrail log records that include information about __IAM identities__ who made requests for resources in your account.  
- You use an __access key__(an access key ID and secret access key) to make programmatic requests to AWS. An Access Key ID and Secret Access Key can only be uniquely generated once and must be regenerated if lost.    
- IAM has been validated as being compliant with Payment Card Industry (PCI) Data Security Standard (DSS).  
- IAM is _eventually consistent_. IAM achieves high availability by replicating data across multiple servers within Amazon's data centers around the world.  
- IAM and AWS Security Token Service (STS) are offered at no additional charge.  
- Your unique account sign-in page URL -> https://Your_AWS_Account_ID.signin.aws.amazon.com/console/  
- You can use IAM tags to add custom attributes to an IAM user or role using a tag key-value pair.  

## Users
- IAM USers
    - Instead of sharing your root user credentials with others, you can create individual __IAM Users__ within your account that correspond to users in your organization. IAM users are not seperate accounts; they are users within your account.
    - Each user can have its own password for access to the AWS Management Console. You can also create an individual access key for each user so that the user can make programmatic requests to work with resources in your account.
    - By default, a brand new IAM user has __NO permission__ to do anything.
    - Users are global entities.
- Federated Users
![IAM federated User](./images/IAM_federated_user.png)
    - If the users in your organization already have a way to be authenticated, you can federate those user identities into AWS.
- IAM Groups
    - An IAM group is a collection of IAM users.
    - You can organize IAM users into IAM groups and attach access control policies to a group.
    - A user can belong to multiple groups.
    - Groups cannot belong to other groups.
    - Groups do not have security credentials, and cannot access web services directly.
- IAM Role
    - A role does not have any credentials associated with it.
    - An IAM user can assume a role to temporarily take on different permissions for a specific task. A role can be assigned to a federated user who signs in by using an external identity provider instead of IAM.
    - __AWS service role__ is a role that a service assumes to perform actios in your account on your behalf. This service role must include all the permissions required for the service to access the AWS resources that it needs.
        - __AWS service role for an EC2 instance__ is a special type of service role that a service assumes to launch an EC2 instance that runs your application. This role is assigned to the EC2 instance when it is launched.
        - __AWS service-linked role__ is a unique type of service role that is linked directly to an AWS service. Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf.
    - An instance profile is a container for an IAM role that you can use to pass role information to an EC2 instance when the instance starts.
- Users or groups can have multiple policies attached to them that grant different permissions.

## AWS Security Token Service (STS)
- Create and provide trusted users with temporary security credentials that can control access to your AWS resources.
- Temporary security credentials are short-term and are not stored with the user but are generated dynamically and provided to the user when requested.
- By default, AWS STS is a global service with a single endpoint at https://sts.amazonaws.com

|When to Create IAM User| When to Create an IAM Role|
|---|---|
|You created an AWS account and you're the only person who works in your account|You're creating an application that runs on an EC2 instance and that application makes requests to AWS.|
|Other people in your group need to work in your AWS account, and your gorup is using no other identity mechanism.|You're creating an app that runs on a mobile phone and that makes requests to AWS.|
|You want to use the CLI to work with AWS.|Users in your company are authenticated in your corporate network and want to be able to use AWS without having no sign in again(federate into AWS)|

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
