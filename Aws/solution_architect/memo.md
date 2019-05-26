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

## Amazon KMS (Key Management Service)
## OLAP (Online Analytical Processing)
- Redshift
## Terminology
- SIT: System Integration Testing, is part of Functional Testing
- UAT: User Acceptance Testing, is part of Functional Testing
- DEV: development
- PROD : production

