CIDR expression
===

## x.x.x.x/32
- denotes one IP address
- example
    - You're instructed to set up a Linux bastion host. It will allow access to the Amazon EC2 instances running in their VPC. For security purposes, only the clients connecting from the corporate external public IP address 175.45.116.100 should have SSH access to the host.
    - Your Action -> Security Group Inbound Rule: Protocol - TCP, Port Range - 22, Source 175.45.116.100/32

## x.x.x.x/0
- refers to the entire network

## SSH protocol uses TCP and port 22,  not UDP
## Network ACLs act as a firewall for your whole VPC subnet, while security groups operate on an instance level. Since you're securing an EC2 instance, you should be using security groups.