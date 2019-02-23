sed
==========================
In writing...

https://www.thegeekstuff.com/2009/09/unix-sed-tutorial-printing-file-lines-using-address-and-patterns/

# 삭제

## sed -e 'd' /etc/service
- /etc/service를 읽어들이며 모든 라인에 대하여 delete를 수행한다.

## sed -e '1d' /etc/service
- 첫번째 라인만 delete를 수행한다.

## sed -e '1,10d' /etc/service
- 첫번째부터 10번째 라인에 대하여 delete를 수행한다.

# 치환

## sed -e s/1234/xxxx/g sample.txt
- 모든 1234를 xxxx로 치환한다.

## sed -e `1,10s/1234/xxxx/g` sample.txt
- 첫번째부터 10번째 라인에 대하여 1234를 xxxx로 치환한다.

## sed -e 's:/usr/local:/usr:g' sample.txt
- sed -e 's/\/usr\/local/\/usr/g' sample.txt와 같다.
- 지저분한 백 슬래쉬를 :로 깔끔하게 작성 가능

## sed -i 's/World/Docker/' *.py
- 확장자가 py인 모든 파일의 내부에 World를 Docker로 치환한다.
