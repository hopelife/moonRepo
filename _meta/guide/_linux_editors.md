
## vi 명령어
[vi 명령어 모음](http://hbesthee.tistory.com/494)

### 삽입 명령

| 명령어 | 설명 |
|------|-----|
| a | 커서 뒤에 입력 |
| A | 라인 끝에 입력 |
| i | 커서 앞에 입력 |
| I | 라인시작 부분에 입력 |
| o | 커서 있는 라인 밑에 입력 |
| O | 커서가 있는 라인 위에 입력 |


### 커서 이동 명령

| 명령어 | 설명 |
|------|-----|
| h | 왼쪽으로 커서 한 칸 이동 |
| H | 화면의 처음으로 이동 |
| L | 오른쪽으로 한 칸 이동 |
| L | 화면 끝으로 이동 |
| e | 다음 단어의 마지막으로 이동 |
| E | 커서를 공백으로 구분된 다음 단어 끝으로 이동 |
| b | 한 단어 뒤로 |
| B | 커서를 공백으로 구분된 이전 단어로 이동 |
| w | 커서를 한 단어 뒤로 |
| W | 커서를 공백으로 구분된 다음 단어로 이동 |
| k | 커서를 한 라인 위로 |
| j | 커서를 한 라인 아래로 이동 |
| O | 커서를 라인의 시작으로 이동 |
| $ | 커서를 라인의 끝으로 이동 |
| Enter | 커서를 다음 라인 시작으로 이동 |
| - | 커서를 전 라인의 시작으로 이동 |
| Ctrl + F | 다음 화면으로 이동 |
| Ctrl + D | 화면의 반만 앞으로 이동 |
| Ctrl + B | 전 화면으로 이동 |
| Ctrl + U | 화면의 반만 뒤로 이동 |
| G | 커서를 텍스트 마지막 라인으로 |
| 숫자G | 커서를 숫자 라인만큼 이동 |
| M | 커서를 화면 중간 라인으로 이동 |
| “ | 커서를 전 위치로 이동 |
| ( | 문장의 시작으로 이동 |
| { | 문단의 시작으로 이동 |
| ) | 문장 끝으로 이동하여 다음 단어의 시작으로 커서 이동 |
| } | 문단 끝으로 이동 |


### 방향키를 이용한 커서 이동 명령

| 명령어 | 설명 |
|------|-----|
| <-, Del | 왼쪽으로 커서 한 칸 이동 |
| PageUp | 화면 위로 이동 |
| ->, Space | 오른쪽으로 한 칸 이동 |
| PageDown | 화면 아래로 이동 |
| ↑ | 윗 줄로 커서 이동 |
| Enter | 다음 줄 첫 칸으로 이동 |
| ↓ | 아래 줄로 커서 이동 |
| Esc | 다음 줄 첫 칸으로 이동 |
| Home | 줄 처음 칸으로 이동 |


### 삭제 명령

| 명령어 | 설명 |
|------|-----|
| x | 커서가 있는 문자 삭제 |
| X | 커서가 있는 문자 앞에 있는 문자 삭제 |
| dw | 커서가 있는 단어 삭제 |
| db | 커서가 앞에 있는 단어 삭제 |
| dW | 공백으로 구분된 뒷 단어 삭제 |
| dB | 공백으로 구분된 앞 단어 삭제 |
| dd | 커서가 있는 라인 삭제 |
| D | 커서가 있는 라인의 나머지 삭제 |
| d) | 문장의 나머지 삭제 |
| d} | 문단의 나머지 삭제 |
| dG | 파일의 나머지 삭제 |
| dH | 화면의 시작까지 삭제 |
| dL | 화면의 나머지 삭제 |
| J | 커서와 다음 단어의 공백을 모두 삭제 |


### 바꾸기 명령

| 명령어 | 설명 |
|------|-----|
| r | 커서에 있는 문자 대치 |
| R | 입력 모드로 한 문자씩 덮어씀 |
| s | 커서가 있는 문자 삭제 후 입력 모드로 전환 |
| S | 커서가 있는 줄을 삭제 후 입력 모드로 전환 |
| cb | 커서가 있는 앞 문자 삭제 후 입력 모드 |
| cW | 공백으로 구분된 뒷 단어를 삭제 후에 입력 모드 |
| cB | 공백으로 구분된 앞 단어 삭제 후 입력 모드 |
| cc | 커서가 있는 라인을 삭제하고 입력 모드 |
| C | 커서가 있는 라인의 나머지를 삭제하고 입력 모드로 전환 |
| cO | 커서에서부터 라인의 시작까지 텍스트 바꾸기 |
| c | 특정 텍스트 바꾸기 |
| c) | 문장의 나머지 바꾸기 |
| c} | 문단의 나머지 바꾸기 |
| cG | 파일의 나머지 바꾸기 |
| cm | 표시까지 모든 것 바꾸기 |
| cL | 화면의 나머지 바꾸기 |
| ch | 화면의 시작까지 바꾸기 |


