# Git 멀티 프로파일 설정

## 배경
- 하나의 PC로부터 개인과 회사의 git account를 구분하여 사용해야할 필요가 있을 필요성이 있음.
- 예를 들어, 개인 깃 계정 활동과 회사 깃 계정 활동을 달리하여야 할 경우.

## 방법
- 회사용 PC에서 일부 개인업무 용 dir(personal)를 구성한다고 했을때를 가정으로 방법을 설명

### 키 생성 후 깃헙 등록
- home과 office용 ssh 키 셋을 각각 준비
    - 키 생성 커맨드
    > cd ~/.ssh
    ssh-keygen -t rsa -b 4096 -C "{your personal}"

### .gitconfig 설정
- personal dir에 개인 .gitconfig를 추가 
```shell
~/personal » cat .gitconfig
[user]
  name = gdh1829
  email = daehyeop.ko@gmail.com
```

- 베이스(~) dir에서 office용 .gitconfig 설정 추가

```shell
~ » cat .gitconfig
[user]
	name = work
	email = work@work.net
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[includeIf "gitdir:~/personal/"]
    path = ~/personal/.gitconfig
```

### END
- 위의 과정으로 끝! 간단.
- 조금 더 설명을 붙이자면, [includeIf ...] 라인 설정에 따라 만약 git 작업 디렉토리가 ~/personal일 경우 해당 디렉토리의 .gitconfig를 읽어들여 중복 property에 대하여 오버라이딩이 이루어지는 구조.
