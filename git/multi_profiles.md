# Git 멀티 프로파일 설정

## 배경
- 하나의 PC로부터 개인과 회사의 git account를 구분하여 사용해야할 필요가 있을 필요성이 있음.
- ex. 개인 깃 계정 활동과 회사 깃 계정 활동을 달리하여야 할 경우.

## 방법
- 회사용 PC에서 일부 개인업무 용 dir(~/personal)를 구성한다고 했을때를 가정으로 방법을 설명.
- github 플랫폼 사용 전제.

### 키 생성 후 깃헙 등록
- personal과 work용 ssh 키 셋을 각각 준비.
  - 키 생성 커맨드
    > cd ~/.ssh
    ssh-keygen -t rsa -b 4096 -C "{your personal}"
- ssh agent 키 등록
  - ssh-add ~/.ssh/{key name}.rsa
  - 키 등록 확인: ssh-add -l
- github 등록

### SSH config
- ~/.ssh/config
```shell
Host work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa

Host personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_personal
```

### .gitconfig 설정
- ~/.gitconfig
  - default로서 .gitconfig-work를 사용하고,
  - personal dir에서의 작업인 경우 .gitconfig-personal을 오버라이딩한다.
```shell
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[include]
  path = .gitconfig-work
[includeIf "gitdir:~/personal/"]
  path = .gitconfig-personal
```

- .gitconfig-work 
```shell
[user]
  name = robin.ko
  email = robin.ko@EMAIL.COM
```

- .gitconfig-personal
```shell
[user]
	name = daehyeop.ko
	email = daehyeop.ko@EMAIL.COM
```

## 사용
remote repository를 clone할 때, REMOTE에 액세스할 USER와 HOST 지정을 커스텀 해야한다.  
기본적으로 깃헙을 통해 ssh clone 주소를 카피할 경우 아래와 같다.  
- `git clone git@github.com:gdh1829/Study-Note.git`
  
우리는 ssh config를 커스텀했기 때문에, repository에 맞는 ssh config를 적용해야 하므로,  
해당 repository가 work용이라면, 아래와 같이 사용한다.  
- `git clone git@work:gdh1829/Study-Note.git`
personal인 경우도 마찬가지이다.
- `git clone git@personal:gdh1829/Study-Note.git`
- `ssh -T git@personal` 커맨드로 테스트도 가능하다.
  - expected output: Hi {xxx}! You've successfully authenticated, but GitHub does not provide shell access.

기존에 미리 받아둔 REPO에 대하여 적용하고 싶다면,
- `git remote -v`로 확인 후, `git remote set-url origin git@personal:gdh1829/Study-Note.git`와 같은 식으로 변경해주도록 한다.