### 복사

| 명령어 | 설명 |
|------|-----|
| yw | 커서가 있는 단어를 복사 |
| yb | 커서가 있는 앞 단어를 복사 |
| yW | 공백으로 구분된 뒷 단어 복사 |
| yB | 공백으로 구분된 앞 단어를 복사 |
| y | 특정한 다음 텍스트 복사 |
| yy | 커서가 있는 라인을 복사, 커서가 가리키는 곳으로 라인을 이동 |
| y) | 문자의 나머지 복사 |
| y} | 문단의 나머지 복사 |
| yG | 파일의 나머지 복사 |
| yH | 화면의 시작까지 복사 |
| yL | 화면의 나머지 복사 |


### 텍스트 이동

| 명령어 | 설명 |
|------|-----|
| p | 삭제나 복사된 텍스트를 커서가 있는 문자나 라인 뒤에 삽입 |
| P | 삭제나 복사된 텍스트를 커서가 있는 문자나 라인 앞에 삽입 |
| dw p | 커서가 있는 단어를 삭제한 후 이를 원하는 곳 커서 뒤로 삽입 |
| dw P | 커서가 있는 단어를 삭제한 후 이를 변경한 커서가 있는 곳으로 삽입 |
| d p | 지정한 다음 텍스트로 삭제한 후 커서가 가리키는 곳으로 이동 |
| d) P | 문장의 나머지로 이동 |
| d} p | 문단의 나머지로 이동 |
| dG P | 파일의 나머지로 이동 |
| dH P | 화면 시작 부분으로 이동 |
| dL P | 화면의 나머지를 이동 |


### vi 에디터 종료 마치기 명령

| 명령어 | 설명 |
|------|-----|
| :q | 그대로 종료하기 |
| :q! | 변경된 내용을 저장하지 않고 강제로 종료하기 |
| :wq | 변경된 내용을 저장하고 종료하기 |
| :x | :wq와 동일한 명령 |
| ZZ | :wq와 동일한 명령 |


### 검색

| 명령어 | 설명 |
|------|-----|
| /pattern | 텍스트에서 앞으로 패턴 검색 |
| >pattern | 텍스트에서 뒤로 패턴 검색 |
| n | 앞 또는 뒤로 이전 검색 반복 |
| N | 반대 방향으로 이전 검색 반복 |
| / | 전 검색을 앞으로 반복 |
| ? | 전 검색을 뒤로 반복 |


### 문자열 치환

| 명령어 | 설명 |
|------|-----|
| :s/old/new | 현재 행의 처음 old를 new로 교체 |
| :s/old/new/g | 현재 행의 모든 old를 new로 교체 |
| :10,20s/old/new/g | 10행부터 20행까지 모든 old를 new로 교체 |
| :-3,+4s/old/new/g | 현재 커서 위치에서 3행 위부터 4행 아래까지 old를 new로 교체 |
| :%s/old/new/g | 문서 전체에서 old를 new로 교체 |
| :%s/old/new/gc | 문서 전체에서 old를 new로 확인하며 교체 |
| :g/pattern/s/old/new/g | Pattern이 있는 모든 행의 old를 new로 교체 |
| :g/pattern/s//new/g | :%s/old/new/g와 동일 |


### 옵션

| 옵션 | 약어 | 기능 | 기본값 |
|----|----|----|----|
| autoindent | ai | 들여 쓰기 가능, 탭으로 들여 쓰기 범위 지정 | off |
| autoprint | ap | 줄이 바뀔 때 현재 줄을 화면상에서 출력 | on |
| errobells | ed | 명령 에러가 발생시 삑 소리나게 함 | off |
| number | nu | 줄 번호를 나타나게 함 | off |
| report | report | 편집시 메시지를 보낼 편집 변화 크기 지정 | 5 |
| showmatch | sm | 가로 닫기 괄호를 사용할 때 일치하는 가로 열기 괄호를 보여줌 | off |
| wam | wam | 저장하지 않고 vi 종료할 때 경고 메시지를 뿌려 줌 | on |
| ignorecase | ic | 검색 패턴에 사용되는 대소문자 구별하지 않음 | on |
| tabstopp=n | ts=n | 탭 공백을 n 수만큼 지정 | 8 |
| wrapmargin=n | wm=n | 텍스트 오른쪽 여백을 n 수만큼 지정 | 0 |


### Mark 사용

