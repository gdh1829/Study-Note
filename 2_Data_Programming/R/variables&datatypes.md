Variables & Datatypes
===

## Variables
- 명명규칙
    - 사용가능한 문자: 알파벳, 숫자, 언더스코어(_), 마침표(.)
    - 하이폰(-) 금지 
    - 첫 글자는 알파벳 또는 마침표로 시작
    - 만약 첫 글자가 마침표라면 연이어 숫자 입력 불가
    - R 1.9.0 이전 버전에서는 변수명에 언더스코어를 사용할 수 없어, 대체로 마침표가 많이 사용되었다.
    >data_gender -> data.gender  # 객체 속성에 접근하는 코드가 아님!
- Assignment Operator
    - Assignment Operator: <-, <<-, =  
    - __Google's R Style Guide says "Use <-, not =, for assignment."__
    ```R
        #GOOD 
        x <- 5
        #BAD:
        x = 5
    ```

## Data Types
