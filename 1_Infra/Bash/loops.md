Loop
===

## While Loops
```bash
#!/bin/bash
# Basic while loop
counter=1
while [ $counter -le 10 ]; do
    echo $counter
    ((counter++))
done
echo All done
```

## Until Loops
While loop와 작동이 거의 같다. Until이 있는 이유는 좀 더 직관적으로 while loop에서의 expression보다 until loop에서의 expression이 더 이해하기 쉽다면 당연히 until을 쓰는게 좀 더 clean, obvious and elegant 코드가 될 수 있을 것.
```bash
#!/bin/bash
# Basic until loop
counter=1
until [ $counter -gt 10 ]; do
    echo $counter
    ((counter++))
done
echo All done
```

## For Loops
```bash
#!/bin/bash
# Basic for loop
names='Ko1 Ko2 Ko3'
for name in $names; do
    echo $name
done
echo All done
```
- 다음은 curly brack안에 range지정을 통한 for loop 실행이다.  
range 지정 시, starting value > ending value => it will count down.
```bash
#!/bin/bash
# from 1 to 5 range in for loop
for value in {1..5}; do # curly bracket, {}의 표현식에서 white space is not allowed.
    echo $value
done
echo All done
```
- curly bracket의 range 지정에서 끝에 '..number'를 append하면, you can specify a value to increase or decrease by each time.
```bash
#!/bin/bash
# Basic range with steps for loop
# It is gonna count down from 10 to 0 as many as 2 by each time
for value in {10..0..2}; do
    echo $value
done
echo All done
```
- for loop를 wildcards(*)와 함께 사용했을때 더욱 강력하다.
```bash
#!/bin/bash
# Make a php copy of any html files
for value in $1/*.html; do
    cp $value $1/$( basename -s .html $value ).php
done
```

## Controlling Loops: Break and Continue
- **break**  
다음은 디스크 사용이 90%를 넘었을 때, bash에게 break를 지시하여 바로 loop를 빠져나오도록 한다.
```bash
#!/bin/bash
# Make a backup set of files
for value in $1/*; do
    used=$( df $1 | tail -1 | awk '{ print $5 }' | sed 's/%//' )
    if [ $used -gt 90 ]; then
        echo Low disk space 1>&2
        break
    fi
    cp $value $1/backup/
done
```
- **continue**  
continue는 bash에게 현재의 iteration을 멈추고 다음 iteration을 진행하다록 지시한다.  
```bash
#!/bin/bash
# Make a backup set of files
for value in $1/*; do
    if [ ! -r $value ]; then
        echo $value not readable 1>&2
        continue
    fi
        cp $value $1/backup/
done
```

## Select
Select는 list안의 모든 데이터를 숫자로 메뉴화된 prompt를 만들어주며, user는 숫자로 input이 가능하며 입력된 값은 변수로 할당된다.  
A few points to note:  
- No error checking is done. If the user enters something other than a number not corresponding to an item then **var** becomes null (empty).  
- If the user hits *enter* without entering data then the list of options will be displayed again.  
- The loop will end when an EOF signal is entered or the break statement is issued.  
- You may change the system variable **PS3** to change the prompt that is displayed
```bash
#!/bin/bash
# A simple menu system
names='Kyle Cartman Stan Quit'
PS3='Select character: '
select name in $names; do
    if [ $name == 'Quit' ]; then
        break
    fi
    echo Hello $name
done
echo Bye
```