| 명령어 | 설명 |
|------|-----|
| mx | 현재 위치를 x 이름의 마크로 저장 |
| `` | 이전에 마크한 위치로 이동 |
| `x | 마크한 위치(행, 열)로 이동 |
| ‘’ | 이전에 마크한 줄로 이동 |
| ‘x | 마크한 줄로 이동 |


### Named Buffer 사용

| 명령어 | 설명 |
|------|-----|
| “ayy | 현재 줄을 "a 버퍼에 복사 |
| “Ayy | 기존의 버퍼에 현재 줄을 버퍼에 추가 |
| "ap | “a 버퍼에 복사된 데이터를 붙여 넣기 |
☞‘a’ 부터 ‘z’ 까지 사용가능


### 여러 문서 편집 ( vi filename1, filename2 … 로 실행 ; 여러 파일 열기)

| 명령어 | 설명 |
|------|-----|
| :n | vi로 open한 여러 파일중 다음 파일로 전환 |
| :N | vi로 open한 여러 파일중 이전 파일로 전환 |
| :4n | 여러 파일중 4개 파일 skip후 파일 Open |
| :args | 현재 열린 모든 파일중 현재 편집중인 파일 표시 |



## nano

### nano 단축키

[리눅스의 Nano 에디터 단축키](https://www.thewordcracker.com/miscellaneous/%EB%A6%AC%EB%88%85%EC%8A%A4%EC%9D%98-nano-%EC%97%90%EB%94%94%ED%84%B0-%EB%8B%A8%EC%B6%95%ED%82%A4/)

아래는 nano 에디터를 사용할 때 참고할 수 있는 유용한 단축키 목록입니다. (출처: http://staffwww.fullcoll.edu/sedwards/Nano/UsefulNanoKeyCommands.html)

자세한 사용법을 원하는 경우 nano가 실행된 상태에서 Ctrl+g를 누르면 도움말이 표시됩니다.


#### 전체 단축키 (영문)
전체 키보드 단축키는 다음을 참고해보세요:

**^** = **Ctrl** key **M** = **Alt** key

```
^G      (F1)            Display this help text
^X      (F2)            Close the current file buffer / Exit from nano
^O      (F3)            Write the current file to disk
^J      (F4)            Justify the current paragraph

^R      (F5)            Insert another file into the current one
^W      (F6)            Search for a string or a regular expression
^Y      (F7)            Move to the previous screen
^V      (F8)            Move to the next screen

^K      (F9)            Cut the current line and store it in the cutbuffer
^U      (F10)           Uncut from the cutbuffer into the current line
^C      (F11)           Display the position of the cursor
^T      (F12)           Invoke the spell checker, if available

^_      (F13)   (M-G)   Go to line and column number
^\      (F14)   (M-R)   Replace a string or a regular expression
^^      (F15)   (M-A)   Mark text at the cursor position
        (F16)   (M-W)   Repeat last search

M-^             (M-6)   Copy the current line and store it in the cutbuffer
M-}                     Indent the current line
M-{                     Unindent the current line

^F                      Move forward one character
^B                      Move back one character
^Space                  Move forward one word
M-Space                 Move back one word
^P                      Move to the previous line
^N                      Move to the next line

^A                      Move to the beginning of the current line
^E                      Move to the end of the current line
M-(             (M-9)   Move to the beginning of the current paragraph
M-)             (M-0)   Move to the end of the current paragraph
M-\             (M-|)   Move to the first line of the file
M-/             (M-?)   Move to the last line of the file

M-]                     Move to the matching bracket
M--             (M-_)   Scroll up one line without scrolling the cursor
M-+             (M-=)   Scroll down one line without scrolling the cursor

M-<             (M-,)   Switch to the previous file buffer
M->             (M-.)   Switch to the next file buffer

M-V                     Insert the next keystroke verbatim
^I                      Insert a tab at the cursor position
^M                      Insert a newline at the cursor position
^D                      Delete the character under the cursor
^H                      Delete the character to the left of the cursor
M-T                     Cut from the cursor position to the end of the file

M-J                     Justify the entire file
M-D                     Count the number of words, lines, and characters
^L                      Refresh (redraw) the current screen

M-X                     Help mode enable/disable
M-C                     Constant cursor position display enable/disable
M-O                     Use of one more line for editing enable/disable
M-S                     Smooth scrolling enable/disable
M-P                     Whitespace display enable/disable
M-Y                     Color syntax highlighting enable/disable

M-H                     Smart home key enable/disable
M-I                     Auto indent enable/disable
M-K                     Cut to end enable/disable
M-L                     Long line wrapping enable/disable
M-Q                     Conversion of typed tabs to spaces enable/disable

