Shell script Array
==========================
쉘 스크립트는 복잡한 데이터 구조를 사용할 수는 없지만, bash에서 1차원 배열은 사용 가능
배열을 참조할 때는 {}가 필요

## Craeting arrays
There is no maximum limit to the size of an array, nor any requiredment that member variables be indexed or assigned contigously.  
Arrays are zero-based: the first element is indexed with the number 0.  
> Array[INDEX]=value  

Array variables may also be created using compound assignments in this format.  
> Array=(value1 value2 value3 ... valueN)

## Adding extra or missing members in an array
```Bash
Array=()
Array+=("variable") # puts a new element at the end of the array
Array[1]="memeber" # puts a new element in 1 index of the array
```

## Refering the content of an item in an array
Use curly braces.
```Bash
#!/bin/bash
app=("grep" "awk" "cut" "tr" "sed") 
echo ${app[3]} # outputs a corressponding element
echo "${#app[@]}" # outputs size of the array
echo ${#app[*]} # as same as the above
echo ${app[@]} # outputs all of elements: "grep" "awk" "cut" "tr" "sed"
echo ${app[*]} # same output as ${app[@]}: "grep" "awk" "cut" "tr" "sed"
```

## Deleting array variables
uses **unset** built-in keyword to destroy or a member variable of an array.
```Bash
unset ARRAY[1] # delete an element of Array
unset ARRAY # delete Array itself
```

## Looping array
```Bash
for i in ${ARRAY[@]}; do
    COMMANDS
done
```