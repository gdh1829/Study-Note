## R data type
number 
character: '' or ""

## Declare variables and insert values

Three ways
x <- 1   # representative way in R
1 -> x
x = 1    # general programming languges

## insert multi values into single variable

x <- 1,2,3 #NG
x <- (1,2,3) #NG
x <- c(1,2,3) #OK

## How multi value variables work in arithmetic operations

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

## How to check out length of variables

x <- c(1,2,3) 
length(x)  # 3

x <- c(20:50) # add values from 1 to 100
 [1] 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39
 [21] 40 41 42 43 44 45 46 47 48 49 50

[] : index of array
x[2] # 21
x[2:5] # [1] 21 22 23 24
※ Unlike general programming langugues, array index of R starts with 1

## How to figure out data type - built-in function called "str"

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

## logical operation

x <- c(1,2,3,4,6)
y <- c('1','2','3','4','5')
x==y #true true true true false
Be catious, in logical operations in R, 1 == '1', true 

## basic built-in functions related to stastics

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

## 

x <- c(3,10,99,0,6,-1, -10, 5, 50, 77)
x>50 # [1] FALSE FALSE TRUE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
x[x>50]   # [1] 99 77
          # [x>50] : if the logical operation 'x>50' is inside of square brackets, it returns an index number
sum(x>50) # [1] 2 : number of true
          # false == 0, true == 1
sum(x[x>50]) # [1] 176
which(x>50)  # [1] 3 10
             # which built-in function returns index numbers

## install and use libraries
```R
install.packages("{library name}")  #install library
library("{library name}") # use library
```