M-B                     Backup files enable/disable
M-F                     Multiple file buffers enable/disable
M-M                     Mouse support enable/disable
M-N                     No conversion from DOS/Mac format enable/disable
M-Z                     Suspension enable/disable
```


#### nano 단축키 (한글)
##### 파일 관리
| 작업 | 단축키/명령어 |
|------|-----|
| nano 내에서 파일 열기 | Ctrl+r <br> 이 명령어를 입력하면 화면 아래에 새로운 메뉴 항목이 표시됩니다. 예를 들어, Ctrl+T를 누르면 파일 시스템을 탐색하여 파일을 찾아서 열 수 있습니다. |
| 다음 파일 버퍼 표시 | lt+> |
| 이전 파일 버퍼 표시 | Alt+< |
| 현재 파일을 디스크에 저장 | Ctrl+o |
| 현재 파일 버퍼 종료 | Ctrl+x <br> 파일이 저장되지 않았다면 저장할 것인지 물어옵니다. 파일 버퍼가 하나만 열려 있는 경우 파일 버퍼를 종료하면 nano에서 나가게 됩니다. |

##### 복사 및 붙여넣기
| 작업 | 단축키/명령어 |
|------|-----|
| 자르기 또는 붙여넣기 작업을 할 영역 선택 | Alt+a <br> Alt+a로 마크를 설정한 후에 커서를 이동시켜 영역을 지정합니다. 커서를 움직일 때 하이라이트됩니다. 또한, 영역 지정을 취소하려면 Alt+a를 다시 누르면 됩니다. |
| 강조 표시된 영역을 클립보드에 복사 | Alt+^ |
| 강조 표시된 영역을 잘라서 클립보드에 저장 | Ctrl+k <br> 라인을 삭제(정확하게는 자르기)할 때에도 사용 |
| 클립보드의 내용을 현재 커서 위치에 붙여넣기 | Ctrl+u |
| 현재 커서 위치에서 라인의 끝(EOL)까지 자르기 | Ctrl+k <br> 이 명령어는 영역을 강조표시할 필요가 없습니다. |

##### 코드 탐색
| 작업 | 단축키/명령어 |
|------|-----|
| 파일의 시작 부분으로 이동 | Alt+\ |
| 파일의 끝으로 이동 | Alt+/ |
| 한 화면 앞으로 이동(아래로 이동) | Ctrl+v |
| 한 화면 뒤로 이동(위로 이동) | Ctrl+y |
| 대상 라인 번호로 이동(라인 번호를 입력하여 곧바로 이동) | Alt+g |
| 짝을 이루는 열린/닫힌 기호로 곧바로 이동 | Alt+] <br> 일치하지 않는 괄호(brace) 컴파일러 오류를 찾을 때 매우 유용 |
| 창 스크롤 | Alt+= 아래로 스크롤 <br> Alt+- 위로 스크롤 |
| 블록 들여쓰기/내어쓰기 | Alt+a 를 사용하여 블록을 선택한 다음 <br> - Alt+} 선택한 블록 들여쓰기 <br> - Alt+{ 선택한 블록 내어쓰기 |

##### 찾기 및 바꾸기
| 작업 | 단축키/명령어 |
|------|-----|
| 대상 문자열 검색  | Ctrl+w <br> 이 명령어를 입력하면 화면 하단에 새로운 메뉴 항목이 표시됩니다. 예: Alt+B를 누르면 역방향 검색 전환, Ctrl+R:  검색 문자열을 다른 문자열로 바꾸기 |
| 마지막 검색 반복 | Alt+w |
| 다음 검색에 대한 방향 토글(전환) | Ctrl+w를 누른 다음 Ctrl+b |
| 찾아서 바꾸기 | Alt+r |

##### 명명된 키에 해당하는 명령어
| 작업 | 단축키/명령어 |
|------|-----|
| Home | Ctrl+a |
| End | Ctrl+e |
| Page Up | Ctrl+y |
| Page Down | Ctrl+v |
| 화살표 키 | Ctrl+f (오른쪽), Ctrl+b (왼쪽), Ctrl+n (아래), Ctrl+p (위) |
| Tab | Ctrl+i |
| Backspace | Ctrl+h |
| Delete | Ctrl+d |
| Return | Ctrl+m |

### 참고
nano가 실행된 상태에서 Ctrl+g를 누르면 도움말이 표시됩니다.

nano에서 라인 번호를 표시하려면 파일을 열 때 -c를 추가합니다.

```
nano -c filename
```

또는, /etc/nanorc에서 # set const를 찾아서 주석 기호를 제거하면 항상 커서 위치의 라인 번호가 표시됩니다.



하지만 왼쪽에 라인 번호를 표시하는 기능은 없다고 합니다.


##

[리눅스 쉘(bash), 기본 명령어 이해 및 실습](http://www.fun-coding.org/linux_basic2.html)


## shell
[쉘 명령어](http://12bme.tistory.com/240)
