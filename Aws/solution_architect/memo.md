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

