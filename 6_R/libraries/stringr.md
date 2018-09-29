stringr library
=============================

install.packages("stringr")
library("stringr")

## str_count function
- grep과 비슷하지만 매칭 데이터의 카운트를 output

- prepares sample data
>mtcars
>rowcas <- rownames(mtcars)

- looks for data that includes a character "t" and output its count in each index 
>str_count(rowcars, "t")
- [1] 0 0 1 1 3 1 1 0 0 0 0 0 0 0 1 2 0 1 0 1 1
- [22] 0 0 0 1 1 0 1 1 0 1 0
>str_count(tolower(rowcars), "toyota")
- [1] 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1
- [22] 0 0 0 0 0 0 0 0 0 0 0
>sum(str_count(tolower(rowcars), "toyota"))
- [1] 2
- 찾은 카운트들의 합을 알려준다.
- 데이터 안에서 원하는 문자열이 얼마나 쓰이고 있는지 확인할 때 유용