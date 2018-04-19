### ls

#### NAME

ls, dir, vdir - 경로의 내용을 나열한다.

#### SYNOPSIS

ls [-abcdfgiklmnpqrstuxABCFGLNQRSUX1] [-w cols] [-T cols] [-I pattern] [--all] [--escape] [--directory] [--inode] [--kilobytes] [--numeric-uid-gid] [--no-group] [--hide-control-chars] [--reverse] [--size] [--width=cols] [--tabsize=cols] [--almost-all] [--ignore-backups] [--classify] [--file-type] [--full-time] [--ignore=pattern] [--dereference] [--literal] [--quote-name] [--recursive] [--sort={none,time,size,extension}] [--format={long,verbose,commas,across,vertical,single-column}] [--time={atime,access,use,ctime,status}] [--help] [--version] [--color[={yes,no,tty}]] [--colour[={yes,no,tty}]] [name...]

#### DESCRIPTION

이 문서는 더이상 최신 정보를 담고 있지않다. 그래서, 몇몇 틀릴 경우도 있고, 부족한 경우도 있을 것이다. 완전한 매뉴얼을 원하면, Texinfo 문서를 참조하기 바란다.

이 매뉴얼 페이지는 ls 명령의 GNU 버전에 대한 것이다. dir과 vdir 명령은 ls 명령의 심블릭 파일로 그 출력 양식을 다르게 보여주는 풀그림들이다. 인자로 파일이름이나, 경로 이름이 사용된다. 경로의 내용은 초기값으로 알파벳 순으로 나열된다. ls의 경우는 출력이 표준 출력(터미날 화면)이면, 세로로 정열된 것이 가로로 나열된다. 다른 방식의 출력이면 한줄에 하나씩 나열된다. dir의 경우는, 초기값으로 ls와 같으나, 모든 출력에서 세로로 정열해서 가로로 나열한다.(다른 방식의 출력에서도 항상 같음) vdir의 경우는, 초기값으로 목록을 자세히 나열한다.

#### OPTIONS

-a, --all

경로안의 모든 파일을 나열한다. `.'으로 시작하는 파일 들도 포함된다.

-b, --escape

알파벳 형식을 사용하는 파일 이름안에서 그래픽 문자가 아닌 문자들을 사용한다. C와 같이 여덟가지 역슬래쉬 문자(`\')와 함께 오는 문자들을 사용한다.

-c, --time=ctime, --time=status

파일 최근 변경 시간에 따라 정열 해서 보여준다. 자세한 나열(-l 옵션)이면, 그 파일의 최근 변경 시간을 보여준다.

-d, --directory

경로안의 내용을 나열하지 않고, 그 경로를 보여준다.(이것은 쉘 스크립트에서 유용하게 쓰인다.)

-f

경로 내용을 정열하지 않는다: 이것은 디스크에 저장된 순으로 보여준다. -a와 -U 옵션과 같은 뜻이며, -l, -s, -t. 옵션과 반대뜻이다.

--full-time

시간을 간략히 표시하지 않고, 모두 보여 준다.

-g

무시: 유닉스 호환을 위해서 있음.

-i, --inode

파일 왼쪽에 색인 번호를 보여준다.

-k, --kilobytes

파일 크기가 나열되면, kb 단위로 보여준다. 이 옵션은 POSIXLY_CORRECT 환경 변수를 무시한다.

-l, --format=long, --format=verbose

파일 나열에 있어, 파일 형태, 사용권한, 하드링크 번호, owner 이름, group 이름, 파일 크기, 시간(따로 지정하지 않으면 파일이 만들어진 날자다)을 자세하게 나열한다. 시간은 여섯달 이전 것이면, 시간이 생략되고, 파일의 연도가 포함된다.

-m, --format=commas

파일을 가로로 나열한다. 가로로 나열할 수 있는 만큼 최대한 나열한다.

-n, --numeric-uid-gid

이름의 나열에서 UID,GID 번호를 사용한다.

-p

파일 형태를 지시하는 문자를 각파일에 추가한다.

-q, --hide-control-chars

