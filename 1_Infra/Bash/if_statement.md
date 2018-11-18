if statement
===

## Square Bracket([]) Logical Operations
|Operator   |Description   |
|:-:|---|
|! EXPRESSION   |The EXPRESSION is false.   |
|-n STRING   |The length of STRING is greater than zero.   |
|-z STRING   |The lengh of STRING is zero (ie it is empty).   |
|STRING1 = STRING2   |STRING1 is equal to STRING2   |
|STRING1 != STRING2   |STRING1 is not equal to STRING2   |
|INTEGER1 -eq INTEGER2   |INTEGER1 is numerically equal to INTEGER2   |
|INTEGER1 -gt INTEGER2   |INTEGER1 is numerically greater than INTEGER2   |
|INTEGER1 -lt INTEGER2   |INTEGER1 is numerically less than INTEGER2   |
|-d FILE   |FILE exists and is a directory.   |
|-e FILE   |FILE exists.   |
|-r FILE   |FILE exists and the read permission is granted.   |
|-s FILE   |FILE exists and it's size is greater than zero (ie. it is not empty).   |
|-w FILE   |FILE exists and the write permission is granted.   |
|-x FILE   |FILE exists and the execute permission is granted.   |
|-f FILE   |FILE exists and it is a regular file. Not a device file or a directory  |

## Boolean Operations
- **and** - &&
- **or** - ||
```bash
#!/bin/bash
# file, $1, is readable and its size is greater than 0
if [ -r $1 ] && [ -s $1 ]; then
    echo This file is useful.
fi
```
```bash
#!/bin/bash
# username is bob or andy
if [ $USER == 'bob' ] || [ $USER == 'andy' ]; then
    ls -alh
else
    ls
fi
```

## Case Statements
case statements는 pattern으로 true/false 판단
```bash
#!/bin/bash
# Print a message about disk useage.
space_free=$( df -h | awk '{ print $5 }' | sort -n | tail -n 1 | sed 's/%//' )
case $space_free in
    [1-5]*) # ) -> means the end of this parttern
        echo Plenty of disk space available
    ;; # ;; -> means the end of this set of statments
    [6-7]*)
        echo There could be a problem in the near future
    ;;
    8*)
        echo Maybe we should look at clearing out old files
    ;;
    9*)
        echo We could have a serious problem on our hands soon
    ;;
    *) # * -> represents any number of any character. Essentialy a catch all if for if none of the other cases match. It is not necssary but is often used.
        echo Something is not quite right here
    ;;
esac # esac-> is case backwards and indicates we are at the end of the case statement. 
```