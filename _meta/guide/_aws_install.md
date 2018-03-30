## aws(ubuntu) 설정

### aws 계정 만들기


### ec2(free-tier) 만들기


### SSH 접속(putty) 설정


### ec2 server 설정(on putty connection)

#### root 계정 활성화

```shell
$ sudo passwd root

Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

#### ubuntu(최초 계정) 암호 설정

```shell
~$ sudo su

root# passwd ubuntu

Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```


#### 계정 만들기

```shell
~$ sudo su

$ adduser aws_ftp

Adding user `aws_ftp' ...
Adding new group `aws_ftp' (1001) ...
Adding new user `aws_ftp' (1001) with group `aws_ftp' ...
Creating home directory `/home/aws_ftp' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
Sorry, passwords do not match
passwd: Authentication token manipulation error
passwd: password unchanged
Try again? [y/N] y
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for aws_ftp
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y
```


### 사용자 변경

- 일반 계정(root) -> 일반 계정
```shell
$ su - ubuntu
# su - ubuntu

su - <유저명>
```

- 일반 계정-> root
```shell
$ su - 

su - <유저명>
```


### check directory

```shell
$ cd /
$ ls
bin   etc         lib         media  proc  sbin  sys  var
boot  home        lib64       mnt    root  snap  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv   usr
```

### check installed applications

