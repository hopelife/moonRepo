
## ubuntu

### SSH 접속(putty)

#### ROOT 계정 활성화

```
$ sudo passwd root
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

#### ubuntu(최초 계정) 암호 설정

#### 계정 만들기

```
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
```
su - [유저명]


$ su
# su - ubuntu

```



### check directory

```bash
$ cd /
$ ls
bin   etc         lib         media  proc  sbin  sys  var
boot  home        lib64       mnt    root  snap  tmp  vmlinuz
dev   initrd.img  lost+found  opt    run   srv   usr
```

### check installed applications

#### apt

```
$ apt-get -v
apt 1.2.24 (amd64)
```

```
$ apt-get -v
apt 1.2.24 (amd64)
```

#### git

```
$ git version
git version 2.7.4
```

```
$ git config --global user.name "hopelife"
$ git config --global user.email deverlife@gmail.com


$ git config --global user.name <user_name>
$ git config --global user.email <user_email>
```


#### nano

```
$ nano --version
GNU nano, version 2.5.3
```

#### python

```
$ python3 --version
Python 3.5.2
```

#### curl

```
$ curl -V
curl 7.47.0 (x86_64-pc-linux-gnu) libcurl/7.47.0 GnuTLS/3.4.10 zlib/1.2.8 libidn/1.32 librtmp/2.3
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtmp rtsp smb smbs smtp smtps telnet tftp
Features: AsynchDNS IDN IPv6 Largefile GSS-API Kerberos SPNEGO NTLM NTLM_WB SSL libz TLS-SRP UnixSockets
```

### install applications

#### node.js

```
$ node -v
The program 'node' is currently not installed. You can install it by typing:
sudo apt install nodejs-legacy
```

```
$ sudo apt-get update
$ sudo apt install global nodejs

~$ node -v
The program 'node' is currently not installed. You can install it by typing:
sudo apt install nodejs-legacy

~$ nodejs -v
v4.2.6

```


#### vsftpd

##### install
```
$ sudo apt-get update
$ sudo apt-get install global vsftpd
```

```
~$ vsftpd -v
vsftpd: version 3.0.3
~$ whereis vsftpd
vsftpd: /usr/sbin/vsftpd /etc/vsftpd.conf /usr/share/man/man8/vsftpd.8.gz
```


##### add user

```
$ sudo vi /etc/ftpusers
```

```
root@ip-172-31-41-147:~# sudo adduser aws_ftp
Adding user `aws_ftp' ...
Adding new group `aws_ftp' (1002) ...
Adding new user `aws_ftp' (1002) with group `aws_ftp' ...
Creating home directory `/home/aws_ftp' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for web
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y

```

```
$ sudo vi /etc/ftpusers
```

```
aws_ftp <<추가>>
```


