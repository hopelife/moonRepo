## manual
[git - 간편 안내서](https://rogerdudler.github.io/git-guide/index.ko.html)

### naming rule
- web_url: https://github.com/<git_id>
- git_url: https://github.com/<git_id>/<repo>.git
- local: 
  - blog : <base_dir>/github/blog/<git_id>
  - data : <base_dir>/github/data/<repo>

### Basic

#### local(command)
##### init / remote add / commit / pull / push

```
git init
git remote add <nick> <git_url>
git pull <nick> master

git add *
git commit -m '<comment>'
git push <nick> master
```

##### config
```
// semantic
$ git config --global user.name <username>
$ git config --global user.email <useremail>

// example
$ git config --global user.name "hopelife"
$ git config --global user.email deverlife@gmail.com
```

#### install
[](url)

### remote(setting)

#### create account

#### create repository

#### create blog(web page)


### Intermediate

#### remote

##### brief
- what?
  - 원격(리모트) 저장소 관리
  - 원격 저장소: 인터넷이나 네트워크 어딘가에 있는 저장소
- when?
  - (공동작업시) 원본 작업 data 저장
- how?
  - usage 참조

##### usage
- add
  - 
```
git remote add <nick> <git_url>

```
- show

```
git remote

git remote show

git remote -v
```

- rename
```
git remote rename <ori_nick> <rep_nick>

```

- remove
```
git remote rm <nick>
```


#### config
[.5 시작하기 - Git 최초 설정](https://git-scm.com/book/ko/v1/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%B5%9C%EC%B4%88-%EC%84%A4%EC%A0%95)

##### brief
- what?
  - Git 환경 설정
- when?
  - 설치후 사용 환정 설정/변경
- where
  - /etc/gitconfig
  - ~/.gitconfig
  - .git/config
- how?
  - usage 참조

##### usage
- 설정 확인
```
$ git config --list
```
- 사용자 정보
  - user.name / user.email
  - Basic 참조
- 편집기
  - 
- Diff도구
  - 

##### tag

### Expert



## list



### My Git account

#### account
| id | pw | email |
|-----|-----|-------|
| monblue | m******* | monwater@naver.com |
| monwater | m******* | monwater@gmail.com |
| moonHani | m******* | monwater@me.com |
| haniMoon | m******* | monblue@daum.net |
| monAndroid | m******* | life681225@gmail.com |
| hopelife | m******* | deverlife@gmail.com |

#### blog
| web_url | 용도 | theme |
|-----|-----|-------|
| monblue.github.io | 한의학서적 | - |
| monwater.github.io | - | - |
| moonhani.github.io | 한의원운영 | cards |
| monandroid.github.io | -  | cards |
| hanimoon.github.io | - | - |
| hopelife.github.io | - | - |

#### repo



#### fork



### repositories

