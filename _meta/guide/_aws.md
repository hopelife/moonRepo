# AWS(Amazon Web Services)
[AWS 설명서](https://aws.amazon.com/ko/documentation/)

## AWS 계정 만들기
[AWS 계정 만들기](https://docs.aws.amazon.com/ko_kr/polly/latest/dg/setting-up.html])

[Amazon S3](https://aws.amazon.com/ko/documentation/s3/)
[Amazon RDS](https://aws.amazon.com/ko/documentation/rds/)
[AWS 명령줄 인터페이스](https://aws.amazon.com/ko/documentation/cli/)
[JavaScript용 AWS SDK](https://aws.amazon.com/ko/documentation/sdk-for-javascript/)



[도메인 이름 등록](https://aws.amazon.com/ko/getting-started/tutorials/get-a-domain/)

!!### AWS S3

[사용자 지정 도메인으로 정적 웹 사이트 설정](https://docs.aws.amazon.com/ko_kr/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)


## AWS EC2 활용
[Amazon EC2](https://aws.amazon.com/ko/documentation/ec2/)

### SSH 접속(Putty)
!!! 병원에서는 실패 !!!
[AWS EC2 인스턴스 생성 및 Putty로 접속하기](http://supdev.tistory.com/22)


#### Install Putty
- 


### FTP 서버 설정
!!! 현재 설정 실패 !!!
[아마존 리눅스 AMI에 FTP 서버 설정하기](https://nolboo.kim/blog/2015/11/23/ftp-server-on-amazon-linux-ami/)
[Ubuntu Server 에 vsftpd 이용하여 파일 전송하기](https://cjh5414.github.io/set-up-vsftpd-on-ubuntu/)
[리눅스 우분투 vsftpd 설치 및 설정](http://nahosung.tistory.com/40)



========================




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

