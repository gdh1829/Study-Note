func tapply
================

apply - array
tapply - table
lapply - list
sapply - ?
mapply - matrix

## Syntax
> apply(array, margin, func)
* first arg - target object
* second arg - criteria
* third arg - function that you would like to apply
* 통계값을 간편하게 출력하기 위한 함수이다.

## Comparision: tapply() 
- Basic way to figure out mean value
```R
mtcars # built-in data.frame type data

class(mtcars)
str(mtcars)

newdata <- mtcars[1:2]
newdata
#                     mpg cyl
#Mazda RX4           21.0   6
#Mazda RX4 Wag       21.0   6
#Datsun 710          22.8   4
#Hornet 4 Drive      21.4   6
#Hornet Sportabout   18.7   8
#<skip>

newdata$cyl == 4
#[1] FALSE FALSE  TRUE FALSE FALSE FALSE FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE
#[20]  TRUE  TRUE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE FALSE FALSE FALSE  TRUE
newdata[2,]
newdata[,1:2]

index_cyl_eq_4=which(newdata$cyl==4) # which => tells indices of true location
index_cyl_eq_4
#  [1]  3  8  9 18 19 20 21 26 27 28 32
data_cyl_4 <- newdata[index_cyl_eq_4,]
data_cyl_4
index_cyl_eq_6=which(newdata$cyl==6)
data_cyl_6 <- newdata[index_cyl_eq_6,]
index_cyl_eq_8=which(newdata$cyl==8)
data_cyl_8 <- newdata[index_cyl_eq_8,]

mean(data_cyl_4$mpg) 
cbind(mean(data_cyl_4$mpg), mean(data_cyl_6$mpg), mean(data_cyl_8$mpg))
#         [,1]     [,2] [,3]
#[1,] 26.66364 19.74286 15.1
```
- tapply to figure out mean value
```R
# syntax
?tapply
tapply(newdata$mpg, newdata$cyl, mean) # same as cbind(mean(data_cyl_4$mpg), mean(data_cyl_6$mpg), mean(data_cyl_8$mpg))
#       4        6        8 
#26.66364 19.74286 15.10000
```
