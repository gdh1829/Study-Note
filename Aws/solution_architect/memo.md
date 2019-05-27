ASG
===

Scaling based on a schedule allows you to scale your application in response to predictable load changes.  
ex) Every week the traffic to your web application starts to increase on Wednesday, remains high on Thursday, and starts to decrease on Friday. 
You can plan your scaling activities based on the predictable traffic patterns of your web application.

To configure your ASG to scale based on a schedule, you create a scheduled action. The scheduled action tells Amazon EC2 Auto Scaling to perform a scaling action at specified times.

You can create scheduled actions for scaling one time only or for scaling on a recurring schedule.

IAM
===
You can authenticate to your DB instance using AWS Identity and Access Management(IAM) database authentication. IAM database authentication works with MySQL and PostgreSQL. With this authentication method, you don't need to use a password when you connect to a DB instance. Instead, you use an authentication token.  

An authentication token is a unique string of characters that Amazon RDS generates on request. Authentication tokens are generated using AWS Signature Version 4. Each token has a lifetime of 15 minutes. You don't need to store user credentials in the database, because authentication is managed externally using IAM. You can also still use standard database authenticaiton.

IAM database authentication provides the following benefits:
    1. Network traffic to and from database is encrypted using Secure Sockets Layer(SSL).
    2. You can use IAM to centrally manage access to your database resources, instead of managing access individually on each DB instance.
    3. For applications running on Amazon EC2, you can use profile credentials specific to your EC2 instance to access your database instead of a password, for greater security.

Security Group
===
A _security group_ acts as a virtual firewall for your instance to control inbound and outbound traffic. When you launch an instance in a VPC, you can assign up to five security groups to the instance. Security groups act at the instance level, not the subnet level. Therefore, each instance in a subnet in your VPC could be assigned to a different set of security groups. If you don't specify a particular group at launch time, the instance is automatically assigned to the default security group for the VPC.
When you add or remove rules, those changes are automatically applied to all instances to which you've assigned the security group. 

Best way to  encrypt sensitive environment variables like API credentials or storing sensitive database that Lambda function has
===
- Create a new KMS key and use it to enable encryption helpers that leverage on AWS Key Management Service to store and encrypt the sensitive information.
- When you create or update Lambda functions that use environment variables, AWS Lambda encrypts them using the AWS Key Management Service. When your Lambda function is invoked, environment variables of Lambda are decrypted and made available to the Lambda code.
- The first time you create or update Lambda functions that use environment variables in a region, a default service key is created for you automatically within AWS KMS. This key is used to encrypt environment variables after your Lambda function is created, you must create your own AWS KMS key and choose it instead of the default key. The default key will give errors when chosen. Creating your own key gives you more flexibility, including the ability to create, rotate, disable, and define access controls, and to audit the encryption keys used to protect your data.
- Lambda does not encrypt environment variables by default during the deployment process. When you deploy your Lambda function, all the environment variables you've specified are encrypted by default after, but not during, the development process.

Lambda@Edge
===
- Lets you run Lambda functions to customize content that CloudFront delivers, executing the functions in AWS locations closer to the viewer. The functions run in response to CloudFront events, without provisioning or managing servers.  
- You can use Lambda functions to change CloudFront requests and responses at the following points:
![Lambda Edge](../images/lambda_edge.png)
    - After CloudFront receives a request from a viewer (viewer request)
    - Before CloudFront forwards the request to the origin (origin request)
    - After CloudFront receives the response from the origin (origin response)
    - Before CloudFront forwards the response to the viewer (viwer response)
- You can automate your serverless application's release process using AWS CodePipeline and AWS CodeDeploy.
- Lambda will automatically track the behavior of your Lambda function invocations and provide feedback that you can monitor. In addition, it provides metrics that allows you to analyze the full function invocation spectrum, including event source integration and whether downstream resources perform as expected.

