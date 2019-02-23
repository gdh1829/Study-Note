Creating ami
===

1. temporarly added aws keys to env variable.
export AWS_ACCESS_KEY=xxxxxxxxxxxxx
export AWS_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxx

2. checks whether the same name(ami) is already existed
ec2-describe-images --filter "name=xxx"

3. necessary chef Node existence check

4. running a temporary instance. ami는 이미지이기 때문에, 이미지란 실제 ec2를 본떠서 이미지화 시킨 것이기 때문에, 당연히 ami를 만들기 위해서는 이미지를 뜨기 위한 instance가 존재해야하는 것. ami가 작성이 완료되면 다시 terminate시키면 된다.  
[ec2 run-instances command reference](https://docs.aws.amazon.com/ko_kr/cli/latest/reference/ec2/run-instances.html)  
ec2-run-instances --image-id ami-xxxxxx --key-name xxx-ec2-key -p xxx-default-role --block-device-mappings "/dev/sdf=snap-xxxxxx" --instance-type t2.small --subnet-id subnet-xxxxxx --security-group-ids sg-xxxxxxx --availability-zone ap-northeast-1b --associate-public-ip-address true

5. create tag
ec2-create-tags $INSTANCE_ID -t Name=prepare -t Type=$NODE -t Version=$VERSION -t xxx-Service=Proto

6. instance가 완전히 만들어질 때까지 대기
ec2-describe-instances $INSTANCE_ID | grep INSTAN | cut -f6 를 통해서 pending이 끝날때까지 작업을 sleep

7. instance가 pending이 완료되면 해당 instance의 Ip를 받아내어 커넥션 테스팅 실시.(instance가 만들어지고 여러가지 software 설정을 하기 위해서 접속이 가능해야 하므로, 본격 작업 전 커넥션 테스트)
Testing connection  
ec2-describe-instances $INSTANCE_ID | grep INSTAN | cut -f4

8. Running Chef 
knife solo bootstrap ec2-user@$INSTANCE_IP -i ~/.ssh/xxx.pem nodes/$NODE-$VERSION.json || exit -1  
[knife-solo reference](https://github.com/matschaffer/knife-solo/blob/master/README.rdoc)

9. Creating Image
//create image  
ec2-create-image -n "$NODE $VERSION $IMAGE_EXTRA" -d "$NODE Base $DATE" $INSTANCE|cut -f2  
//check whether the created image is available  
ec2-describe-images $AMI |grep IMAGE|cut -f5  

10. Terminate the instance
ec2-terminate-instances $INSTANCE_ID  