파일 이름에 그래픽 문자가 아닌 것이 있으면, `?'로 표시한다.

-r, --reverse

정열 순서를 내림차순으로 한다.

-s, --size

파일 크기를 1Kb 단위로 나타낸다. POSIXLY_CORRECT 환경 변수가 지정되면, 512b 단위로 지정된다.

-t, --sort=time

파일 시간 순으로 정열한다. 최근 파일이 제일 먼저.

-u, --time=atime, --time=access, --time=use

파일 사용 시간 순으로 정열한다. 자세한 나열이면, 시간 표시는 만들어진 날자대신, 사용된 날자를 보여준다.

-x, --format=across, --format=horizontal

정열 방식을 가로로 한다.

-A, --almost-all

`.', `..' 경로를 제외하고 디렉토리안의 모든 파일을 나열한다.

-B, --ignore-backups

파일 끝이 `~'인 파일은 목록 나열에 제외된다.

-C, --format=vertical

정열 방식을 세로로 한다.

-F, --classify

파일 형식을 알리는 문자를 각 파일 뒤에 추가한다. 일반적으로 실행파일은 "*", 경로는 "/", 심블릭 링크는 "@", FIFO는 "|", 소켓은 "=", 일반적인 파일은 없다.

-G, --no-group

자세한 목록 나열에서 group 정보를 제외한다.

-L, --dereference

심블릭 링크 파일들을 그냥 파일로 보여준다.

-N, --literal

이름이 영문이 아닌 경우, C에서 사용하는 역슬래쉬 문자(`\')와 함께 사용하는 표기 대신 그대로 출력한다.

-Q, --quote-name

-N 옵션과 반대.

-R, --recursive

하위 경로와 그 안에 있는 모든 파일들도 나열한다.

-S, --sort=size

파일 크기가 가장 큰 것 부터 정열해서 나열한다.

-U, --sort=none

정열을 하지 않고, 디스크에 저장된 순서대로 보여준다. 이 옵션은 -f 옵션을 사용할 수 없다. 유닉스 용 ls -f는 -a 옵션은 가능하나, -l, -s, -t 옵션이 불가능하기 때문이다.

-X, --sort=extension

파일 확장자 순으로 정열한다. 확장자가 없는 파일이 제일 먼저 나열된다.

-1, --format=single-column

한 줄에 한 파일씩 나열.

-w, --width cols

가로 길이를 ols 값으로 지정한다. 기본적으로는 한 화면의 가로 값이된다. 또한 COLUMNS 환경 변수 값으로 지정할 수 있다. 초기값은 80이다.

-T, --tabsize cols

탭이 사용될 때, cols 값으로 지정한다. 초기값은 8이다. 0으로 지정되면 탭 문자는 무시된다.

-I, --ignore pattern

pattern 패턴으로 지정된 파일들은 목록에서 제외된다. 이때, 명령행에서 그 파일이 지정되면 물론 나열된다.

--color, --colour, --color=yes, --colour=yes

파일의 형태에 따라 그 파일의 색깔을 다르게 보여주는 기능한다. 자세한 이야기는 아래 DISPLAY COLORIZATION 부분을 참조한다.

--color=tty, --colour=tty

--color 옵션과 같으나, 단지 표준 출력에서만 색깔을 사용한다. 이 옵션은 칼라 제어 코드를 지원하지 않는 보기 풀그림을 사용하는 쉘 스크립트나, 명령행 사용에서 아주 유용하게 쓰인다.

--color=no, --colour=no

색깔 사용하지 않는다. 이것이 초기값이다. 이옵션은 색깔 사용을 이미 하고 있다면, 이 값을 무시한다.

--help

도움말을 보여주고 마친다.

--version

버전 정보를 보여주고 마친다.

 

DISPLAY COLORIZATION

--color 옵션을 사용할 때, 이 버전의 ls 명령은 파일 이름이나, 파일 형태에 따라 파일의 색깔별로 나열할 수 있다. 이 칼라화는 초기값으로 파일 형태에 따라서만 사용된다. 사용되는 코드는 ISO 6429 (ANSI)이다.

이런 초기 색깔 지정은 LS_COLORS (또는 LS_COLOURS) 환경 변수 지정으로 바꿀 수 있다. 이 변수들의 형식은 termcap(5) 파일 포멧의 방식을 사용한다. 각 항목은 ":"으로 하며, 각 항목은 "xx=문자열"로 한다. xx에는 두개의 문자가 오는데, 여기서 사용할 수 있는 문자는 다음과 같다.

no       0       파일 이름이 아닌 일반 텍스트

fi       0       일반 파일

di       32      경로

ln       36      심블릭 링크

pi       31      FIFO(파이프)

so       33      소켓

bd       44;37   블럭 장치

cd       44;37   캐릭터 장치