## Bring on-premises network to AWS
- You can bring part or all of your public IPv4 address range from your on-premises network to your AWS account. You continue to own the address range, but AWS advertises it on the internet. After you bring the address range to AWS, it appears in your account as an address pool. You can create an Elastic IP address from your address pool and use it with your AWS resources, such as EC2 instances, NAT gateways, and Network Load Balancers. This is also called "`Bring Your Own IP Addresses (BYOIP)`".
- To ensure that only you can bring your address range to your AWS account, you must authorize Amazon to advertise the address range and provide proof that you own the address range.
- A __Route Origin Authorization (ROA)__ is a document that you can create through your Regional Internet Registry (RIR), such as the American Registry for Internet Numbers (ARIN) or Réseaux IP Européens Network Coordination Centre (RIPE). It contains the address range, the ASNs that are allowed to advertise the address range, any an expiration date
- The ROA authorizes Amazon to advertise an address range under a specific AS number. However, it does not authorize your AWS account to bring the address range to AWS. To authorize your AWS account to bring an address range to AWS, you must publish a self-signed X509 certificate in the RDAP remarks for the address range. The certificate contains a public key, which AWS uses to verify the authorization-context signature that you provide. You should keep your private key secure and use it to sign the authorization-context message.

S3 Storage Classes
===
- S3 Standard: General purpose
- S3 Intelligent-Tiering: Unknown or chaning access
- S3 Standard-Infrequent Access (S3 Standard-IA): Infrequent access
- S3 Zone-Infrequent Access (S3 One Zone-IA): Infrequent access, non-critical data
- S3 Glacier: Archive
- S3 Glacier Deep Archive: Archive, lowest-cost 

S3 Intelligent-Tiering
===
![S3 Intelligent-Tiering](../images/S3_INT.png)
- a New Amazon S3 Storage Class designed for customers who want to optimize storage costs automatically when data access patterns change, without performance impact or operational overhead. S3 Intelligent-Tiering is the first cloud object storage class that delivers automatic cost savings by moving data between two access tiers --frequent access and infrequent access-- when access pattern change, and is ideal for data with unknown or changing access patterns.
- S3 Intelligent-Tiering stores objects in two access tiers:
    -  one tier that is optimized for frequent access and another lower-cost tier that is optimized for infrequent access.
    - For a small monthly monitoring and automation fee per object, S3 Intelligent-Tiering monitors access patterns and moves objects that have not been accessed for 30 consecutive days to the infrequent access tier. There are no retrieval fees in S3 Intelligent-Tiering.
    - If an object inthe infrequent access tier is accessed later, it is automatically moved back to the frequent access tier. No additional tiering fees apply when objects are moved between access tiers within the S3 Intelligent-Tiering storage class. S3 Intelligent-Tiering is designed for 99.9% availability and 99.999999999% durability, and offers the same low latency and high throughput performance of S3 Standard.
- Amazon S3 features including S3 Object Tagging, S3 Cross-Region Replication, and S3 Select all work with S3 Intelligent-Tiering. Customers can start using S3 Intelligent-Tiering through the S3 API, CLI, and management console by putting objects directly into S3 Intelligent-Tiering or by using a S3 Lifecycle policy to move objects from S3 Standard or S3 Standard-IA to S3 Intelligent-Tiering. Customers can also archive obejcts with a S3 Lifecycle policy from S3 Intelligent-Tiering into Amazon S3 Glacier.
- S3 Intelligent-Tiering charges a small tiering fee and has a minimum eligible object size of 128KB for auto-tiering. Smaller objests may be stored but will always be charged at the Frequent Access tier rates.

## how to ensure data security
- You can secure the privacy of your data in AWS, both at rest and in-transit, through encryption.
- If your data is stored in EBS volume, you can enable EBS Encryption.
- If it is stored on Amazon S3, you can enable client-side and server-side encryption.
※ There is no such thing as On-Premises Data Encryption for S3 and EBS as these services are in the AWS cloud and not on your on-premises network.

## Amazon DynamoDB Accelerator (DAX)
![DynamoDB DAX](../images/dynamoDB_DAX.png)
- a fully managed, highly available, in-memory cache that can reduve Amazon DynamoDB response times from milliseconds to microseconds, even at millions of requests per second.
- Although you may use ElasticCache as your database cache, it will not reduve the DynamoDB response time from milliseconds to microseconds as compared with DynamoDB DAX.
- With Amazon EBS, you can use any of the standard RAID configurations that you can use with a traditional bare metal server, as long as that particular RAID configuration is supported by the operating system for your instance. This is because all RAID is accomplished at the software level. For greater I/O performance than you can achieve with a single volume, RAID 0 can stripe multiple volumes together; for on-instance redundancy, RAID 1 can mirror two volumes together.

