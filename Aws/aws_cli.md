AWS CLIs
===

## aws s3 ls
- s3의 파일 목록 불러오기
ex. aws s3 ls s3://examplebucket10

## aws --region {region} dynamodb scan --table-name {table name}
- dynamo db의 테이블을 읽어오기
ex. aws --region ap-northeast-1 dynamodb scan --table-name record_table


## aws sts decode-authorization-message --encoded-message {encoded message}
- 아마존으로부터 받은 에러 메시지를 decode
ex. aws sts decode-authorization-message --encoded-message fwivJw....E9Q
=> Unable to locate credentials. You can configure credentials by running "aws configure".
