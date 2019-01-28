alternatives command
===

## syntax
> $ alternatives --install \<link\> \<name\> \<path\> \<priority\> [--slave \<link\> \<name\> \<path\>]  
\<link\> : 심볼릭 링크의 경로
\<name\> : alternatives에서 고나리할 심볼릭 링크 그룹명
\<path\> : 패키지의 절대 경로
\<priority\> : 링크 그룹 내에서 우선순위 지정. 정수로 입력하며 클 수록 높음.

/usr/sbin/alternatives --install /usr/java/latest java_latest /usr/lib/jvm/java 20000