## HVM AMI
- is required to take advantage of enhanced networking and GPU processing. 
- In order to pass through instructions to specialized network and GPU devices, the OS needs to be able to have access to the native hardware platform which the HVM virtualization provides.
- Although the enhanced networking feature can provide higher I/O performance and lower CPU utilization to your EC2 instance, you have to use an HVM AMI instead of PV AMI.

## How to increase the write performance of the database hosted in an EC2 instance.
- You can achieve this by either setting up a standard RAID 0 configuration or simply by increasing the size of the EC2 instance.
- Some EC2 instance types can drive more I/O throughput than what you can provision for a single EBS volume. You can join multiple gp2, io1, st1, or sc1 volumes together in a RAID 0 configuration to use the available bandwidth for these instances.

## Redundant Array of Inexpensive Disks (RAID)
- 여러 개의 디스크를 배열하여 속도의 증대, 안정성의 증대, 효율성, 가용성의 증대를 하는데 쓰이는 기술
- 종류와 구성방식
    - RAID 0
        - Concatenate 방식: 두개 이상의 디스크에 데이터를 순차적으로 쓰는 방법
        - Stripe 방식: 두개 이상의 디스크에 데이터를 랜덤하게 쓰는 방법
        - more suitable option for providing faster read and write operations, compared with RAID 1
    - RAID 1 (Mirror)
        - 볼륨 내의 패리티를 사용하지 않고 디스크에 같은 데이터를 중복 기록하여 데이터를 보존하게 되며, 적어도 동일한 용량의 디스크가 두 개가 필요.
        - provide mirroring redundancy, and fault-tolerance
    - RAID 2
        - RAID 0처럼 striping 방식이지만 에러 체크와 수정을 할 수 있도록 Hamming code를 사용하고 있는 것이 특징
        - 하드 디스크에서 ECC(Error Correction Code)를 지원하지 않기 때문에 ECC를 별도의 드라이브에 저장하는 방식으로 처리
        - 하지만 ECC를 위한 드라이브가 손상될 경우는 문제가 발생할 수 있으며 패리티 정보를 하나의 하드 드라이브에 저장하는 RAID 4가 나오면서 거의 사용되지 않는 방식
    - RAID 3, 4
        - RAID 0, 1의 문제점을 보완하기 위한 방식으로 3, 4로 나뉘긴 하지만 구성 방식은 거의 같다. RAID 3, 4는 기본적으로 RAID 0과 같은 striping 구성을 하고 있어 성능을 보완하고 디스크 용량을 온전히 사용할 수 있게 해주는데 여기에 추가로 에러 체크 및 수정을 위해서 패리티 정보를 별도의 디스크에 따로 저장
        - RAID 3은 데이터를 바이트 단위로 나누어 디스크에 동등하게 분산 기록, RAID 4는 데이터를 블록 단위로 나눠 기록하므로 완벽하게 동일하진 않다는 차이가 있다.
        - RAID 3은 드라이브 동기화가 필수적이라 많이 사용되지 않고 RAID 4를 더 많이 쓴다
    - RAID 5
        - RAID 3, 4에서 별도의 패리티 정보 디스크를 사용함으로써 발생하는 문제점을 보완하는 방식으로 패리티 정보를 stripe로 구성된 디스크 내에서 처리하게 만듦.
        - 만약 1개의 하드가 고장나더라도 남은 하드들을 통해 데이터를 복구 할 수 있다는 장점
    - RAID 6
        - RAID 5와 같은 개념이지만 다른 드라이브들 간에 분포되어 있는 2차 패리티 정보를 넣어 2개의 하드에 문제가 생겨도 복구할 수 있게 설계되었으므로 RAID 5보다 더욱 데이터의 안전성을 고려하는 시스템에서 사용.

## Amazon HSM 
- a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud.
- With CloudHSM, you can manage your own encryption keys using FIPS 140-2 Level 3 validated HSMs.
## Amazon KMS (Key Management Service)
## OLAP (Online Analytical Processing)
- Redshift
## Terminology
- SIT: System Integration Testing, is part of Functional Testing
- UAT: User Acceptance Testing, is part of Functional Testing
- DEV: development
- PROD : production
## Amazon Athena
- a service that enables a data analyst to perform interactive queries in the AWS on data stored in Amazon S3.
- Athena is a serverless query service, an analyst doesn't need to manage any underlying compute infrastructure to use it.
- There is also no need to load S3 data into Amazon S3 or transform it for analysis, which makes it easier and faster for an analyst to gain insight

