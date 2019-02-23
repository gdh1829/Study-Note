data.frame
============================

name <- c('ko', 'ko1', 'ko2', 'ko3')
age <- c(19, 21, 23, 27)
sex <- c('female', 'male', 'female', 'male')
occu <- c('engineer', 'doctor', 'speaker', 'basketball player')

data.frame(name, age, sex, occu) # Excel과 같은 형태의 프레임으로 데이터 형태를 바꿔준다.
member <- data.frame(name, age, sex, occu) # Excel 형태의 데이터를 변수에 담기
member
  name age    sex              occu
1   ko  19 female          engineer
2  ko1  21   male            doctor
3  ko2  23 female           speaker
4  ko3  27   male basketball player
member[2] 
  age
1  19
2  21
3  23
4  27
member[2,]
  name age  sex   occu
2  ko1  21 male doctor
member[,2]
[1] 19 21 23 27
member$age # ${column name}
[1] 19 21 23 27
member[2,4]
[1] doctor
Levels: basketball player doctor engineer speaker

## update data

member
  name age    sex              occu
1   ko  19 female          engineer
2  ko1  21   male            doctor
3  ko2  23 female           speaker
4  ko3  27   male basketball player

member[2,3] <- "female"
member[2,3] # female

## Import data

with file path
read.table(file="file path") 
with file.choose
dataset <- read.table(file.choose(), header=TRUE) # text
dataset2 <- read.csv(file.choose(), header=T) #csv

head(dataset2)
tail(dataset2)
str(dataset2)
sum(dataset2$Count)