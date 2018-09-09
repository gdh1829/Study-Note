a=""
b=" "

#true
if [ -n $a ]; then
    echo 'length of the string a is not 0'
    echo ${#a} #0
fi

#true - weirdo...
if [ -n $b ]; then
    echo 'length of the string b is not 0'
    echo ${#b} #1
fi

#!true
if [ ! -z $a ]; then
    echo 'length of the string a is not 0'
    echo ${#a}
fi

#!true
if [ ! -z $b ]; then
    echo 'length of the string b is not 0'
    echo ${#b}
fi