ex       35      실행 파일

mi       (없음)  잃어버린 파일 (초기값은 fi)

or       (없음)  심블릭 링크 대상이 없는 파일(초기값은 ln)

lc       \e[    왼쪽 코드

rc       m       오른쪽 코드

ec       (없음)  마침 코드 (lc+no+rc로 바뀜)

색깔을 바꿀 경우는 그 해당 변수만 바꾸면 된다.

파일 이름은 파일의 확장자에 따라 색깔을 지정할 수 있다. LS_COLORS 환경 변수에 포함하면 되고, 그 사용법은 위와 같다. 문법은 "*ext=문자열"이다. 예를 들어, C 소스 파일을 파란색으로 지정하려면, "*.c=34"이다.

제어 문자는 C에서와 갈이 `\'문자로 시작하는 문자를 사용하거나, stty와 같이 `^'문자로 시작하는 문자를 사용할 수 있다. C 스타일일 경우는 \e는 Esc, \_ 공백문자, \? Delete 이다. 추가로, \ escape 문자는 \, ^, :, =의 초기 처리 방식을 무시하는데 사용될 수 있다.

각 파일은 <색깔값> <파일이름> 형태로 지정 된다. 만약 코드를 지엉하지 않으면, 가 대치된다. 이 방법은 보다 많은 변환을 하지만 일반적인 방법은 아니다. 왼쪽, 오른쪽, 마지막 코드는 일반적인 ISO 6429 코드를 지원하지 않는 터미날을 위한 값으로 특별한 경우가 아니면, 사용할 필요가 없다.

ISO 6429 코드일 경우 사용될 수 있는 코드값은 다음과 같다. (물론 lc, rc, ec 값은 제외된다.)

 0     초기 색깔로 다시 돌린다.

 1        강조색

 4        밑줄

 5        깜빡이는 글자.

30        까만색 전경

31        빨강 전경

32        녹색 전경

33        노랑(또는 갈색) 전경

34        파랑 전경

35        보라 전경

36        청록색 전경

37        흰색(또는 회색) 전경

40        까만색 배경

41        빨강 배경

42        녹색 배경

43        노랭(또는 갈색) 배경

44        파랑 배경

45        보라 배경

46        청록색 배경

47        흰색(또는 회색) 배경

모든 명령이 모든 시스템이나 디스플레이 장치에서 제대로 동작하는 것은 아니다.

몇 터미날은 초기 마지막코드(ec)가 인식되지 않을 수 있다. 만약, 색들을 사용했다면, no, fi 값을 0으로 지정해 초기값으로 되돌려 놓아야 한다.

BUGS

BSD 시스템에서는, -s 옵션이 HP-UX 시스템으로 부터 NFS 마운트된 파일을 위한 파일 크기가 반으로 잘못 보여진다고 한다. HP-UX 시스템에서는, BSD 시스템으로 부터 NFS 마운트된 파일을 위한 파일의 크기가 반대로 두배로 나타난다. 이런 현상은 HP-UX ls 풀그림도 마찬가지라고 한다.

영어권 문자셋을 사용할 경우는 별 문제가 없지만, 한국어와 같이 2바이트 문자권에서는 자국어로 된 파일 이름을 보기 위해 특별한 옵션을 지정해 주어야한다. 
``-N --color=tty'' 옵션이 그 옵션이다.

 

 

lsattr 의 매뉴얼

 

NAME
       lsattr  -  list file attributes on a Linux second extended
       file system
 
SYNOPSIS
       lsattr [ -RVadv ] [ files...  ]
 
DESCRIPTION
       lsattr lists the file attributes on a second extended file
       system.
 
OPTIONS
       -R     Recursively  list  attributes  of  directories  and
              their contents.
 
       -V     Display the program version.
 
       -a     List all files in directories, including files that
              start with `.'.
 
       -d     List  directories  like  other  files,  rather than
              listing their contents.
 
       -v     List the files version.
 
AUTHOR
       lsattr has been written by Remy  Card  <card@masi.ibp.fr>,
       the developer and maintainer of the ext2 fs.
 
BUGS
       There are none :-).
 
AVAILABILITY
       lsattr  is  part of the e2fsprogs package and is available
       for anonymous ftp from tsx-11.mit.edu in  /pub/linux/pack-
       ages/ext2fs.



## grep
[리눅스 grep 옵션 정리](http://blankspace-dev.tistory.com/277)

