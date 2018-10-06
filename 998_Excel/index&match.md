## MATCH Function
* 지정한 영역에서 찾은 값이 있는 행을 알려준다.
* syntax: MATCH(lookup_value, lookup_array, [match_type])
    - lookup_value: 원하는 값을 찾기 위한 키 값
    - lookup_array: 값을 찾을 영역
    - match_type: 1 - 보다 작음, 0 - 일치, 1 - 보다 큼

## INDEX Function
* 값을 찾을 영역에서 행번호와 열변호를 이용하여 값을 가져온다.
* syntax: INDEX(array, row_num, [column_num])
    - array: 값을 찾을 영역
    - row_num: 행번호
    - column_num: 열번호

## MIX of MATCH and INDEX
* vlookup만으로 찾을 수 없는 제한적 영역을 벗어나 데이터를 찾아올 수 있다.
* vlookup은 지정 영역의 mostleft 값을 기준으로 잡아야 하기 때문에, 제한이 크다. 
* 그렇기 때문에 데이터의 형태를 마음대로 하기엔 곤란한 경우, 좀 더 자유로운 match와 index의 mix는 좋은 대안이 된다.
* INDEX(array, MATCH(lookup_value, lookup_array, [match_type]), [column_num])


