Shell script Array
==========================
쉘 스크립트는 복잡한 데이터 구조를 사용할 수는 없지만, bash에서 1차원 배열은 사용 가능
배열을 참조할 때는 {}가 필요

<pre><code>
#!/bin/bash

app=("grep" "awk" "cut" "tr" "sed") #배열 선언
echo ${app[3]} #output: tr
echo ${app[@]} #output all of elements: "grep" "awk" "cut" "tr" "sed"
echo ${app[*]} #same output as ${app[@]}: "grep" "awk" "cut" "tr" "sed"
echo "${#app[@]}" #output size of the array
echo ${#app[*]} #위와 같음



</code></pre>