## R help script
?{keyword}
ex. ?plot

## R data type
numeric 
character
boolean

## Declare variables and insert values

Three ways
```R
x <- 1   # representative way in R
1 -> x
x = 1    # general programming languges
```
## insert multi values into single variable
```R
x <- 1,2,3 #NG
x <- (1,2,3) #NG
x <- c(1,2,3) #OK
```
## How multi value variables work in arithmetic operations
```R
x <- c(1,2,3) 
y <- c(2,3,4)
x*y   # c(2,6,12)

x <- c(1,2,3) 
y <- 3
x*y     # c(3,6,9)

x <- c(1,2,3) 
y <- c(2,3)
x*y     # NG
    Warning message:
    In x * y : longer object length is not a multiple of shorter object length

x <- c(1,2,3,4,6)
y <- c('1','2','3','4','5')
x*y #NG
    Error in x * y : non-numeric argument to binary operator
```
## How to check out length of variables
```R
x <- c(1,2,3) 
length(x)  # 3

x <- c(20:50) # add values from 1 to 100
 [1] 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
 [21] 40 41 42 43 44 45 46 47 48 49 50

[] : index of array
x[2] # 21
x[2:5] # [1] 21 22 23 24
※ Unlike general programming langugues, array index of R starts with 1
```
## How to figure out data type - built-in function called "str"
```R
x <- 1
str(x)  # num 3

x <- 'cat'
str(x)  # chr "cat"
x <- "cat"
str(x)  # chr "cat"

x <- c(1,2,3,4,6)
str(x)  # num [1:5] 1 2 3 4 6
        # [1:5] => 1: single line
        # [1:5] => 5: length

y <- c('1','2','3','4','5')
str(y)  # chr [1:5] "1" "2" "3" "4" "5"
```
## logical operation
```R
x <- c(1,2,3,4,6)
y <- c('1','2','3','4','5')
x==y #true true true true false
Be catious, in logical operations in R, 1 == '1', true 
```

## basic built-in functions related to stastics
```R
sum() # total
mean() # average
max()  # maximum
min()  # minimum 

y <- c('1','2','3','4','5')
sum(y) #NG
Error in sum(y) : invalid 'type' (character) of argument

x <- c(3,10,99,0,6)

sum(x) # 118
mean(x) # 23.6
max(x)  # 99
min(x)  # 0
```

## 
```R
x <- c(3,10,99,0,6,-1, -10, 5, 50, 77)
x>50 # [1] FALSE FALSE TRUE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
x[x>50]   # [1] 99 77
          # [x>50] : if the logical operation 'x>50' is inside of square brackets, it returns an index number
sum(x>50) # [1] 2 : number of true
          # false == 0, true == 1
sum(x[x>50]) # [1] 176
which(x>50)  # [1] 3 10
             # which built-in function returns index numbers
```

## install and use libraries
```R
install.packages("{library name}")  #install library
library("{library name}") # use library
```

## 반복 데이터, 일정한 구조/순차 데이터 생성
R에서 데이터를 입력할 때 c()를 사용하는데, 일정한 반복이나 규칙을 따르는 데이터를 입력을 돕는다.
- **rep()**
```R
rep("sample",  times=5)
# [1] "sample" "sample" "sample" "sample" "sample"

rep(c("a", "b"), times=3)
# [1] "a" "b" "a" "b" "a" "b"

rep(c("a", "b"), c(3, 5))
# [1] "a" "a" "a" "b" "b" "b" "b" "b"

rep(1:3, each=3)
# [1] 1 1 1 2 2 2 3 3 3
```

- **rep()** 행렬에 대하여
```R
x <- c(1:6)
y <- rep(1, times=6)
z <- rep(c(1,2), c(3,3))
xyz <- data.frame(cbind(x,y,z))
xyz
#  x y z
#1 1 1 1
#2 2 1 1
#3 3 1 1
#4 4 1 2
#5 5 1 2
#6 6 1 2
xyz$seq_no_1 <- rep(c(1:2), len=nrow(xyz))
xyz
#  x y z seq_no_1
#1 1 1 1        1
#2 2 1 1        2
#3 3 1 1        1
#4 4 1 2        2
#5 5 1 2        1
#6 6 1 2        2
seq_no_2 <- rep(c(1:2), len=nrow(xyz))
xyz <- cbind(xyz, seq_no_2)
xyz
#  x y z seq_no_1 seq_no_2
#1 1 1 1        1        1
#2 2 1 1        2        2
#3 3 1 1        1        1
#4 4 1 2        2        2
#5 5 1 2        1        1
#6 6 1 2        2        2
```

- **seq()**: 일정한 구조/순차 데이터 생성
```R
c(1:10)
# [1]  1  2  3  4  5  6  7  8  9 10
seq_len(10)
# [1]  1  2  3  4  5  6  7  8  9 10
seq(from=1, to=10) # from, to param name 생략 가능
# [1]  1  2  3  4  5  6  7  8  9 10
seq(1, 10, by=2) # 숫자간 간격 2
# [1] 1 3 5 7 9
seq(to=10, by=2) # 이 경우 to는 생략 불가. 첫번째 10이 무엇을 의미하는지 불명해지기 때문
# [1] 1 3 5 7 9
seq(1, 10, length=5) # 1부터 10까지의 수를 5개의 숫자로 등간격으로 순차 데이터 생성(숫자는 5개, 구간은 4개)
# [1]  1.00  3.25  5.50  7.75 10.00
seq(1, 2, length.out=10) # length.out: 개수의 지정
# [1] 1.000000 1.111111 1.222222 1.333333 1.444444 1.555556 1.666667 1.777778 1.888889 2.000000
```







