## AWS EC2 활용

### FTP 서버 설정
[아마존 리눅스 AMI에 FTP 서버 설정하기](https://nolboo.kim/blog/2015/11/23/ftp-server-on-amazon-linux-ami/)

#### vsftpd 설치

```
$ sudo apt-get update
$ sudo apt-get install vsftpd
```

#### EC2 인스턴스의 FTP 포트를 연다.
- AWS EC2 관리 콘솔에 로그인하고 왼쪽의 내비게이션 메뉴에서 보안 그룹(Security Groups)을 선택한다.
- EC2 인스턴스에 할당된 보안 그룹을 선택하고 Inbound 탭에서 20-21 범위의 포트를 추가한다.
- 1024-1048 포트 범위도 추가한다.


#### VSFTP 설정
아래의 값을 참고하여 설정한 후에, 저장하고 vsftpd를 재시작 해준다.

- 설정 파일 열기

```
$ sudo nano /etc/vsftpd.conf
```

```
// anonymous 유저 사용 불가
anonymous_enable=NO  /* 수정 필요 내용

// 계정사용자 접속 가능
local_enable=YES

// 업로드 가능
write_enable=YES

// 디렉토리나 파일 생성시 umask 값
local_umask=022

// 접속시 메세지
ftpd_banner=Welcome to moonAWS FTP service

// 접속시 출력 메세지 설정 ( shell등을 이용해 접속시 )
// 사용자 홈디렉토리에 .message 파일에 작성
dirmessage_enable=YES

// chroot 적용
// 아래와 같은 설정을 할 경우 사용자들은 자신의 계정에서 상위 디렉토리로 이동할수 없게된다.
chroot_local_user=YES

// 특정 사용자만을 Jail 설정할 경우
// chroot_list에 등록되어있는 계정에만 chroot가 적용
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list

// 특정 사용자를 제외한 나머지 사용자만을 Jail 설정할 경우
// chroot_list에 등록된 계정을 제외한 나머지가 자신의 계정에 chroot가 걸림
chroot_local_user=YES
chroot_list_enable=YES
chroot_list_file=/etc/vsftpd/chroot_list

// 계정마다 동적으로 설정할 경우
// 아래와 같이 설정을 하게 되면 /etc/passwd 파일을 참고하여 jail 설정을 할 수 있게 됨
// /etc/passwd 파일을 수정하여 경로에 .을 찍게 되면 그 지점이 chroot지점이 됨
// theeye:x:600:100::/home/./theeye:/bin/bash
chroot_local_user=YES
passwd_chroot_enable=YES
```

- passive mode 설정
```
//추가
pasv_enable=YES
pasv_min_port=1024
pasv_max_port=1048
pasv_address=13.124.194.133
#pasv_address=자신의 인스턴스 공인 IP
```


#### FTP 디렉토리 변경
vsftpd를 설치하면서 자동으로 ftp 유저가 생성되며 홈디렉토리로 /srv/ftp 로 지정된다. 이것을 변경해 보자.


```bash
// 사용할 디렉토리 생성
$ sudo mkdir /home/ftp

// ftp 유저의 홈디렉토리를 변경 
$ sudo usermod -d /home/ftp ftp
```

// 재시작
$ sudo restart vsftpd
```

#### FTP 접속을 거부할 유저 등록
한 줄에 한명씩 아이디를 등록하면 해당 유저는 접속이 거부된다.

```bash
// 이 곳에 등록
$ sudo vi /etc/ftpusers

// 재시작
$ sudo service vsftpd restart
```


#### passive mode
[vsftpd 패시브 모드로 동작하게 하기](http://theeye.pe.kr/archives/1947)


클라이언트가 FTP서버에 접속하여 데이터를 주고 받는데에는 엑티브 모드와 패시브 모드 두가지가 있습니다. 이 두가지의 차이는 다음과 같습니다.

엑티브 모드는 클라이언트가 데이터를 수신받을 임의의 포트를 열고 서버에 알려주면 서버는 자신의 20번 포트를 통해 클라이언트의 임의의 포트에 데이터를 전송해 줍니다.

하지만 엑티브 모드에서는 클라이언트가 방화벽(공유기등의 사설 네트워크) 밑에 있다면 외부에서 이 클라이언트에 직접 접근하는것을 불가능합니다. 그래서 패시브 모드에서는 이러한 동작을 반대로 진행합니다. 정리하면 다음과 같습니다.

패시브 모드는 서버가 데이터를 송신해줄 임의의 포트를 열고 클라이언트에 알려주면 클라이언트는 서버의 임의의 포트에 접속하여 데이터를 가져갑니다.

결과적으로 방화벽과 같은 복잡한 네트워크 환경에서는 FTP의 패시브 모드의 지원이 꼭 필요합니다. 하지만 여기서 문제가 있는데 패시브 모드에서 서버가 사용하는 임의의 포트가 1024 이후의 모든 임의의 포트라는 것입니다. 이는 서버의 보안이나 방화벽 설정을 함에 있어 껄끄러움으로 작용하게 됩니다.

vsftpd에서는 이 패시브모드의 포트의 범위를 임의 설정할 수 있습니다. 그렇게 되면 방화벽 설정도 한결 용이해 질것입니다. /etc/vsftpd/vsftpd.conf 파일에 다음의 내용을 추가해줍니다.


pasv_enable=Yes
pasv_min_port=10090
pasv_max_port=10100
1
2
3
pasv_enable=Yes
pasv_min_port=10090
pasv_max_port=10100
위에서 설정한 포트의 범위는 원하시는 적절한 범위로 설정하시기 바랍니다. 이제 방화벽 설정을 추가해 보겠습니다. /etc/sysconfig/iptables 에 다음을 추가하겠습니다.


-A INPUT -m state --state NEW -m tcp -p tcp --dport 10090:10100 -j ACCEPT
1
-A INPUT -m state --state NEW -m tcp -p tcp --dport 10090:10100 -j ACCEPT
이제 데몬들을 재시작하면 패시브 모드가 정상적으로 동작하게 됩니다.


ftp> get eye.sql
local: eye.sql remote: eye.sql
229 Entering Extended Passive Mode (|||10093|).
150 Opening BINARY mode data connection for eye.sql (13719976 bytes).
 30% |****************                                       |  4094 KiB  682.45 KiB/s    00:13 ETA
1
2
3
4
5
ftp> get eye.sql
local: eye.sql remote: eye.sql
229 Entering Extended Passive Mode (|||10093|).
150 Opening BINARY mode data connection for eye.sql (13719976 bytes).
 30% |****************                                       |  4094 KiB  682.45 KiB/s    00:13 ETA
파일을 한번 다운로드 받아보았습니다. 정상적으로 패시브 모드로 진입하는것을 확인할 수 있습니다.

==============================
#### vsftpd.conf 파일 업데이트

```
sudo nano /etc/vsftpd/vsftpd.conf
```

```
anonymous_enable=YES  //익명접근 허용

//추가
pasv_enable=YES
pasv_min_port=1024
pasv_max_port=1048
pasv_address=자신의 인스턴스 공인 IP



#### vsftpd 재시작
```
sudo /etc/init.d/vsftpd restart
```

/etc/vsftpd/user_list를 보면 다음과 같을 것이다:

# vsftpd userlist
# If userlist_deny=NO, only allow users in this file
# If userlist_deny=YES (default), never allow users in this file, and
# do not even prompt for a password.
# Note that the default vsftpd pam config also checks /etc/vsftpd/ftpusers
# for users that are denied.
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
news
uucp
operator
games
nobody
이건 기본적으로 “이 사용자들은 FTP 접근을 허락하지 않는다”라고 말하는 것이다. vsftpd는 이 목록에 없는 사용자가 FTP에 접근할 수 있게 한다.

그러므로 새 FTP 계정을 만들기 위해서, 서버에 사용자를 새로 만들어야 한다.(만약 /etc/vsftpd/user_list에 열거되지 않은 사용자 계정(예를 들어 ec2-user: 역자주)을 이미 가지고 있다면 다음 단계로 넘어간다.)

EC2 인스턴스에 사용자를 새로 만드는 것은 매우 간단하다. 예를 들어 사용자 bret을 만들려면:

sudo adduser bret
sudo passwd bret
다음과 같이 보일 것이다.



6단계: 사용자의 홈 디렉토리를 제한한다.
이 시점에서의 FTP 사용자는 홈 디렉토리에 제한이 없다. 이것은 보안상 좋지 않으나, 매우 쉽게 고칠 수 있다.

vsftpd.conf 파일을 편집한다:

sudo nano /etc/vsftpd/vsftpd.conf
다음 라인을 주석해제한다:

chroot_local_user=YES
다음과 같이 보일 것이다:



vsftpd 서버를 재시작한다:

sudo /etc/init.d/vsftpd restart
이제 다 했다!

부록 A: 리부트에서 살아남기
vsftpd는 서버가 부트할 때 자동으로 시작되지 않는다. 다음과 같이 한다:

sudo chkconfig --level 345 vsftpd on
부록 A: vsftpd 제거하기(역자)
sudo yum remove vsftpd
우분투와 달리 위의 명령어로 환경설정까지 제거되고, 서비스도 정지된다.



### Git 설치

#### Git 설치
```
sudo apt-get install git
```

#### Git 서버 설치
```
sudo add-apt-repository ppa:git-core/ppa
sudo apt-get update
sudo apt-get install git-core
git version
```

============================

### jekyll

# ubuntu

```
$ sudo apt-get install curl
$ gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
$ \curl -sSL https://get.rvm.io | bash -s stable
$ source /home/<ubuntu>/.rvm/scripts/rvm
$ rvm install ruby
$ sudo apt-get install nodejs
$ gem install jekyll
$ gem install jekyll bundler
```

```
ubuntu@ip-172-31-19-231:/var$ sudo chown ubuntu:ubuntu /var
```

```
$ jekyll new my-awesome-site
$ cd my-awesome-site
$ bundle exec jekyll serve
$ bundle exec jekyll serve --host=0.0.0.0	//aws!!!
```

```
ubuntu@ip-172-31-19-231:/var/blog$ which gem
/home/ubuntu/.rvm/rubies/ruby-2.4.1/bin/gem
ubuntu@ip-172-31-19-231:/var/blog$ which bundle
/home/ubuntu/.rvm/gems/ruby-2.4.1/bin/bundle
```

 
```
mkdir /var/blog

ubuntu@ip-172-31-19-231:/var$ sudo chown ubuntu:ubuntu -R /var/blog
ubuntu@ip-172-31-19-231:/var$

ubuntu@ip-172-31-19-231:/var$ sudo chown ubuntu:ubuntu /var
```

#### git init / remote / pull
```
/var$ jekyll new blog2
/var$ cd blog2
/var/blog2$ git init
/var/blog2$ git remote add blog1 https://github.com/hopelife/hopelife.github.io.git
/var/blog2$ git pull blog1 master

ubuntu@ip-172-31-19-231:/var/blog2$ ls
404.html  about.md  _config.yml  Gemfile  Gemfile.lock  index.md  _posts
ubuntu@ip-172-31-19-231:/var/blog2$ rm *.html
ubuntu@ip-172-31-19-231:/var/blog2$ rm *.md
ubuntu@ip-172-31-19-231:/var/blog2$ rm _c*
ubuntu@ip-172-31-19-231:/var/blog2$ ls
Gemfile  Gemfile.lock  _posts
ubuntu@ip-172-31-19-231:/var/blog2$ rm -rf _posts
ubuntu@ip-172-31-19-231:/var/blog2$ rm -rf .git*

ubuntu@ip-172-31-19-231:/var/blog2$ ls
Gemfile  Gemfile.lock


/var/blog2$ git pull blog1 master
```

### 터미널과 분리

```
var/blog2$ bundle exec jekyll serve --host=0.0.0.0 --detach

Server detached with pid '2036'. Run `pkill -f jekyll' or `kill -9 2036' to stop the server.
```