#### apt
[package manager apt](https://help.ubuntu.com/lts/serverguide/apt.html)
[Install global on Ubuntu: sudo apt-get install global](https://www.devmanuals.net/install/ubuntu/ubuntu-12-04-lts-precise-pangolin/install-global.html)

- check version

```shell
$ apt-get -v
apt 1.2.24 (amd64)
```

```
$ apt -v
apt 1.2.24 (amd64)
```


#### git

- check version
```shell
$ git version
git version 2.7.4
```

- cofig user_name / user_email

```shell
$ git config --global user.name "hopelife"
$ git config --global user.email deverlife@gmail.com


$ git config --global user.name <user_name>
$ git config --global user.email <user_email>
```


#### nano

- check version
```shell
$ nano --version
GNU nano, version 2.5.3
```


#### python
- check version

```shell
$ python3 --version
Python 3.5.2
```


#### curl

- check version
```shell
$ curl -V
curl 7.47.0 (x86_64-pc-linux-gnu) libcurl/7.47.0 GnuTLS/3.4.10 zlib/1.2.8 libidn/1.32 librtmp/2.3
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtmp rtsp smb smbs smtp smtps telnet tftp
Features: AsynchDNS IDN IPv6 Largefile GSS-API Kerberos SPNEGO NTLM NTLM_WB SSL libz TLS-SRP UnixSockets
```

### install applications

#### node.js
[How To Install Node.js on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04)

- check version

```shell
$ nodejs -v
The program 'nodejs' is currently not installed. You can install it by typing:
sudo apt install nodejs
```

- install

```shell
$ sudo apt-get update
$ sudo apt install global nodejs


~$ nodejs -v
v4.2.6

```


#### ftp server(vsftpd)
[아마존 리눅스 AMI에 FTP 서버 설정하기](https://nolboo.kim/blog/2015/11/23/ftp-server-on-amazon-linux-ami/)
[Ubuntu Server 에 vsftpd 이용하여 파일 전송하기](https://cjh5414.github.io/set-up-vsftpd-on-ubuntu/)
[리눅스 우분투 vsftpd 설치 및 설정](http://nahosung.tistory.com/40)

##### install

- install

```shell
$ sudo apt-get update
$ sudo apt-get install global vsftpd
```

- check version & where is installed

```shell
~$ vsftpd -v
vsftpd: version 3.0.3
~$ whereis vsftpd
vsftpd: /usr/sbin/vsftpd /etc/vsftpd.conf /usr/share/man/man8/vsftpd.8.gz
```


##### setting

- add user
```shell
$ sudo vi /etc/ftpusers
```


```Conf
aws_ftp <<추가>>
ubuntu <<추가>>
root
...
```


##### EC2 인스턴스 인바운드(Inbound) 추가
[AWS EC2 관리 콘솔](https://ap-northeast-1.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#Instances:sort=instanceId)
- AWS EC2 관리 콘솔 > 왼쪽 내비게이션 메뉴 > 보안 그룹(Security Groups) > Inbound 탭 선택
- 포트 추가시 '소스: 0.0.0.0/0'로 설정
- 80 포트 추가(http용)
- 443 포트 추가(https용)
- 20-21 범위 포트 추가(ftp용)
- 1024-1048 포트 범위 추가(ftp passive mode용)
- 4000 포트 추가(jekyll server용)


#### vsftpd.conf 편집
- 설정 파일 열기

```shell
$ sudo vi /etc/vsftpd.conf
```


```Conf
//변경
#local_enable=YES -> local_enable=YES

#write_enable=YES -> write_enable=YES

#utf8_filesystem=YES -> utf8_filesystem=YES

#local_umask=022 -> local_umask=022

pam_service_name=vsftpd -> pam_service_name=ftp


//추가
#
# userlist //user added
userlist_enable=YES
userlist_file=/etc/ftpusers
userlist_denystem=YES=NO


#
# passive mode // user add!!!
pasv_enable=YES
pasv_min_port=1024
pasv_max_port=1048
pasv_address=13.230.8.128

#
# ftp root directory //user add!!!
local_root=/home/ubuntu

```


##### vsftpd 재시작
```shell
// 재시작1
sudo /etc/init.d/vsftpd restart

// 재시작2
$ sudo service vsftpd restart
```


#### jekyll(+ rvm, ruby, bundler)

- install

```shell
//@@@curl이 설치되지 않은 경우
$ sudo apt-get install curl


$ gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3

//rvm 설치
$ \curl -sSL https://get.rvm.io | bash -s stable
$ source /home/ubuntu/.rvm/scripts/rvm

$ source /home/<user_name>/.rvm/scripts/rvm

//ruby 설치
$ rvm install ruby

//@@@nodejs가 설치되지 않은 경우
$ sudo apt-get install nodejs

//jekyll 설치
$ gem install jekyll

//bundler 설치
$ gem install bundler

//jekyll, bundler 설치
_$ gem install jekyll bundler
```

- web server directory 생성

```shell
~$ mkdir www
~$ cd www
```

- jekyll server 시작

```shell
$ jekyll new hopelife.github.io
$ cd hopelife.github.io
//host:0.0.0.0 : aws Inbound설정
//--detach: 터미널 종료후에도 jekyll server 종료안됨
$ bundle exec jekyll serve --host=0.0.0.0 --detach


$ jekyll new <site_name>
$ cd <site_name>
//host:0.0.0.0 : aws Inbound설정
//--detach: 터미널 종료후에도 jekyll server 종료안됨
$ bundle exec jekyll serve --host=0.0.0.0 --detach

//stop jekyll server
Server detached with pid '2036'. Run `pkill -f jekyll' or `kill -9 2036' to stop the server.
$ pkill -f jekyll
```


#### connect jekyll server in browser

- webbrowser open & type url

```Text
//connect jekyll server in browser

http://13.230.8.128:4000/
```

#### aws-github 연동

##### create github repository for jekyll blog
- github account: hopelife
  [gitub hopelife](https://github.com/hopelife)
- 상단 우측 메뉴 > New repository
- 'Create a new repository' 페이지 > Repository Name -> hopelife.github.io

##### init & push

```shell
echo "# hopelife.github.io" >> README.md
git init
git add *
git commit -m "first commit"
git remote add hopelife https://github.com/hopelife/hopelife.github.io.git
git push -u hopelife master
```


### tensorflow

```shell
$ sudo apt-get install python3-pip
$ sudo -H pip3 install --upgrade pip
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc0-py3-none-any.whl
$ sudo -H pip3 install --upgrade $TF_BINARY_URL

$ python3

>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> print(sess.run(hello))
Hello, TensorFlow!


$ sudo chmod -R 666 /usr/lib/python3.5

$ pip3 install --upgrade protobuf

//for python2
$ sudo apt-get install python-pip python-dev
$ pip install --upgrade pip
$ sudo -H pip install --upgrade $TF_BINARY_URL

```