#### EC2 인스턴스 인바운드(Inbound) 추가
[AWS EC2 관리 콘솔](https://ap-northeast-1.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#Instances:sort=instanceId)
- AWS EC2 관리 콘솔 > 왼쪽 내비게이션 메뉴 > 보안 그룹(Security Groups) > Inbound 탭 선택
- 포트 추가시 '소스: 0.0.0.0/0'로 설정
- 80 포트 추가(http용)
- 443 포트 추가(https용)
- 20-21 범위 포트 추가(ftp용)
- 1024-1048 포트 범위 추가(ftp passive mode용)
- 4000 포트 추가(jekyll server용)


#### VSFTP 설정
- 설정 파일 열기

```
$ sudo vi /etc/vsftpd.conf
```


```
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
```
// 재시작1
sudo /etc/init.d/vsftpd restart

// 재시작2
$ sudo service vsftpd restart
```


##### filezilla 접속
!!! 현재 root로만 접속 가능 !!!



#### ruby

```

```

#### bundler


#### jekyll


```
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

_$ gem install jekyll bundler
```


```
~$ mkdir www
~$ cd www
```

```
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

```
//connect jekyll server in browser

http://13.230.8.128:4000/
```


#### create github repository for jekyll blog
- github account: hopelife
[gitub hopelife](https://github.com/hopelife)
- 상단 우측 메뉴 > New repository
- 'Create a new repository' 페이지 > Repository Name -> hopelife.github.io


```
echo "# hopelife.github.io" >> README.md
git init
git add *
git commit -m "first commit"
git remote add hopelife https://github.com/hopelife/hopelife.github.io.git
git push -u hopelife master
```






### directory
[C.2. The Directory Tree](https://help.ubuntu.com/lts/installation-guide/s390x/apcs02.html)
[Filesystem Hierarchy Standard](http://www.pathname.com/fhs/pub/fhs-2.3.html)

Ubuntu adheres to the Filesystem Hierarchy Standard for directory and file naming. This standard allows users and software programs to predict the location of files and directories. The root level directory is represented simply by the slash /. At the root level, all Ubuntu systems include these directories:

| Directory | Content |
|-----------|---------|
| bin | Essential command binaries |
| boot | Static files of the boot loader |
| dev | Device files |
| etc | Host-specific system configuration |
| home | User home directories |
| lib | Essential shared libraries and kernel modules |
| media | Contains mount points for replaceable media |
| mnt | Mount point for mounting a file system temporarily |
| proc | Virtual directory for system information |
| root | Home directory for the root user |
| run | Run-time variable data |
| sbin | Essential system binaries |
| sys | Virtual directory for system information |
| tmp | Temporary files |
| usr | Secondary hierarchy |
| var | Variable data |
| srv | Data for services provided by the system |
| opt | Add-on application software packages |

The following is a list of important considerations regarding directories and partitions. Note that disk usage varies widely given system configuration and specific usage patterns. The recommendations here are general guidelines and provide a starting point for partitioning.

- The root partition / must always physically contain /etc, /bin, /sbin, /lib and /dev, otherwise you won't be able to boot. Typically 150–310MB is needed for the root partition.

- /usr: contains all user programs (/usr/bin), libraries (/usr/lib), documentation (/usr/share/doc), etc. This is the part of the file system that generally takes up most space. You should provide at least 500MB of disk space. This amount should be increased depending on the number and type of packages you plan to install. A generous server installation should allow 4–6GB.

- It is now recommended to have /usr on the root partition /, otherwise it could cause some trouble at boot time. This means that you should provide at least 600–750MB of disk space for the root partition including /usr, or 5–6GB for a workstation or a server installation.

- It is now recommended to have /usr on the root partition /, otherwise it could cause some trouble at boot time. This means that you should provide at least 600–750MB of disk space for the root partition including /usr, or 5–6GB for a workstation or a server installation.

- /var: variable data like news articles, e-mails, web sites, databases, the packaging system cache, etc. will be placed under this directory. The size of this directory depends greatly on the usage of your system, but for most people will be dictated by the package management tool's overhead. If you are going to do a full installation of just about everything Ubuntu has to offer, all in one session, setting aside 2 or 3 GB of space for /var should be sufficient. If you are going to install in pieces (that is to say, install services and utilities, followed by text stuff, then X, ...), you can get away with 300–500 MB. If hard drive space is at a premium and you don't plan on doing major system updates, you can get by with as little as 30 or 40 MB.

- /tmp: temporary data created by programs will most likely go in this directory. 40–100MB should usually be enough. Some applications — including archive manipulators, CD/DVD authoring tools, and multimedia software — may use /tmp to temporarily store image files. If you plan to use such applications, you should adjust the space available in /tmp accordingly.

- /home: every user will put his personal data into a subdirectory of this directory. Its size depends on how many users will be using the system and what files are to be stored in their directories. Depending on your planned usage you should reserve about 100MB for each user, but adapt this value to your needs. Reserve a lot more space if you plan to save a lot of multimedia files (pictures, MP3, movies) in your home directory.


### apt(Advanced Packaging Tool)
[package manager apt](https://help.ubuntu.com/lts/serverguide/apt.html)

[Install global on Ubuntu: sudo apt-get install global](https://www.devmanuals.net/install/ubuntu/ubuntu-12-04-lts-precise-pangolin/install-global.html)

The apt command is a powerful command-line tool, which works with Ubuntu's Advanced Packaging Tool (APT) performing such functions as installation of new software packages, upgrade of existing software packages, updating of the package list index, and even upgrading the entire Ubuntu system.

Being a simple command-line tool, apt has numerous advantages over other package management tools available in Ubuntu for server administrators. Some of these advantages include ease of use over simple terminal connections (SSH), and the ability to be used in system administration scripts, which can in turn be automated by the cron scheduling utility.

Some examples of popular uses for the apt utility:

1. Install a Package: Installation of packages using the apt tool is quite simple. For example, to install the network scanner nmap, type the following:

```
sudo apt install nmap
```

2. Remove a Package: Removal of a package (or packages) is also straightforward. To remove the package installed in the previous example, type the following:

```
sudo apt remove nmap
```

복수 꾸러미: 설치나 삭제를 위해 복수의 꾸러미를 지정할 때는, 공백(스페이스 키로)으로 구분 합니다.

Also, adding the --purge option to apt remove will remove the package configuration files as well. This may or may not be the desired effect, so use with caution.

3. Update the Package Index: The APT package index is essentially a database of available packages from the repositories defined in the /etc/apt/sources.list file and in the /etc/apt/sources.list.d directory. To update the local package index with the latest changes made in the repositories, type the following:

```
sudo apt update
```

4. Upgrade Packages: Over time, updated versions of packages currently installed on your computer may become available from the package repositories (for example security updates). To upgrade your system, first update your package index as outlined above, and then type:

```
sudo apt upgrade
```

For information on upgrading to a new Ubuntu release see Upgrading.

Actions of the apt command, such as installation and removal of packages, are logged in the /var/log/dpkg.log log file.

For further information about the use of APT, read the comprehensive Debian APT User Manual or type:

```
apt help
```

### git



### nano

### node.js
[How To Install Node.js on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04)

