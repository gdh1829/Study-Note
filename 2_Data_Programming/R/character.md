character
=====================

```R
x <- character()
x2 <- ""
class(x) # "character"
class(x2) # "character"

length(x) # 0
- character()로 할당된 변수의 길이는 0
length(x2) # 1
- <주의> ""로 할당된 변수의 길이는 1

x <- character(10)
x[13] <- "Thirteen" # OK
- 단, x[11]과 x[12]의 값은 NA가 됨

x <- 1
x2 <- "1"
is.character(x) #TRUE
is.character(x2) #FALSE

class(x) #numeric
class(x2) #character

as.character(x) # "1"
- 단, x의 value를 바꿔버리는 것이 아닌 새로운 value로 output하기 때문에 다시 x를 출력해보면 숫자 1이 character "1"로 바뀌어 있지는 않음.

x <- c(1:5)
- 데이터 형은 numberic
x2 <- c(1:5, "apple")
- "1" "2" "3" "4" "5" "apple"
- class(x2) 역시 "character"가 출력됨.
- 데이터 형은 character로서 끝의 apple이 character형이기 때문에 character로 통일의 되어 출력됨

x <- c(1:5, TRUE, FALSE)
class(x) # "integer"
x
- 1 2 3 4 5 1 0
- TRUE와 FALSE는 각각 1과 0으로 출력됨.
- 만약 그 끝에 다시 문자열 "a"를 넣는다면? x <- c(1:5, TRUE, FALSE, "a")
- 결과는 "1" "2" "3" "4" "5" "TRUE" "FALSE" "a"

- data frame에서 데이터 형 변환에 대해 알아보자
df1 <- data.frame(column1=c(1:3), column2=c("a", "b", "c"))
df1
-  column1 column2
- 1       1       a
- 2       2       b
- 3       3       c
str(df1)
- 'data.frame':	3 obs. of  2 variables:
- $ column1: int  1 2 3
- $ column2: Factor w/ 3 levels "a","b","c": 1 2 3
df1[3,1] <- "aaa"
- column1의 세번째 값을 3에서 character "aaa"로 바꿔보았다.
df1
-  column1 column2
- 1       1       a
- 2       2       b
- 3     aaa       c
- df1의 출력에서는 데이터 형에 관계 없이 보여주기 때문에 column1의 첫째와 둘째가 그대로 numeric 1과 2처럼 보인다. 하지만!
str(df1)
- 'data.frame':	3 obs. of  2 variables:
- $ column1: chr  "1" "2" "aaa"
- $ column2: Factor w/ 3 levels "a","b","c": 1 2 3
- structure함수를 이용해보면 column1의 데이터형이 int에서 chr로 바뀐것을 알 수 있다.
```
## paste function
```R
x <- paste("pine", "apple") # "pine apple"
- default seperator가 공백이기 때문에 character끼리 스페이스로 자동 구분됨

x <- paste("pine", "apple", sep="")
- seperator를 ""과 같이 공백 없이 설정하면?
- output: "pineapple"

x <- paste(1, 1:5, sep="-")
- output: 1-1 1-2 1-3 1-4 1-5
```
## noquote function
```R
a <- paste("The value of 'pi' is", pi, "!!")
- output: [1] "The value of 'pi' is 3.14159265358979 !!"
noquote(a)
- output: [1] The value of 'pi' is 3.14159265358979 !!
- double quotation mark없이 출력
- print(a, quote=FALSE)와 같음
```
## character의 길이 함수: nchar function
```R
>mtcars # R에 있는 기본 제공형 table형 샘플 데이터
>rowcars <- rownames(mtcars)
- rownames() : table의 row 이름 list를 가져온다
```
## colnames(mtcars)
```R
- column 이름 list
>rowcars
>nchar(rowcars) # rownames의 각각 길이를 출력
>which(nchar(rowcars) == max(nchar(rowcars)))
- rowcars의 nchar중 max값의 table index를 리턴
- output: 16
> rowcars[which(nchar(rowcars) == max(nchar(rowcars)))]
- [1] "Lincoln Continental"
```
## grep function
```R
- 샘플 데이터 준비
>mtcars
>rowcars <- rownames(mtcars)

>grep("z", mtcars)
- mtcars와 같은 frame형에는 NG
>grep("z", rowcars)
- c("a", "b")형태에는 OK
- index가 출력
>grep("z", rowcars, value=TRUE)
- value=TRUE : index가 아닌 value를 출력해줌
- default는 FALSE이므로 value=FALSE를 생략해도 되고, 명시적으로 입력해도 OK
>grep("[tT]", rowcars, value=TRUE)
>grep("toyota|Toyota", rowcars, value=TRUE)
- 정규표현식 형태로 원하는 character 검색도 가능

>grep("TOYOTA", toupper(rowcars), value=TRUE)
- toupper()함수를 이용하여 샘플 데이터를 모두 대문자로 바꾸고 TOYOTA검색
- output: [1] "TOYOTA COROLLA" "TOYOTA CORONA"
```