## 아마존 서버 간 파일 카피
    * s3 명령 집합에는 cp, mv, ls 및 rm이 포함되며 이러한 명령은 해당 Unix 명령과 유사한 방식으로 작동
    * examples
        // Copy MyFile.txt in current directory to s3://my-bucket/path
        $ aws s3 cp MyFile.txt s3://my-bucket/path/

        // Move all .jpg files in s3://my-bucket/path to ./MyDirectory
        $ aws s3 mv s3://my-bucket/path ./MyDirectory --exclude '*' --include '*.jpg' --recursive

        // List the contents of my-bucket
        $ aws s3 ls s3://my-bucket

        // List the contents of path in my-bucket
        $ aws s3 ls s3://my-bucket/path/

        // Delete s3://my-bucket/path/MyFile.txt
        $ aws s3 rm s3://my-bucket/path/MyFile.txt

        // Delete s3://my-bucket/path and all of its contents
        $ aws s3 rm s3://my-bucket/path --recursive




