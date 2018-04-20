~~~
^[ \t]+\n  \n
\n+```nodejs  \n\n\n```javascript\n// [[nodejs]]\n
\n+```c\+\+  \n\n\n```c++\n// [[c++]]\n
\n+```swift  \n\n\n```swift\n// [[swift]]\n
\n+## +  \n\n\n\n##
\n+(문제|입력|출력)$  \n\n#### $1
\n예제 입력 (\d+) *$  \n\n~~~\n#### 예제 입력 $1\n~~~\n
\n예제 출력 (\d+) *$  \n\n~~~\n#### 예제 출력 $1\n~~~\n
\n힌트  \n~~~\n\n#### 힌트
~~~\n#### 예제 입력 1\n  \n#### 예제 입력 1\n
\n\n~~~  \n~~~\n
\n+(출처|보기|메모)$  \n\n#### $1
\n+비슷한 문제  \n\n#### 비슷한 문제
\n+알고리즘 분류 * \n\n#### 알고리즘 분류
```([a-zA-Z])  #### 풀이\n``$1
~~~



## 입/출력 받아보기
입력과 출력만 사용하는 문제들로 입출력을 해봅니다

### 2557  Hello World [#]
Hello World! 를 화면에 출력하는 문제

#### 문제
Hello World!를 출력하시오.

#### 입력
없음

#### 출력
Hello World!를 출력하시오.


#### 예제 입력 1
~~~
~~~

#### 예제 출력 1
~~~
Hello World!
~~~

#### 힌트

#### 알고리즘 분류
출력

#### 메모
- 모든 프로그래밍 언어의 입구 : 1st Problem
- 출력함수 기본 예제 Hello World!
- nodejs:: memory: 720268 KB
- swift:: memory: 1984 KB
- c++17:: memory: 60068 KB
- nodejs, swift는 memory를 어마어마~하게 잡아먹는다.
- c++:: <iostream> vs. <cstdio> [!]
- c++:: cout vs. printf [!]

#### 풀이 1
```javascript
// [[nodejs]]

console.log("Hello World!")
```


#### 풀이 2
```swift
// [[swift]]

print("Hello World!")
```


#### 풀이 3
```c++
// [[c++]]

#include <iostream>

int main() {
  std::cout << "Hello World!\n";
  return 0;
}
```

### 1000  A+B [#]
두 수를 입력받고 합을 출력하는 문제

#### 문제
두 수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A+B를 출력한다.


#### 예제 입력 1
~~~
1 2
~~~

#### 예제 출력 1
~~~
3
~~~

#### 힌트
[여기](https://www.acmicpc.net/help/language)를 누르면 1000번 예제 소스를 볼 수 있습니다.

#### 출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: doju

#### 비슷한 문제
1001번. A-B
1008번. A/B
2558번. A+B - 2
10950번. A+B - 3
10951번. A+B - 4
10952번. A+B - 5
10953번. A+B - 6
10998번. A×B
11021번. A+B - 7
11022번. A+B - 8

#### 알고리즘 분류
사칙연산
수학

#### 메모
- +입력문, +사칙연산
- nodejs:: memory: 721440 KB
- swift:: memory: 60092 KB
- c++17:: memory: 1984 KB
- c++:: cin vs. scanf [!]
- c++:: using namespace std [!]

#### 풀이
```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a+b);
```


#### 풀이
```swift
// [[swift]]

let input =  readLine()!

let arr = input.split(separator: " ")

var a: Int = Int(arr[0])!
var b: Int = Int(arr[1])!

print(String(a+b))
```


#### 풀이
```c++
// [[c++]]

#include <iostream>
using namespace std;

int main() {
  auto a=0, b=0;
  cin >> a >> b;
  cout << a+b << endl;
  return 0;
}


// scanf, printf
#include <iostream>

int main() {
  int a, b;
  scanf("%d %d",&a,&b);
  printf("%d\n",a+b);
  return 0;
}
```

### 1001  A-B
두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제

#### 문제
A-B를 계산하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0< A, B < 10)

#### 출력
첫째 줄에 A-B를 출력한다.


#### 예제 입력 1
~~~
3 2
~~~

#### 예제 출력 1
~~~
1
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 비슷한 문제
1000번. A+B
1008번. A/B
10998번. A×B

#### 알고리즘 분류
사칙연산
수학

#### 메모
- nodejs:: memory: 720268 KB
- swift:: memory: 60092 KB

#### 풀이
```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a-b);
```


#### 풀이
```swift
// [[swift]]

let input =  readLine()!

let arr = input.split(separator: " ")

var a: Int = Int(arr[0])!
var b: Int = Int(arr[1])!

print(String(a-b))
```



### 7287  등록
자신이 acmicpc.net에서 푼 문제의 수와 acmicpc.net 아이디를 출력하는 문제

#### 문제
자신이 온라인 저지에서 맞은 문제의 개수와 아이디를 그대로 출력하는 프로그램을 작성하시오.

#### 입력
이 문제는 입력이 없다.

#### 출력
첫 줄에 자신이 맞은 문제의 수, 둘째 줄에 아이디를 출력한다.


#### 예제 입력 1
~~~
~~~

#### 예제 출력 1
~~~
123
Your_ICPC_Team_Name
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2013 J번

ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2014 H번

ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2015 K번

ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2016 K번

ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2017 K번

데이터를 만든 사람: baekjoon

#### 알고리즘 분류

#### 출력

#### 메모
- [BAEKJOON](https://www.acmicpc.net/)에서 맞은 문제 개수, 아이디를 찾아넣기
- crawling으로 자동으로 넣는 방법은? [!]

#### 풀이
```javascript
// [[nodejs]]

console.log("3\nhopelife")
```


#### 풀이
```swift
// [[swift]]

print("8\nhopelife")
```



### 10172  개 [#]
그림을 출력하는 문제

#### 문제
아래 예제와 같이 개를 출력하시오.

#### 입력
없음.

#### 출력
개를 출력한다.


#### 예제 입력 1
~~~
~~~

#### 예제 출력 1
~~~
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
~~~

#### 힌트

#### 출처
High School > PLU High School Programming Contest > PLU 2014 - Novice 3번

#### 알고리즘 분류

#### 출력

#### 메모
- 문자열 표시법
- 언어별 ", ' 사용법/처리법 [!]

#### 풀이
```javascript
// [[nodejs]]

console.log('|\\_/|\n|q p|   \/}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\\__|');
```


#### 풀이
```swift
// [[swift]]

print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
```


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  std::cout << "|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|\n";
  return 0;
}
```


### 10718 We love kriii
주어진 문자를 출력하는 문제1

#### 문제
ACM-ICPC 인터넷 예선, Regional, 그리고 World Finals까지 이미 2회씩 진출해버린 kriii는 미련을 버리지 못하고 왠지 모르게 올 해에도 파주 World Finals 준비 캠프에 참여했다.

대회를 뜰 줄 모르는 지박령 kriii를 위해서 격려의 문구를 출력해주자.

#### 입력
본 문제는 입력이 없다.

#### 출력
두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.


#### 예제 입력 1
~~~
~~~

#### 예제 출력 1
~~~
강한친구 대한육군
강한친구 대한육군
~~~

#### 힌트

#### 출처
Contest > Coder's High > Coder's High 2015 Side Contest P1번

문제를 만든 사람: tae

#### 알고리즘 분류

#### 출력

#### 메모
- 개행문자(줄바꿈) 처리방법

#### 풀이
```javascript
// [[nodejs]]

console.log("강한친구 대한육군\n강한친구 대한육군");
```


#### 풀이
```swift
// [[swift]]

print("강한친구 대한육군\n강한친구 대한육군")
```

#### 메모

### 11718 그대로 출력하기 [#]
입력받은 문자를 출력하는 문제1

#### 문제
입력 받은 대로 출력하는 프로그램을 작성하시오.

#### 입력
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

#### 출력
입력받은 그대로 출력한다.


#### 예제 입력 1
~~~
Hello
Baekjoon
Online Judge
~~~

#### 예제 출력 1
~~~
Hello
Baekjoon
Online Judge
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모
- 여러줄을 한꺼번에 입력하는 방법은 아님
- scanf, printf로 구현해볼 것 [!]

#### 풀이
```c++
// [[c++]]

#include<iostream>

#include<string>
using namespace std;

int main() {
  string a;

  for (int i = 0; i < 100; ++i) {
    getline(cin, a);
    if (a == "") break;
    cout << a << endl;
  }
}
```



### 11719 그대로 출력하기 2 [#]
입력받은 문자를 출력하는 문제2

#### 문제
입력 받은 대로 출력하는 프로그램을 작성하시오.

#### 입력
입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄이 주어질 수도 있고, 각 줄의 앞 뒤에 공백이 있을 수도 있다.

#### 출력
입력받은 그대로 출력한다.


#### 예제 입력 1
~~~
    Hello

Baekjoon
   Online Judge
~~~

#### 예제 출력 1
~~~
    Hello

Baekjoon
   Online Judge
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모
- 공백문자(띄어쓰기)가 있는 경우의 입력
- scanf, printf 시도해 볼 것 [!]

#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <string>

using namespace std;

int main() {
  char a;
  a = getchar();

  while (a != -1) {
    putchar(a);
    a = getchar();
  }

  return 0;
}
```



## 사칙연산 도전하기
덧셈, 뺄셈, 곱셈, 나눗셈, 나머지 연산을 사용해 봅니다


### 1000  A+B [@]
두 수의 덧셈

#### 메모
- 입/출력 받아보기 1000번과 중복



### 1001  A-B [@]
두 수의 뺄셈


#### 메모
- 입/출력 받아보기 1001번과 중복



### 10998 A×B
두 수의 곱셈

#### 문제
두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A×B를 출력한다.


#### 예제 입력 1
~~~
1 2
~~~

#### 예제 출력 1
~~~
2
~~~

#### 예제 입력 2
~~~
3 4
~~~

#### 예제 출력 2
~~~
12
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 비슷한 문제
1000번. A+B
1001번. A-B
1008번. A/B

#### 알고리즘 분류
사칙연산

#### 메모
- trivial

#### 풀이
```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a*b);
```



### 1008  A/B
두 수의 나눗셈

#### 문제
A/B를 계산하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A/B를 출력한다. 절대/상대 오차는 10-9 까지 허용한다.


#### 예제 입력 1
~~~
1 3
~~~

#### 예제 출력 1
~~~
0.33333333333333333333333333333333
~~~

#### 예제 입력 2
~~~
4 5
~~~

#### 예제 출력 2
~~~
0.8
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 비슷한 문제
1000번. A+B
1001번. A-B
10998번. A×B

#### 알고리즘 분류
사칙연산
수학

#### 메모
- trivial


#### 풀이
```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a/b);
```



### 10869 사칙연산
모든 사칙연산 해보기

#### 문제
두 자연수 A와 B가 주어진다. 이 때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

#### 입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

#### 출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.


#### 예제 입력 1
~~~
7 3
~~~

#### 예제 출력 1
~~~
10
4
21
2
1
~~~

#### 힌트

#### 알고리즘 분류
사칙연산

#### 메모
- nodejs로는 실패


#### 풀이
```swift
// [[swift]]

let input =  readLine()!

let arr = input.split(separator: " ")

var a: Int = Int(arr[0])!
var b: Int = Int(arr[1])!

print(String(a+b))
print(String(a-b))
print(String(a*b))
print(String(a/b))
print(String(a%b))
```



### 10430 나머지
나머지 연산을 하고 계산한 결과와 계산을 한 결과를 나머지 연산한 결과가 같은지를 살펴봅니다

#### 문제
(A+B)%C는 (A%C + B%C)%C 와 같을까?

(A×B)%C는 (A%C × B%C)%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

#### 출력
첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.


#### 예제 입력 1
~~~
5 8 4
~~~

#### 예제 출력 1
~~~
1
1
0
0
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류
사칙연산
나머지 연산

#### 메모
- %(mod, 나머지 연산) 의미, 사용법


#### 풀이
```swift
// [[swift]]

let input =  readLine()!

let arr = input.split(separator: " ")

var a: Int = Int(arr[0])!
var b: Int = Int(arr[1])!
var c: Int = Int(arr[2])!

print(String((a+b)%c))
print(String((a%c+b%c)%c))
print(String((a*b)%c))
print(String((a%c*b%c)%c))
```



### 2558  A+B - 2
두 수의 입력을 받아 더한 값을 출력하는 문제

#### 문제
A+B를 계산하시오.

#### 입력
첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A+B를 출력한다.


#### 예제 입력 1
~~~
1
2
~~~

#### 예제 출력 1
~~~
3
~~~

#### 힌트

#### 비슷한 문제
1000번. A+B
10950번. A+B - 3
10951번. A+B - 4
10952번. A+B - 5
10953번. A+B - 6
11021번. A+B - 7
11022번. A+B - 8

#### 메모
- trivial


#### 풀이
```swift
// [[swift]]

var input: Array<Int> = []

for _ in 1...2 {
  input.append(Int(readLine()!)!)
}

print(String(input[0]+input[1]))
```



### 2839  설탕 배달
나누기, 나머지 연산을 이용하는 문제

설탕 배달 성공
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 128 MB  47132 11575 9491  27.083%

#### 문제
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

#### 출력
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


#### 예제 입력 1
~~~
18
~~~

#### 예제 출력 1
~~~
4
~~~

#### 예제 입력 2
~~~
4
~~~

#### 예제 출력 2
~~~
-1
~~~

#### 예제 입력 3
~~~
6
~~~

#### 예제 출력 3
~~~
2
~~~

#### 예제 입력 4
~~~
9
~~~

#### 예제 출력 4
~~~
3
~~~

#### 예제 입력 5
~~~
11
~~~

#### 예제 출력 5
~~~
3
~~~

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2010/2011 > Contest #7 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013

#### 알고리즘 분류
수학
구현

#### 메모
- 최소값 구하기
- 5킬로그램 봉지를 최대한 많이 쓰자.
- 반복문 최소화(5회) [!]


#### 풀이
```swift
// [[swift]]

func main(m: Int) -> Int {
  var n: Int = m
  var b: Int = 0

  for _ in 0...4 {
    if n%5 == 0 {
      //print(String(b + n/5))
      return b + n/5
    }
    if (n > 2) {
      n -= 3
      b += 1
    } else {
      return -1
    }
  }
  return -1
}

print(String(main(m: Int(readLine()!)!)))
```



## for문 사용해보기
for문을 사용해 봅니다

### 2741  N 찍기
1부터 N까지 숫자를 한 줄에 하나씩 출력해봅니다

#### 문제
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
1
2
3
4
5
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 비슷한 문제
2742번. 기찍 N

#### 알고리즘 분류

#### 출력

#### 메모
- for(반복문) 기본문


#### 풀이
```swift
// [[swift]]

let n = Int(readLine()!)!

for i in 1...n {
   print(String(i))
}
```



### 2742  기찍 N
N부터 1까지 숫자를 한 줄에 하나씩 출력해봅니다

기찍 N 성공
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 128 MB  28244 17938 16509 65.284%

#### 문제
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
5
4
3
2
1
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 비슷한 문제
2741번. N 찍기

#### 알고리즘 분류

#### 출력

#### 메모


#### 풀이
```swift
// [[swift]]

let n = Int(readLine()!)!

for i in (1...n).reversed() {
    print(String(i))
}
```



### 2739  구구단
구구단을 출력해봅니다

#### 문제
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

#### 입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

#### 출력
출력형식과 같게 N*1부터 N*9까지 출력한다.


#### 예제 입력 1
~~~
2
~~~

#### 예제 출력 1
~~~
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
~~~

#### 힌트

#### 알고리즘 분류

#### 출력

#### 메모
- for(반복문)의 전형적 문제


#### 풀이
```swift
// [[swift]]

let n = Int(readLine()!)!

for i in (1...9) {
    print("\(n) * \(i) = \(n*i)")
}
```



### 2438  별찍기 - 1
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개 출력해 봅니다

#### 문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

#### 입력
첫째 줄에 N (1<=N<=100)이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
*
**
***
****
*****
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: grace0068 hchanhong

#### 알고리즘 분류

#### 출력

#### 메모


#### 풀이
```swift
// [[swift]]

let n = Int(readLine()!)!

for i in 1...n {
  for _ in 1...i {
      print("*", terminator:"")
  }
  //print("\n", terminator:"")
  print("")
}
```



### 2439  별찍기 - 2
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개 출력해 봅니다. (오른쪽 정렬)

#### 문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별 (예제 참고)을 출력하시오.

#### 입력
첫째 줄에 N (1<=N<=100)이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
    *
   **
  ***
 ****
*****
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: namnamseo

#### 알고리즘 분류

#### 출력

#### 메모
- 공백문자 처리 방법이 여러 가지 있을 듯 [!]


#### 풀이
```swift
// [[swift]]

let n: Int = Int(readLine()!)!

for i in 1...n {
  print(String(repeating: " ", count: n-i) + String(repeating: "*", count: i))
}
```



### 2440  별찍기 - 3
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 출력해 봅니다.

#### 문제
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

#### 입력
첫째 줄에 N (1<=N<=100)이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
*****
****
***
**
*
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
잘못된 데이터를 찾은 사람: jms100300

#### 알고리즘 분류

#### 출력

#### 메모
- for문 내림차순으로 돌리기


#### 풀이
```swift
// [[swift]]

let n: Int = Int(readLine()!)!

for i in (1...n).reversed() {
  print(String(repeating: "*", count: i))
}
```



### 2441  별찍기 - 4
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 출력해 봅니다. (오른쪽 정렬)

#### 문제
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

하지만, 오른쪽을 기준으로 정렬한 별 (예제 참고)을 출력하시오.

#### 입력
첫째 줄에 N (1<=N<=100)이 주어진다.

#### 출력
첫째 줄부터 N번째 줄 까지 차례대로 별을 출력한다.


#### 예제 입력 1
~~~
5
~~~

#### 예제 출력 1
~~~
*****
 ****
  ***
   **
    *
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모
- 공백문자 + 거꾸로


#### 풀이
```swift
// [[swift]]

let n: Int = Int(readLine()!)!

for i in (1...n).reversed() {
  print(String(repeating: " ", count: n-i) + String(repeating: "*", count: i))
}
```



### 1924  2007년
2007년 x월 y일이 무슨 요일인지 알아내보기

#### 문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

#### 입력
첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

#### 출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.


#### 예제 입력 1
~~~
1 1
~~~

#### 예제 출력 1
~~~
MON
~~~

#### 힌트

#### 알고리즘 분류
구현

#### 메모
- 배열 사용하지 않는 방법이 있을까? [!]


#### 풀이
```swift
// [[swift]]

let dates: Array<Int> = [0,31,28,31,30,31,30,31,31,30,31,30,31]
let days: Array<String> = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
var diff: Int = 0

func getDay(_ month: Int, _ date: Int) -> Int {
    for i in 0...month-1 {
        diff += dates[i]
    }

    return diff + date
}

func getDate(_ diff: Int) -> String {
  return days[diff%7]
}

let input =  readLine()!
let arr = input.split(separator: " ")

var month: Int = Int(arr[0])!
var date: Int = Int(arr[1])!

print(getDate(getDay(month, date)))
```



### 8393  합
1부터 N까지 합을 구합니다

#### 문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

#### 출력
1부터 n까지 합을 출력한다.


#### 예제 입력 1
~~~
3
~~~

#### 예제 출력 1
~~~
6
~~~

#### 힌트

#### 출처
Contest > Algorithmic Engagements > PA 2006 0-1번

문제를 번역한 사람: baekjoon

#### 메모
- for문 전형적 학습 문제


#### 풀이
```swift
// [[swift]]

let n: Int = Int(readLine()!)!
var sum: Int = 0

for i in 1...n {
  sum += i
}

print(String(sum))
```



### 11720 숫자의 합
주어진 수를 모두 더하는 문제

#### 문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

#### 출력
입력으로 주어진 숫자 N개의 합을 출력한다.


#### 예제 입력 1
~~~
1
1
~~~

#### 예제 출력 1
~~~
1
~~~

#### 예제 입력 2
~~~
5
54321
~~~

#### 예제 출력 2
~~~
15
~~~

#### 예제 입력 3
~~~
25
7000000000000000000000000
~~~

#### 예제 출력 3
~~~
7
~~~

#### 예제 입력 4
~~~
11
10987654321
~~~

#### 예제 출력 4
~~~
46
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: jh05013

#### 알고리즘 분류

#### 출력

#### 메모
- 문자열 자르기 + 문자 -> 숫자 [!]


#### 풀이
```swift
// [[swift]]

var input: Array<Int> = []
var n: Int = 0
var nArray: Array<Character?> = []
var sum = 0

for i in 1...2 {
    if (i==1) {
        n = Int(readLine()!)!
    } else {
        nArray = Array(readLine()!)
    }
}

for i in 0..<n {
    sum += Int(String(nArray[i]!))!
}

print(sum)
```


### 11721 열 개씩 끊어 출력하기

#### 문제
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 단어가 주어진다. 단어는 알파벳 소문자와 대문자로만 이루어져 있으며, 길이는 100을 넘지 않는다. 길이가 0인 단어는 주어지지 않는다.

#### 출력
입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 미만의 글자만 출력할 수도 있다.


#### 예제 입력 1
~~~
BaekjoonOnlineJudge
~~~

#### 예제 출력 1
~~~
BaekjoonOn
lineJudge
~~~

#### 예제 입력 2
~~~
OneTwoThreeFourFiveSixSevenEightNineTen
~~~

#### 예제 출력 2
~~~
OneTwoThre
eFourFiveS
ixSevenEig
htNineTen
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: eric00513

#### 알고리즘 분류

#### 출력

#### 메모
- 문자열 일정 개수로 자르기
- c++로 구현해 볼 것 [!]


#### 풀이
```swift
// [[swift]]
3
let input: String = readLine()!

var len = input.characters.count
var n: Int = Int(len/10)

for i in 0...n {
  if (i < n) {
    let index0 = input.index(input.startIndex, offsetBy: i*10)
    let index1 = input.index(input.startIndex, offsetBy: i*10+10)
    print(input[index0..<index1])
  } else if len%10 != 0 {
    let index2 = input.index(input.startIndex, offsetBy: i*10)
    let index3 = input.index(input.endIndex, offsetBy: 0)
    print(input[index2..<index3])
  }
}
```


### 15552 빠른 A+B

#### 문제
본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 cin/cout을 사용하고자 한다면, cin.tie(NULL)과 sync_with_stdio(false)를 먼저 적용해 주자. 단, 이렇게 하면 더 이상 scanf/printf/puts/getchar/putchar 등 C의 입출력 방식을 사용하면 안 된다. 또한 endl 대신 개행문자를 쓰자.

Java를 사용하고 있다면, Scanner와 System.out.println 대신 BufferedReader와 BufferedWriter를 사용할 수 있다. BufferedWriter.flush는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이 때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다. 이 문제는 메모리 제한이 작아서 테스트케이스를 전부 저장할 수 없도록 설계되었다.

자세한 설명 및 기타 BOJ 팁은 [이 글](https://www.acmicpc.net/blog/view/55)을 참고하자.

#### 입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

#### 출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.


#### 예제 입력 1
~~~
5
1 1
12 34
5 500
40 60
1000 1000
~~~

#### 예제 출력 1
~~~
2
46
505
100
2000
~~~

#### 힌트

#### 출처
문제를 만든 사람: jh05013

#### 메모
- 해당 언어에서 가장 빠른 구현법은?
- 메모리를 아끼자!
- cio/cout vs scanf/printf [!]
- cin/cout 사용시 적용하면 좋은 조건? [!]


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  int t, a, b;
  scanf("%d",&t);

  while(t--) {
    scanf("%d %d",&a,&b);
    printf("%d\n",a+b);
  }

  return 0;
}
```



## if문 사용해보기

### 9498 시험성적
시험 점수를 입력받고 성적 출력해보기

#### 문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 자연수이다.

#### 출력
시험 성적을 출력한다.


#### 예제 입력 1
~~~
100
~~~

#### 예제 출력 1
~~~
A
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류
구현

#### 메모
- if/else문 기본 문제
- switch/case문으로 구현해 볼 것 [!]


#### 풀이
```swift
// [[swift]]

let input: Int = Int(readLine()!)!
var grade: String = "F"

if input >= 90 {
  grade = "A"
} else if (input >= 80) {
  grade = "B"
}  else if (input >= 70) {
  grade = "C"
} else if (input >= 60) {
  grade = "D"
} else {
  grade = "F"
}

print(grade)

```


### 10817 세 수
세 정수 A, B, C중에 두 번째로 큰 정수 찾아보기

#### 문제
세 정수 A, B, C가 주어진다. 이 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

#### 출력
두 번째로 큰 정수를 출력한다.


#### 예제 입력 1
~~~
20 30 10
~~~

#### 예제 출력 1
~~~
20
~~~

#### 예제 입력 2
~~~
30 30 10
~~~

#### 예제 출력 2
~~~
30
~~~

#### 예제 입력 3
~~~
40 40 40
~~~

#### 예제 출력 3
~~~
40
~~~

#### 예제 입력 4
~~~
20 10 10
~~~

#### 예제 출력 4
~~~
10
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모
- 기본 정렬법 [!]
- 변수값 바꾸기(swap) 기능 구현법 [!]


#### 풀이
```swift
// [[swift]]
3
//not success on baekjoon but not error!!
//swap function
let input =  readLine()!
let arr = input._split(separator: " ")

var s: Array<Int> = [Int(arr[0])!, Int(arr[1])!, Int(arr[2])!]
var temp: Int = 0

func swapArr(_ i: Int, _ j: Int) {
  temp = s[i]
  s[i] = s[j]
  s[j] = temp
}

if (s[0] > s[1]) {
  swapArr(0, 1)
}

if (s[1] > s[2]) {
  swapArr(1, 2)
}

if (s[0] > s[1]) {
  swapArr(0, 1)
}

print(s)
```


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  int a, b, c, t;
  scanf("%d %d %d", &a, &b, &c);
  if (a > b) {
    t = a; a = b; b = t;
  }
  if (b > c) {
    t = b; b = c; c = t;
  }
  if (a > b) {
    t = a; a = b; b = t;
  }

  printf("%d\n", b);
  return 0;
}


//use swap function
#include <iostream>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  if (a > b) {
    std::swap(a, b);
  }
  if (b > c) {
    std::swap(b, c);
  }
  if (a > b) {
    std::swap(a, b);
  }

  printf("%d\n", b);
  return 0;
}

void swap(int *i, int *j) {
  int t;
  t = *i;
  *i = *j;
}
```

### 10871  X보다 작은 수
정수 N개 중에서 X보다 작은 수 모두 출력해보기

#### 문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이 때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

#### 출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.


#### 예제 입력 1
~~~
10 5
1 10 4 9 2 3 8 5 7 6
~~~

#### 예제 출력 1
~~~
1 4 2 3
~~~

#### 힌트

#### 출처
문제의 오타를 찾은 사람: jh82582 thinksong1

#### 알고리즘 분류

#### 보기

#### 메모
- 크기 비교


#### 풀이
```c++
// [[c++]]

//cin, cout
#include <iostream>
using namespace std;

int main () {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N, X;
  cin>>N>>X;
  int* arr = new int[N];

  for (int i = 0 ; i < N ; i++)
    cin>>arr[i];

  for (int i = 0 ; i < N ; i++)
    if ( X > arr[i] )
      cout<<arr[i]<<' ';

  cout<<'\n';

  return 0;
}


//scanf, printf
#include <iostream>
using namespace std;

int main() {
  int n,m,x;
  scanf("%d %d",&n,&m);

  for(int i=0;i<n;++i){
    scanf("%d",&x);
    if(x<m)printf("%d ",x);
  }
}
```


### 1546 평균
최대값을 찾아, 그 값으로 다른 값들을 바꾼 후 평균을 구하는 문제

#### 문제
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최대값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

#### 출력
첫째 줄에 새로운 평균을 출력한다. 정답과의 절대/상대 오차는 10-2까지 허용한다.


#### 예제 입력 1
~~~
3
40 80 60
~~~

#### 예제 출력 1
~~~
75.00
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: ho94949
빠진 조건을 찾은 사람: powdragon1

#### 메모
- 평균 + 조건에 따른 변수값 변경


#### 풀이
```c++
// [[c++]]

#include <iostream>
using namespace std;

int main () {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  //cout.setf(ios_base::showpoint);
  cout.setf(ios::fixed);
  cout.precision(2);

  int n;
  int s = 0;
  int max = 0;

  cin>>n;
  int* arr = new int[n];

  for (int i = 0; i < n; i++) {
    cin>>arr[i];
    if (arr[i] > max) {
      max = arr[i];
    }
  }

  for (int i=0 ; i<n; i++) {
      s += arr[i]*100/max;
  }

  cout<< (float)s/n;

  return 0;
}


//scanf, printf
//#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  int N = 0;
  scanf("%d", &N);
  double* sub = new double[N];

  for(int i = 0; i<N; i++) {
    scanf("%lf",&sub[i]);
  }

  double max = sub[0];
  double sum = 0;

  for (int i = 0; i < N; i++) {
    if (max < sub[i]) {
      max = sub[i];
    }
  }

  for (int i = 0; i < N; i++) {
    sum += 100*sub[i]/max;
  }

  printf("%.2lf", sum/N);

  return 0;
}
```


### 4344 평균은 넘겠지 [#]
평균이 넘는 학생들의 퍼센테이지를 출력하는 문제

#### 문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

#### 입력
첫째 줄에는 테스트케이스 C가 주어진다.

둘째 줄부터 각 테스트케이스 마다 첫 수로 정수 N(1 <= N <= 1000)명의 학생이 주어지고 그 다음으로 N명의 0부터 100 사이의 점수가 이어서 주어진다.

#### 출력
각 케이스마다 한줄씩 평균을 넘는 학생들의 비율을 소수점 넷째자리에서 반올림하여 출력한다.


#### 예제 입력 1
~~~
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
~~~

#### 예제 출력 1
~~~
40.000%
57.143%
33.333%
66.667%
55.556%
~~~

#### 힌트

#### 출처
Contest > Waterloo's local Programming Contests > 28 September, 2002 D번

문제를 번역한 사람: busyhuman
문제의 오타를 찾은 사람: choiking10
링크
PKU Judge Online
ZJU Online Judge
TJU Online Judge

#### 메모
- 평균 + 값 비교


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  int T, N, i, j, k;
  //int T, N, i, j, k, score[1001] = {0, };

  scanf("%d", &T);

  for(i = 0; i < T; i++){
    int sum = 0, cnt = 0;
    double avg = 0.0;

    scanf("%d", &N);
    int* score = new int[N];

    for(j = 0; j < N; j++){
      scanf("%d", &score[j]);
      sum += score[j];
    }

    avg = (double)sum / (double)N;

    for(k = 0; k < N; k++){
      if(avg < score[k])
        cnt++;
    }

    avg = (double)cnt / (double)N;

    printf("%.3lf%\n", avg * 100);
  }

  return 0;
}

```


### 더하기 사이클 [#]
조건을 만족할 때까지 계속 더하는 문제

#### 문제
0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 숫자와 앞에서 구한 합의 가장 오른쪽 자리 숫자를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

26부터 시작한다. 2+6 = 8이다. 새로운 숫자는 68이다. 6+8 = 14이다. 새로운 숫자는 84이다. 8+4 = 12이다. 새로운 숫자는 42이다. 4+2 = 6이다. 새로운 숫자는 26이다.

위의 예는 4번만에 원래 숫자로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

#### 출력
첫째 줄에 N의 사이클 길이를 출력한다.


#### 예제 입력 1
~~~
26
~~~

#### 예제 출력 1
~~~
4
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: doju

#### 알고리즘 분류

#### 보기

#### 메모
- 자리수 구현 [!]
- floor() vs (int) [!]
- (int)로 구현해 볼 것 [!]


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <cmath>

int main() {
  int N, M, c=0;
  scanf("%d", &N);

  M = N;

  while(1) {
    M = 10*(M%10) + int((floor(M/10) + M%10))%10;
    c++;
    //printf("N: %d M: %d c: %d\n",N, M, c);
    if (M == N) {
      printf("%d",c);
      return 0;
    }
  }

}
```



## 함수 사용하기 [#]

### 4673 셀프 넘버
자연수 n에 대해 d(n)의 값을 구하는 함수를 정의해 문제를 해결해봅니다

#### 문제
셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.

양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.

예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.

33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...

n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다.

생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97

10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#### 입력
입력은 없다

#### 출력
10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.


#### 예제 입력 1
~~~
~~~

#### 예제 출력 1
~~~
1
3
5
7
9
20
31
42
53
64
 |
 |       <-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > North America > Mid-Central Regional > [1998 Mid-Central Regional Programming Contest](https://www.acmicpc.net/category/detail/154) D번

문제를 번역한 사람: baekjoon
링크
ACM-ICPC Live Archive
PKU Judge Online
ZJU Online Judge
TJU Online Judge
HDU Online Judge

#### 알고리즘 분류

#### 보기

#### 메모
- 자리수 분리하기
- int형 변수 = float값 [!]
- 배열 사용법(선언, 초기화) [!]
- 최적화된 알고리즘 찾아내기 [!]


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  //int a, b, c, d, res, sum=0;
  int a, b, c, d, res;
  int p[10000] = {0,};

  for(int num=1; num<10000; num++){
    //find self number
    a = num / 1000;
    b = (num / 100) % 10;
    c = (num / 10) % 10;
    d = num % 10;
    res = a + b + c + d + num;

    if(res < 10000){
      p[res] = 1;
    }

    //make sum
    if(p[num] == 0){
      printf("%u\n", num);
      //sum += num;
    }
  }
  //printf("\nThe sum is %d\n", sum);

  return 0;
}
```


### 1065 한수
각 자리수가 등차수열을 이루는지 판별하는 함수를 구현해 문제를 해결해봅니다

#### 문제
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

#### 출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.


#### 예제 입력 1
~~~
110
~~~

#### 예제 출력 1
~~~
99
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모
- 등차수열이란?


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  int N, a, b, c, cnt=99;
  scanf("%d", &N);

  if (N<100) {
    printf("%d", N);
    return 0;
  } else if (N==100) {
    printf("%d", 99);
    return 0;
  }

  for(int i=100; i<N+1; i++){
    a = i / 100;
    b = (i / 10) % 10;
    c = i % 10;

    if(a - b == b - c){
      cnt++;
    }
  }
  printf("%d", cnt);

  return 0;
}
```


### 2448 별찍기 - 11 [#]
그리고자 하는 삼각형의 크기와 위치에 대한 함수를 정의해 재귀적으로 문제를 해결해봅니다

별찍기 - 11
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 128 MB  8526  2758  1988  32.070%

#### 문제
예제를 보고 별찍는 규칙을 유추한 뒤에 별을 찍어 보세요.

#### 입력
첫째 줄에 N이 주어진다. N은 항상 3*2^k 수이다. (3, 6, 12, 24, 48, ...) (k<=10)

#### 출력
첫째 줄부터 N번째 줄까지 별을 출력한다.


#### 예제 입력 1
~~~
24
~~~

#### 예제 출력 1
~~~
                       *
                      * *
                     *****
                    *     *
                   * *   * *
                  ***** *****
                 *           *
                * *         * *
               *****       *****
              *     *     *     *
             * *   * *   * *   * *
            ***** ***** ***** *****
           *                       *
          * *                     * *
         *****                   *****
        *     *                 *     *
       * *   * *               * *   * *
      ***** *****             ***** *****
     *           *           *           *
    * *         * *         * *         * *
   *****       *****       *****       *****
  *     *     *     *     *     *     *     *
 * *   * *   * *   * *   * *   * *   * *   * *
***** ***** ***** ***** ***** ***** ***** *****
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모
- 재구함수(recursive function) 구현 [!]
- 프랙탈(fractal) [!]


#### 풀이
```c++
// [[c++]]

#include<iostream>
using namespace std;

void triangle(int n, int x, int y);
char arr[3072][6144];

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, i, j;

  cin >> n;  //N입력

  //배열 초기화
  //각 높이의 행의 요소들을 공백으로, 행의 끝부분만 null로 초기화한다.
  for (i = 0; i<n; i++) {
    for (j = 0; j<2 * n; j++){
      if (j == 2 * n - 1)
        arr[i][j] = '\0';
      else
        arr[i][j] = ' ';
    }
  }

  triangle(n, n - 1, 0);//삼각형의 높이와, 삼각형 맨 위 꼭지점 좌표를 매개변수로 넘긴다.

  //삼각형 출력
  for (i = 0; i < n; i++) {
    for (j = 0; j < 2 * n - 1; j++) {
      cout << arr[i][j];
    }
    cout << "\n";
  }

  return 0;
}

void triangle(int n, int x, int y) {
  if (n == 3) { //높이가 3이라면 삼각형을 만들어 출력한다.
    //삼각형을 그린다.
    arr[y][x] = '*';
    arr[y + 1][x - 1] = '*';
    arr[y + 1][x + 1] = '*';
    arr[y + 2][x - 2] = '*';
    arr[y + 2][x - 1] = '*';
    arr[y + 2][x] = '*';
    arr[y + 2][x + 1] = '*';
    arr[y + 2][x + 2] = '*';
    return;
  }
  triangle(n / 2, x, y); // 위의 삼각형 높이와 맨 위 꼭대기 좌표를 보낸다.
  triangle(n / 2, x - (n / 2), y + (n / 2)); // 왼쪽 하단 삼각형 높이와 맨 위 꼭대기 좌표를 보낸다.
  triangle(n / 2, x + (n / 2), y + (n / 2)); // 오른쪽 하단 삼각형 높이와 맨 위 꼭대기 좌표를 보낸다.
}
```



## 1차원 배열 사용하기 [!]

###   1152  단어의 개수
일차원 문자열 배열에서 단어의 개수를 구해봅니다

#### 문제
영어 대소문자와 띄어쓰기만으로 이루어진 문장이 주어진다. 이 문장에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.

#### 입력
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문장이 주어진다. 이 문장의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.

#### 출력
첫째 줄에 단어의 개수를 출력한다.


#### 예제 입력 1
~~~
The Curious Case of Benjamin Button
~~~

#### 예제 출력 1
~~~
6
~~~

#### 힌트

#### 출처
문제를 만든 사람: author5
빠진 조건을 찾은 사람: his130

#### 알고리즘 분류

#### 보기

#### 메모
- 문자열 vs 배열 [!]
- 문자열 저장시 배열의 크기 할당 [!]


#### 풀이
```c++
// [[c++]]

//scanf("%[^\n]", str)
#include <iostream>

int main() {
  int cnt = 1;
  int N = 1000002;
  char s[N];
  scanf("%[^\n]", s);

  for(int i=0;i<N;i++) {
    if (s[i] == ' ' && i != N-1) {
      cnt++;
    } else if (s[i] == '\0' || i == N-1) {
      if (s[0] == ' ') {
        cnt--;
      }
      if (s[i-1] == ' ') {
        cnt--;
      }

      printf("%d", cnt);
      return 0;
    }
  }
}

//cin.getline
# include <iostream>

using namespace std;

int main() {
  for (int i = 0; i < 3; i++) {
    char string[1000];
    cin.getline(string,1000,'\n');
    cout << string << endl;
  }
}


```


### 2577  숫자의 개수 [#]
세 수를 곱한 수의 각 자리수에 해당하는 숫자의 개수를 저장하기 위한 1차원 배열을 선언하여 문제를 해결해봅니다

#### 문제
세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면

A × B × C = 150 × 266 × 427 = 17037300 이 되고,

계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

#### 입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 같거나 크고, 1,000보다 작은 자연수이다.

#### 출력
첫째 줄에는 A×B×C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A×B×C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.


#### 예제 입력 1
~~~
150
266
427
~~~

#### 예제 출력 1
~~~
3
1
0
2
0
0
0
2
0
0
~~~

#### 힌트

#### 출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > [초등부](https://www.acmicpc.net/category/detail/367) 2번

문제의 오타를 찾은 사람: pineapple
잘못된 데이터를 찾은 사람: tncks0121

#### 알고리즘 분류

#### 보기

#### 메모
- 이게 초등부 문제다.
- 배열, 자리수 분리 [!]


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int a, b, c, n, p, q;
  int d[10] = {0,};

  scanf("%d\n%d\n%d", &a, &b, &c);
  n = a*b*c;

  if (n < 10000000) {
    p = 7;
  } else if (n < 100000000) {
    p = 8;
  } else {
    p = 9;
  }

  for (int i = 0; i < p; i++) {
    q = pow(10, i);
    d[n/q%10]++;
  }

  for (int i = 0; i < 10; i++) {
    printf("%d\n", d[i]);
  }

  return 0;
}
```


### 8958  OX퀴즈
OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산합니다

#### 문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

#### 출력
각 테스트 케이스마다 점수를 출력한다.


#### 예제 입력 1
~~~
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
~~~

#### 예제 출력 1
~~~
10
9
7
55
30
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > [Asia Regional - Seoul 2005](https://www.acmicpc.net/category/detail/1067) A번
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jh82582

#### 링크
[ACM-ICPC Live Archive](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1355)
[TJU Online Judge](http://acm.tju.edu.cn/toj/showp2501.html)

#### 메모
- 배열, 등차수열 구현


#### 풀이
```c++
// [[c++]]

#include <iostream>
using namespace std;

int main() {
  // n: 입력 줄수, ts: 전체 점수, ps: 부분 점수, M: 배열 최대 크기
  int n, ts = 0, ps = 0, M = 81;
  char* ox = new char[M];

  fill_n(ox, M, 'E');  //배열 초기화
  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    scanf("%s", ox);

    for(int j = 0; j < M; j++) {

      if (ox[j] == 'O') {
        ps++;
        ts += ps;
      } else if (ox[j] == 'X'){
        ps = 0;
      //} else if (ox[j] == 'E' || ox[j] == '\0') {
      } else {
        break;
      }
    }

    printf("%d\n", ts);

    // 변수, 배열 초기화
    ts = 0;
    ps = 0;
    fill_n(ox, M, 'E');
  }

  return 0;
}
```


### 2920  음계 [#]
주어진 배열이 오름차순인지 아닌지 판단하는 문제

#### 문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

#### 출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.


#### 예제 입력 1
~~~
1 2 3 4 5 6 7 8
~~~

#### 예제 출력 1
~~~
ascending
~~~

#### 예제 입력 2
~~~
8 7 6 5 4 3 2 1
~~~

#### 예제 출력 2
~~~
descending
~~~

#### 예제 입력 3
~~~
8 1 7 2 6 3 5 4
~~~

#### 예제 출력 3
~~~
mixed
~~~

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2009/2010 > Contest #1 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013
문제의 오타를 찾은 사람: thinksong1

#### 알고리즘 분류

#### 보기

#### 메모
- 조건문, 반복문 최소화 하기


#### 풀이
```c++
// [[c++]]

#include <iostream>
using namespace std;

int main() {
  int M = 8;
  int* a = new int[M];
  string scale = "mixed";

  for(int i = 0; i < M; i++) {
    scanf("%d", &a[i]);
  }

  if (a[0]==1) {
    scale = "ascending";
  } else if (a[0]==8) {
    scale = "descending";
  } else {
    printf("%s", "mixed");
    return 0;
  }

  for(int i = 0; i < M; i++) {
    if (scale == "ascending" && a[i] == i+1) {
      scale = "ascending";
    } else if (scale == "descending" && a[i] == M - i) {
      scale = "descending";
    } else {
      printf("%s", "mixed");
      return 0;
    }
  }

  printf("%s", scale.c_str());
  return 0;
}

// cin, cout, continue, break, define, enum
#include <iostream>
#include <cstdio>
#define LEN 8
enum {ASC=0, DESC, MIXED};
using namespace std;

int main(void){
  int result=0;
  int arr[LEN];

  for(int i=0; i<LEN; i++){
    scanf("%d", &arr[i]);
  }

  //초기 값 정해주기
  if(arr[1]-arr[0] == 1) result = ASC;
  else if(arr[1]-arr[0] == -1) result = DESC;
  else result = MIXED;

  //이전 값과 같은지 아닌지
  for(int i=1; i<LEN-1; i++){
    if(arr[i+1]-arr[i] == 1 && result == ASC) continue;
    if(arr[i+1]-arr[i] == -1 && result == DESC) continue;

    result = MIXED;
    break;
  }


  if(result == ASC) cout << "ascending";
  else if(result == DESC) cout << "descending";
  else cout << "mixed";

  return 0;
}
```


### 10039 평균 점수
조건에 따라 주어진 배열의 평균을 구하는 문제

#### 문제
상현이가 가르치는 아이폰 앱 개발 수업의 수강생은 원섭, 세희, 상근, 숭, 강수이다.

어제 이 수업의 기말고사가 있었고, 상현이는 지금 학생들의 기말고사 시험지를 채점하고 있다. 기말고사 점수가 40점 이상인 학생들은 그 점수 그대로 자신의 성적이 된다. 하지만, 40점 미만인 학생들은 보충학습을 듣는 조건을 수락하면 40점을 받게 된다. 보충학습은 거부할 수 없기 때문에, 40점 미만인 학생들은 항상 40점을 받게 된다.

학생 5명의 점수가 주어졌을 때, 평균 점수를 구하는 프로그램을 작성하시오.

#### 입력
입력은 총 5줄로 이루어져 있고, 원섭이의 점수, 세희의 점수, 상근이의 점수, 숭이의 점수, 강수의 점수가 순서대로 주어진다.

점수는 모두 0점 이상, 100점 이하인 5의 배수이다. 따라서, 평균 점수는 항상 정수이다.

#### 출력
첫째 줄에 학생 5명의 평균 점수를 출력한다.


#### 예제 입력 1
~~~
10
65
100
30
95
~~~

#### 예제 출력 1
~~~
68
~~~

#### 힌트
숭과 원섭이는 40점 미만이고, 보충학습에 참여할 예정이기 때문에 40점을 받게 된다. 따라서, 점수의 합은 340점이고, 평균은 68점이 된다.

#### 출처
Olympiad > 일본정보올림피아드 예선 > JOI 2014 예선 1번

문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모
- 평균, 조건에 따른 변수값 변경


#### 풀이
```c++
// [[c++]]

#include <iostream>
#define N 5

int main() {
  int score[N];
  int sum = 0;

  for(int i = 0; i < N; i++) {
    scanf("%d", score[i]);
  }

  for(int i = 0; i < N; i++) {
    if (score[i] > 40) {
      sum += score[i];
    } else {
      sum += 40;
    }
  }

  print("%u", int(sum/N));
}
```



## 문자열 사용하기
문자열을 다루는 문제들을 해결해 봅니다


### 11654 아스키 코드 [#]
알파벳의 아스키 코드 값을 출력해봅니다

#### 문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

#### 입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

#### 출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.


#### 예제 입력 1
~~~
A
~~~

#### 예제 출력 1
~~~
65
~~~

#### 예제 입력 2
~~~
C
~~~

#### 예제 출력 2
~~~
67
~~~

#### 예제 입력 3
~~~
0
~~~

#### 예제 출력 3
~~~
48
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: eric00513

#### 알고리즘 분류

#### 보기

#### 메모
- 아스키 코드란? [!]
- char / int type [!]


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  char c;

  scanf("%c", &c);
  printf("%d", (int)c);
}
```

@@@
### 10809 알파벳 찾기
한 단어에서 각 알파벳이 처음 등장하는 위치를 찾아봅니다

#### 문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

#### 출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.


#### 예제 입력 1
~~~
baekjoon
~~~

#### 예제 출력 1
~~~
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <string>
#define N 100
#define M 26

using namespace std;

int main() {
  char s[N];
  char a = 'a';
  int m[M];

  fill_n(m, M, -1);  //배열 초기화

  scanf("%s", s);

  for(int i = 0; i < N; i++) {
    int p = (int)s[i] - (int)a;

    if (s[i] != '\0') {
      if (m[p] == -1)
        m[p] = i;
      continue;
    } else {
      break;
    }
  }

  for(int i = 0; i < M; i++) {
    printf("%d ", m[i]);
  }
}
```


### 2675  문자열 반복
문자열의 각 문자를 반복하여 출력해봅니다

#### 문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 T를 만든 후 출력하는 프로그램을 작성하시오.

다시 설명하자면, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 T를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$%*+-./: 이다.

#### 입력
첫째 줄에 테스트 케이스의 개수 T(1 <= T <= 1,000)가 주어진다. 각 테스트 케이스는  반복 횟수 R(1 <= R <= 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

#### 출력
각 테스트 케이스에 대해 T를 출력한다.


#### 예제 입력 1
~~~
2
3 ABC
5 /HTP
~~~

#### 예제 출력 1
~~~
AAABBBCCC
/////HHHHHTTTTTPPPPP
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > North America > Greater New York Region > 2011 Greater New York Programming Contest A번

문제를 번역한 사람: baekjoon
잘못된 데이터를 찾은 사람: pichulia
링크
ACM-ICPC Live Archive
HDU Online Judge

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <string>
#define MAXT 1000
#define MAXR 10
#define MAXL 22

using namespace std;

int main() {
  int T, R = 0;
  char s[MAXL];

  scanf("%d", &T);

  for(int i = 0; i < T; i++) {
    scanf("%d %s", &R, s);

    for(int i = 0; i < MAXL; i++) {
      if (s[i] != '\0') {
        for(int j = 0; j < R; j++) {
          printf("%c",s[i]);
        }
        continue;
      } else {
        printf("\n");
        break;
      }
    }
  }

  return 0;
}


//compile error!!! putchar, puts
#include <iostream>
#include <string>

int main(){
  int t, i, j, k, n, length;
  char str[22] = " ";
  scanf("%d", &t);

  for(i = 0; i < t; i++){
    scanf("%d%s", &n, str);

    length = strlen(str);

    for(j = 0; j < length; j++){
      for(k = 0; k < n; k++){
        putchar(str[j]);
      }
    }

    puts("");
  }
}
```


### 1157  단어 공부
주어진 단어 중 가장 많이 사용된 알파벳을 출력하는 문제

#### 문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#### 입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

#### 출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


#### 예제 입력 1
~~~
Mississipi
~~~

#### 예제 출력 1
~~~
?
~~~

#### 예제 입력 2
~~~
zZa
~~~

#### 예제 출력 2
~~~
Z
~~~

#### 예제 입력 3
~~~
z
~~~

#### 예제 출력 3
~~~
Z
~~~

#### 예제 입력 4
~~~
baaa
~~~

#### 예제 출력 4
~~~
A
~~~

#### 힌트

#### 출처
문제를 만든 사람: author5
데이터를 추가한 사람: jh05013

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <string>
#define MAX 1000002  // 입력 문자열 최대 길이 + 2
#define ALP 27  // 알파벳 갯수(A~Z) + 1
#define A 'A'  // 알파벳 첫 글자(ascii값이 가장 작은 알파벳)
#define GAP 32  // 'A' - 'a' ascii 값 차이

using namespace std;

int main() {
  char s[MAX];  // 입력문자 배열(string)
  int m[ALP] = {0, };  // matched 문자 갯수 저장 배열 m[0] => 'A', 'a'
  int x[3] = {0, };  // 최빈도 횟수,문자 배열 m[0] => 최빈도수, m[1] => 최빈도 문자(int), m[2] => 동일 최빈도 수
  int p = 0;

  scanf("%s", s);

  for (int i = 0; i < MAX; i++) {
    if (s[i] != 0) {

      if (s[i] > (int)A + 26) {  //소문자 -> 대문자
        s[i] = (int)s[i] - GAP;
      }

      p = (int)s[i] - (int)A;

      //해당문자 빈도수 +1
      m[p] += 1;

      //최빈도 표시
      if (m[p] > x[0]) {
        x[0] = m[p];
        x[1] = (int)s[i];
        x[2] = 1;
        //printf("s[i]: %d p: %d x[0]: %d x[1]: %d x[2]: %d\n", s[i], p, x[0], x[1], x[2]);
        continue;
      } else if (m[p] == x[0]) {
        x[2]++;
        continue;
      }

    } else {
      break;
    }
  }

  //최빈도 문자 표시
  if (x[2] == 1) {
    printf("%c", (char)x[1]);
  } else if(x[2] > 1) {
    printf("%c", '?');
  } else {
    printf("?");
  }

}
```


### 1316  그룹 단어 체커
규칙에 맞는 알파벳의 개수를 출력하는 문제1

#### 문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

#### 출력
첫째 줄에 그룹 단어의 개수를 출력한다.


#### 예제 입력 1
~~~
3
happy
new
year
~~~

#### 예제 출력 1
~~~
3
~~~

#### 예제 입력 2
~~~
4
aba
abab
abcabc
a
~~~

#### 예제 출력 2
~~~
1
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013
문제의 오타를 찾은 사람: joonas

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#define MAX 102
#define Aa 97  // 'a'의 ascii code number

using namespace std;

bool checkGroupWord(string s);

int main() {
  int n, cnt = 0;
  char s[MAX];

  scanf("%d\n", &n);

  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    if (checkGroupWord(s)) {
      cnt++;
    }
  }

  printf("%d", cnt);

  return 0;
}

bool checkGroupWord(string s) {
  int p = 0;
  int m[26] = {0,};
  char c = 96;
  bool g = true;  //  group word?

  for(int i = 0; i < MAX; i++) {

    if (s[i] == '\0') {
      break;
    }

    if (c != s[i]) {
      p = s[i] - Aa;

      if (m[p] == 0) {
        m[p] = 1;
        c = s[i];
      } else {
        g = false;
        break;
      }
    } else {
      continue;
    }
  }

  return g;
}
```


### 1152  단어의 개수
단어의 개수를 구하는 문제


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 2908  상수
숫자를 뒤집어서 비교하는 문제

#### 문제
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 숫자 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른사람과 다르게 거꾸로 읽는다. 예를 들어, 734과 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

#### 출력
첫째 줄에 상수의 대답을 출력한다.


#### 예제 입력 1
~~~
734 893
~~~

#### 예제 출력 1
~~~
437
~~~

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2009/2010 > Contest #3 1번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jongfighter

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
int rev(int n);

int main() {
  int a, b, x, y;

  scanf("%d %d", &a, &b);
  x = rev(a);
  y = rev(b);

  x > y ? printf("%d", x) : printf("%d", y);

  return 0;
}

int rev(int n) {
  return n%10*100 + (int)(n/10)%10*10 + (int)(n/100)%10;
}
```


### 5622  다이얼
규칙에 따라 문자에 대응하는 수를 출력하는 문제

#### 문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

![dial](images/dial.png)


전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 다른 숫자를 누르려면 다이얼이 원래 위치로 돌아가기를 기다려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 시간을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.

#### 출력
첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.


#### 예제 입력 1
~~~
UNUCIC
~~~

#### 예제 출력 1
~~~
36
~~~

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2012/2013 > [Contest #6](https://www.acmicpc.net/category/detail/560) 1번

문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#define MAX 16
#define A 'A'

int main() {
  int t = 0;
  int dial[26] = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9};
  char s[MAX];

  scanf("%s", s);

  for (int i = 0; i < MAX; i++) {
    if (s[i] != '\0') {
      t += dial[(int)s[i] - (int)A] + 1;
    } else {
      break;
    }
  }

  printf("%d", t);

}
```


### 2941  크로아티아 알파벳
규칙에 맞는 알파벳의 개수를 출력하는 문제2

#### 문제
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 다음과 같이 변경해서 입력했다.

크로아티아 알파벳 | 변경
-----
č | c=
ć | c-
dž | dz=
ñ | d-
lj | lj
nj | nj
š | s=
ž | z=

예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

#### 입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

문제 설명에 나와있는 크로아티아 알파벳만 주어진다.

#### 출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.


#### 예제 입력 1
~~~
ljes=njak
~~~

#### 예제 출력 1
~~~
6
~~~

#### 예제 입력 3
~~~
ddz=z=
~~~

#### 예제 출력 3
~~~
3
~~~

#### 예제 입력 4
~~~
nljj
~~~

#### 예제 출력 4
~~~
3
~~~

#### 예제 입력 5
~~~
c=c=
~~~

#### 예제 출력 5
~~~
2
~~~

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2008/2009 > Contest #5 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: handong jh05013 jms100300 veydpz zzangho

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <string>
#define MAX 100

using namespace std;
void replace_all(string& source, string const& find, string const& replace);

int main() {
  const string ca[8] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
  string s = "";
  cin >> s;

  for (int i = 0; i < 8; i++) {
    replace_all(s, ca[i], "@");
  }

  //printf("%s\n%lu\n", s.c_str(), s.length());
  printf("%lu", s.length());

}

void replace_all(string& source, string const& find, string const& replace) {
  for(string::size_type i = 0; (i = source.find(find, i)) != string::npos;) {
    source.replace(i, find.length(), replace);
    i += replace.length();
  }
}
```



## 규칙 찾기
규칙을 찾아 문제를 해결해 봅니다


### 2438  별찍기 - 1
출력 예시의 별 모양을 보고 규칙을 유추해 봅니다


### 2292  벌집
벌집이 형성되는 규칙을 유추해 문제를 해결해 봅니다

#### 문제

![honeycomb](images/honeycomb.png)
위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

#### 입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

#### 출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.


#### 예제 입력 1
~~~
13
~~~

#### 예제 출력 1
~~~
3
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - [Daejeon Nationalwide Internet Competition 2004](https://www.acmicpc.net/category/detail/1089) B번

문제의 오타를 찾은 사람: waylight3

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int m, n, a = 0;

  scanf("%d", &n);

  m = (int)sqrt(n/3) + 1;
  a = 3*m*m - 3*m + 1;
  //printf("m: %d n: %d a: %d\n", m, n, a);

  while(a < n) {
    //printf("m: %d n: %d a: %d\n", m, n, a);
    m++;
    a = 3*m*m - 3*m + 1;
  }

  printf("%d\n", m);
}
//
#include <iostream>
using namespace std;

int main(void){
  //입력
  long long n;
  cin >> n;

  //계산
  int cnt = 1;    //몇겹인지 = 최소 칸수
  long long range =1; //숫자의 범위 ex) 2~7, 8~19를 나타내기 위함
  long long tmp =1;   //6의 배수를 더하기 위해서 사용

  while(1){
    if(range >= n){ //숫자의 범위가 커지면 break;
      break;
    }
    tmp = 6 * (cnt++);
    range += tmp;
  }

  //출력
  cout << cnt;

  return 0;
}
```


### 1193  분수찾기
각 번호의 분수들이 어떤 규칙을 있는지 유추해 문제를 해결해 봅니다

#### 문제
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1 | 1/2 | 1/3 | 1/4 | 1/5 | …
2/1 | 2/2 | 2/3 | 2/4 | … | …
3/1 | 3/2 | 3/3 | … | … | …
4/1 | 4/2 | … | … | … | …
5/1 | … | … | … | … | …
… | … | … | … | … | …

이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 X(1≤X≤10,000,000)가 주어진다.

#### 출력
첫째 줄에 분수를 출력한다.


#### 예제 입력 1
~~~
14
~~~

#### 예제 출력 1
~~~
2/4
~~~

#### 힌트

#### 출처
문제를 만든 사람: author6
문제의 오타를 찾은 사람: deadlylaid

#### 메모


#### 풀이
```c++
// [[c++]]

#include <iostream>

int main() {
  int m = 0, n = 1, a = 0;  // n: 입력값, m: m번째 그룹(분자+분모+1), a: m번째 그룹까지 갯수

  scanf("%d", &n);

  while (a < n) {
    a += 1 + m++;
    //printf("m: %d a: %d n: %d\n", m, a, n);
  }

  if(m%2 == 0) {
    printf("%d/%d\n", m-a+n, a-n+1);
  } else {
    printf("%d/%d\n", a-n+1, m-a+n);
  }

  return 0;
}
```


### 1011  Fly me to the Alpha Centauri
거리에 따른 장치 사용 횟수를 출력하는 문제

#### 문제
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

![centauri](images/centauri.jpg)

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최소값을 구하는 프로그램을 작성하라.

#### 입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. ( 0 ≤ x < y < 231)

#### 출력
각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 회수를 출력한다.


#### 예제 입력 1
~~~
3
0 3
1 5
45 50
~~~

#### 예제 출력 1
~~~
3
3
4
~~~

#### 힌트

#### 출처
문제를 번역한 사람: AIAI

#### 메모


#### 풀이
```c++
// [[c++]]

// '시간 초과.' Why?
#include <cstdio>

int main() {
  int n, x;  // n: 입력값, x: 출력값(횟수)
  unsigned int a, b; // a: 출발점, b: 도착점
  int k;  // k: 매개변수 2k ~ x

  scanf("%d", &n);

  for(int i = 0; i < n; i++) {
    int d = 0;
    scanf("%u %u", &a, &b);
    d = b - a;  // d: distance(거리)

/*
  //sqrt 이용

  k = (int)sqrt(d);

  if (k*k == d) {  // k*k == d : /\ type
    x = 2*k - 1;
  } else if (k*k + k >= d) { // k*k + k == d : /-\ type
    x = 2*k;
  } else {
    x = 2*k + 1;
  }

*/

  //non-sqrt 이용
  for(int k = 0; k*k < d; k++) {
    //printf("k: %d d: %d k*k: %d\n", k, d, k*k);
    if (k*k + 2*k + 1 < d) {
      continue;
    } else {
      if (k*k == d) {  // k*k == d : /\ type
        x = 2*k - 1;
      } else if (k*k + k >= d) { // k*k + k == d : /-\ type
        x = 2*k;
      } else {
        x = 2*k + 1;
      }
      break;
    }
  }

    printf("%d\n", x);
  }
}


// long long, for
#include<cstdio>
#include<cmath>
typedef long long ll;

int main() {
  int tc;
  for (scanf("%d", &tc); tc > 0; tc--) {
    ll x1, x2;
    scanf("%lld%lld", &x1, &x2);
    ll dist = x2 - x1;
    for (ll i = 1; i < 50000; i++) {
      ll n2 = i*i;
      ll rem = ceil((dist - n2) / (float)i);
      ll mn = 2 * i - 1;

      if (n2 <= dist && dist < (i+1)*(i+1) ) {
        printf("%lld\n", mn + rem);
        break;
      }
    }
  }
  return 0;
}
```


### 10250 ACM 호텔
호텔 방 번호의 규칙을 찾아 출력하는 문제

#### 문제
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 여러분은 지우를 도와 줄 프로그램을 작성하고자 한다. 즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자. 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99). 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고). 이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다. 또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.

![acmhotel](images/acmhotel.png)

![acmhotel2](images/acmhotel2.png)

그림 1. H = 6 이고 W = 12 인 H × W 호텔을 간략하게 나타낸 그림

방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다. 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.

손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다. 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.

여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

#### 입력
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).

#### 출력
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.


#### 예제 입력 1
~~~
2
6 12 10
30 50 72
~~~

#### 예제 출력 1
~~~
402
1203
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2014 A번

데이터를 만든 사람: baekjoon
어색한 표현을 찾은 사람: hidonggi
문제의 오타를 찾은 사람: joonas startup

#### 메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {
  int t, h, w, n;  // t: 입력 횟수, h: 전체 층수, w: 층당 방수, n: 순번
  int x, y;  // x: 배정 호수, y: 배정 층수

  scanf("%d", &t);

  for(int i = 0; i < t; i++) {
    scanf("%d %d %d", &h, &w, &n);
    //checkInput(h, w, n);
    x = (n-1)/h + 1;
    y = (n-1)%h + 1;

    if (x < 10) {
      printf("%d0%d\n", y, x);
    } else {
      printf("%d%d\n", y, x);
    }
  }
}

int checkInput(int& h, int& w, int& n) {
  if(h < 1 || w> 99 || n > h*w) {
    print("input error!!");
    return 333;
  }
  return 0;
}
```


### 1924  2007년
2007년도 어느 날의 요일의 규칙을 찾아 출력하는 문제


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 2775  부녀회장이 될테야 [#]
층과 거주자 수의 규칙을 찾는 문제

#### 문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a 층의 b 호에 살려면 자신의 아래(a-1)층에 1호부터 b 호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정 했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있나를 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층에 i호에는 i명이 산다.

#### 입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

#### 출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.


#### 예제 입력 1
~~~
2
1
3
2
3
~~~

#### 예제 출력 1
~~~
6
10
~~~

#### 힌트

#### 출처
문제의 오타를 찾은 사람: sunhmj44
어색한 표현을 찾은 사람: veydpz

#### 메모


#### 풀이
```c++
// [[c++]]

// 재귀함수
#include <cstdio>

int getIt(int n, int k);

int main() {
  int t, n, k;  // 입력값 t: 테스트 횟수, n: 층수, k: 호수

  scanf("%d", &t);

  for(int i = 0; i < t; i++) {
    scanf("%d\n%d", &n, &k);
    printf("%d", getIt(n, k));
  }
}

int getIt(int n, int k) {
  int x = 0;

  if (n == 0) {
    return k;
  }

  for(int i = 1; i < k+1; i++) {
    x += getIt(n-1, i);
  }

  return x;
}
```


### 1475  방 번호
주어진 단어를 만들기 위한 규칙을 찾는 문제

#### 문제
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

#### 입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

#### 출력
첫째 줄에 필요한 세트의 개수를 출력한다.


#### 예제 입력 1
~~~
9999
~~~

#### 예제 출력 1
~~~
2
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: doju
빠진 조건을 찾은 사람: newdeal
문제의 오타를 찾은 사람: waylight3

#### 알고리즘 분류

#### 보기

#### 메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>
#define MAX 8  // 입력 최대 길이 + 1
#define ZERO 48  // '0'의 ascii code 값

int main() {
  int x = 0;  // 필요한 플라스틱 숫자 세트 개수
  int a[11] = {0,};  // 숫자(방번호) 갯수 배열
  char s[MAX];  // 입력 숫자(문자열)

  scanf("%s", s);

  for (int i = 0; i < MAX; i++) {
    if (s[i] == '\0') {
      break;
    } else {
      a[(int)s[i] - ZERO]++;
    }
  }

  x = (int)(a[6] + a[9] + 1)/2;  // 6, 9에 필요한 세트 개수

  for (int i = 0; i < 10; i++) {
    if (i == 6 || i == 9) continue;  // 6, 9 제외
    if (a[i] > x) x = a[i];
  }

  printf("%d", x);

}
```


### 6064  카잉 달력 [#]
주어진 네 숫자를 규칙을 찾아 바꾸는 문제

#### 문제
최근에 ICPC 탐사대는 남아메리카의 잉카 제국이 놀라운 문명을 지닌 카잉 제국을 토대로 하여 세워졌다는 사실을 발견했다. 카잉 제국의 백성들은 특이한 달력을 사용한 것으로 알려져 있다. 그들은 M 과 N 보다 작거나 같은 두 개의 자연수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다. 그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다. <x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다. <M:N>은 그들 달력의 마지막 해로서, 이 해에 세상의 종말이 도래한다는 예언이 전해 온다.

예를 들어, M = 10 이고 N = 12라고 하자. 첫 번째 해는 <1:1>로 표현되고, 11 번째 해는 <1:11>로 표현된다. <3:1>은 13 번째 해를 나타내고, <10:12>는 마지막인 60 번째 해를 나타낸다.

네 개의 정수 M, N, x 와 y가 주어질 때, <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는 지를 구하는 프로그램을 작성하라.

#### 입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터는 한 줄로 구성된다. 각 줄에는 네 개의 정수 M, N, x와 y가 주어진다. (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N) 여기서 <M:N>은 카잉 달력의 마지막 해를 나타낸다.

#### 출력
출력은 표준 출력을 사용한다. 각 테스트 데이터에 대해, 정수 k를 한 줄에 출력한다. 여기서 k는 <x:y>가 k번째 해를 나타내는 것을 의미한다. 만일 <x:y>에 의해 표현되는 해가 없다면, 즉, <x:y>가 유효하지 않은 표현이면, -1을 출력한다.


#### 예제 입력 1
~~~
3
10 12 3 9
10 12 7 2
13 11 5 6
~~~

#### 예제 출력 1
~~~
33
-1
83
~~~

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2013 B번

문제의 오타를 찾은 사람: 2e718 roeniss
데이터를 만든 사람: baekjoon

#### 메모


#### 풀이
```c++
// [[c++]]

//x, y go step by M, N
#include <cstdio>

int lcm(int m, int n) {
  int z, a, b;
  a = m; b = n;

  while(true) {
    z = a%b;
    if(z == 0) break;
    a = b; b = z;
  }

  return (m*n)/b;
}

int main() {
  int T;
  scanf("%d",&T);

  while(T--) {
    int M, N, x, y;
    scanf("%d %d %d %d",&M, &N, &x, &y);
    int max = lcm(M, N);

    while(x!=y && x <= max) {
      if(x < y) x += M;
      else y += N;
    }

    if(x != y) printf("-1\n");
    else printf("%d\n", x);
  }

  return 0;
}


//
#include <cstdio>
#include <algorithm>
#define INF 987654321

using namespace std;

int t, m, n, x, y, r, a;

int main() {
  scanf("%d", &t);

  while (t--) {
    scanf("%d%d%d%d", &m, &n, &x, &y);
    r = INF;
    for (int i = 0; i <= n; i++) {
      if (!((m*i + (x - y)) % n)) {
        r = m*i + x;
        break;
      }
    }
    for (int i = 0; i <= n; i++) {
      if (!((m*i + (m - n)) % n)) {
        a = m*i + m;
        break;
      }
    }
    if (r == INF || a < r)
      printf("-1\n");
    else
      printf("%d\n", r);
  }

  return 0;
}
```



## 정렬해보기
정렬을 해 봅니다

### 2750  수 정렬하기 [#]
삽입 정렬, 거품 정렬 등의 간단한 정렬 알고리즘을 구현해 봅니다

#### 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절대값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#### 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


#### 예제 입력 1
~~~
5
5
2
3
4
1
~~~

#### 예제 출력 1
~~~
1
2
3
4
5
~~~

#### 힌트

#### 출처
문제의 오타를 찾은 사람: lazy_ren

#### 비슷한 문제
2751번. 수 정렬하기 2
10989번. 수 정렬하기 3

#### 메모
> 정렬(sort), 교환(swap) [!]
> [거품정렬(bubble sort)](https://ko.wikipedia.org/wiki/거품_정렬) 구현 [!]
> [삽입정렬(insertion sort)](https://ko.wikipedia.org/wiki/삽입_정렬) 구현 [i]

@@@
#### 풀이
```c++
// [[c++]]

//bubble sort
#include <cstdio>

int main() {
  int n;
  scanf("%d", &n);

  int arr[n] = {0,};

  for(int i = 0; i < n; i++){
    scanf("%d", &arr[i]);
  }

  //bubble sort.
  int tmp;

  for(int i = 0 ; i < n; i++) {
    for(int j = 0 ; j < n-1-i ; j++) {

      //swap
      if(arr[j] > arr[j+1]) {
        tmp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = tmp;
      }

    }
  }

/*
  //insertion sort
  int key;

  for(int i = 1; i < n ;i++) {
    int j;
    key = arr[i];

    for(j = i-1; j >= 0; j--) {
      if(arr[j] > key) {
        arr[j+1] = arr[j];
      } else {
        break;
      }
    }
    arr[j+1] = key;
  }
*/

  for(int i = 0; i < n; i++){
    printf("%d\n", arr[i]);
  }

  //delete []arr;
  return 0;
}




// insertion sort
#include<iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;

  int * arr = new int[n];
  for(int i=0; i< n; i++){
    cin >> arr[i];
  }

  //insertion sort
  int key;

  for(int i=1; i<n ;i++){
    int j;
    key = arr[i];

    for(j= i-1 ; j>=0 ; j--){
      if(arr[j] > key){
        arr[j+1] = arr[j];
      }else{
        break;
      }
    }
    arr[j+1] = key;
  }

  //print
  for(int i=0; i<n; i++){
    cout << arr[i] << endl;
  }

  delete []arr;
  return 0;
}
```


### 2751  수 정렬하기 2
병합정렬(Merge Sort) 혹은 힙 정렬(Heap Sort)을 사용해 봅니다

#### 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절대값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#### 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


#### 예제 입력 1
~~~
5
5
4
3
2
1
~~~

#### 예제 출력 1
~~~
1
2
3
4
5
~~~

#### 힌트

#### 비슷한 문제
2750번. 수 정렬하기
10989번. 수 정렬하기 3

#### 메모
> [시간 복잡도](https://ko.wikipedia.org/wiki/시간_복잡도) Big-O [!]
> [병합정렬(Merge Sort)](https://ko.wikipedia.org/wiki/병합_정렬) [!]
> [힙 정렬(Heap Sort)](https://ko.wikipedia.org/wiki/힙_정렬) [!]
> [퀵 정렬(Quick Sort)](https://ko.wikipedia.org/wiki/퀵_정렬) [!]
> [백준 2751번 문제 HeapSort구현](http://survivalking.tistory.com/34)


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}

// Quick sort
#include <cstdio>
#define MAX 1000000  // 데이터 개수의 MAX 범위

#define qSWAP(x, y) { int t = x; x = y; y = t; }  // SWAP 함수
int N, arr[MAX]; // 데이터 개수와 저장할 배열

void qSort(int *array, int left, int right) {
  int mLeft = left, mRight = right;
  int pivot = array[(left + right) / 2];

  while(mLeft <= mRight) {
    while(pivot > array[mLeft]) mLeft++;
    while(pivot < array[mRight]) mRight--;

    if(mLeft <= mRight) {
      qSWAP(array[mLeft], array[mRight]);
      mLeft++, mRight--;
    }
  }

  if(left < mRight) qSort(arr, left, mRight);
  if(mLeft < right) qSort(arr, mLeft, right);
}

int main() {
  int i;

  // 입력
  scanf("%d", &N);
  for(i = 0; i < N; i++) {
    scanf("%d", &arr[i]);
  }

  qSort(arr, 0, N - 1);  // 배열 인덱스 0 ~ N-1 까지 퀵소트


  // 출력
  for(i = 0; idx < N; i++) {
    printf("%d ", arr[i]);
  }

  return 0;
}


//개선된 퀵정렬
#include<stdio.h>
#include<stdlib.h>

void swap(int &x, int &y)
{
  int z = x;
  x = y;
  y = z;
}

int choosePivot(int low, int high)
{
  return low + (high-low)/2;
}

int partition(int *a, int low, int high)
{
  int pivotIndex = choosePivot(low,high);
  int pivotValue = a[pivotIndex];
  swap(a[pivotIndex], a[high]);
  int storeIndex = low;

  for(int i=low; i<high;i++)
  {
    if(a[i]<pivotValue)
    {
      swap(a[storeIndex], a[i]);
      storeIndex++;
    }
  }
  swap(a[storeIndex],a[high]);
  return storeIndex;
}

void quicksort(int *a, int low, int high)
{
  if(low<high)
  {
    int pivot = partition(a,low,high);
    quicksort(a, low, pivot-1);
    quicksort(a, pivot+1 ,high);

  }
}

int main()
{
int n;
  scanf("%d",&n);

  int *a = (int *)malloc(sizeof(int)*n);

  for (int i=0; i<n; i++) {
    scanf("%d",&a[i]);
  }

  quicksort(a, 0, n-1);

  for (int i=0; i<n; i++) {
    printf("%d\n",a[i]);
  }

  free(a);

  return 0;
}
```


### 10989 수 정렬하기 3 [#]
카운팅 정렬(Counting Sort) 혹은 기수 정렬(Radix Sort)를 사용해 봅니다

수 정렬하기 3
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
5 초 8 MB  19828 4506  3273  24.182%

#### 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

#### 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


#### 예제 입력 1
~~~
10
5
2
3
1
4
2
3
5
1
7
~~~

#### 예제 출력 1
~~~
1
1
2
2
3
3
4
5
5
7
~~~

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: joonas

#### 비슷한 문제
2750번. 수 정렬하기
2751번. 수 정렬하기 2

#### 알고리즘 분류

#### 보기

#### 메모
> [카운팅 정렬(Counting Sort)](http://bowbowbow.tistory.com/8) [!]
> [기수 정렬(radix sort)](https://ko.wikipedia.org/wiki/기수_정렬) [!]


#### 풀이
```c++
// [[c++]]

// Counting sort
#include <cstdio>
#define CMAX 10001

int main() {

  int N;  // 입력값 개수
  int arr[CMAX] = {0,}; // counting 배열
  int p = 0;  // counting 배열 index(position)

  //입력
  scanf("%d", &N);
 
  for(int i = 0; i < N; i++) {
    scanf("%d", &p);
    arr[p] += 1;
  }

  //출력
  for(int i = 1; i < CMAX; i++) {
    if(arr[i] > 0) {
      for(int j = 0; j < arr[i]; j++) {
        printf("%d ", i);
      }
    }
  }

  return 0;
}
```


### 2108  통계학 [#]
네가지 통계값을 구하는 문제
통계학
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  6912  1386  1051  22.583%

#### 문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최대값과 최소값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절대값은 4,000을 넘지 않는다.

#### 출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.


#### 예제 입력 1
~~~
5
1
3
8
-2
2
~~~

#### 예제 출력 1
~~~
2
2
1
10
~~~

#### 힌트

#### 출처
문제의 오타를 찾은 사람: cpp05013 skynet
데이터를 추가한 사람: yungoon

#### 메모
> 산출평균, 중앙값, 최빈값, 범위 [!]
> vector [!]
> [백준 2108 통계학 (최빈값, 산술평균, 중앙값, 범위)](http://mizzo-dev.tistory.com/entry/baekjoon2108) [!]


#### 풀이
```c++
// [[c++]]

// vector 제출전 확인요
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stack>

using namespace std;

//sort 기준
bool comp(const pair<int, int> &p1, const pair<int, int> &p2){

  if(p1.second == p2.second){   //빈도수가 같으면
    return p1.first < p2.first; //숫자(key)작은 게 앞으로
  }
  return p1.second > p2.second;  //다르면 빈도수가 큰 게 앞으로

}

int main(void) {
  int n;
  vector<int> v;
  int  key;
  double sum=0;  //산술평균용

  //입력 1
  scanf("%d", n);
  for(int i=0; i<n ;i++){
    //cin >> key;
    scanf("%d", key);
    v.push_back(key);

    sum += key;
  }

  //오름차순으로 정렬.
  sort(v.begin(), v.end());

  //산술평균 출력
  //내림함수를 이용하여 반올림.
  //cout <<  (int)floor( (sum / n) + 0.5) << endl;
  printf("%d\n", (int)floor( (sum / n) + 0.5));

  //중앙값 출력
  //cout << v[n/2] << endl;
  printf("%d\n", v[n/2]);

  //최빈값
  vector<pair<int,int> > st;  //key 와 빈도수를 저장할 pair형 vector.
  vector<int>::size_type i;

  for(i=0; i<v.size(); i++){
    if(st.empty()){
      st.push_back(pair<int,int>(v[i],1));
      continue;
    }

    if(st.back().first == v[i]){  //같은게 있다면

      pair<int, int> tmp = st.back();
      tmp.second++;  //하나 증가
      st.pop_back();  //기존것 없애고
      st.push_back(tmp);  //새로운 것 다시 삽입

    }else{
      st.push_back(pair<int,int>(v[i],1));
    }
  }

  //빈도수가 높고, 숫자(key)가 낮은 순으로 정렬
  sort(st.begin(), st.end(), comp);

  if(st[0].second == st[1].second){
    //cout << st[1].first << endl;
    printf("%d\n", st[1].first);
  }else{
    //cout << st[0].first << endl;
    printf("%d\n", st[0].first);
  }

  //범위
  //cout << v.back() - v.front() << endl;
  printf("%d\n", v.back() - v.front());


  return 0;
}



// Counting sort
#include <cstdio>
#define CMAX 10001

int main() {

  int N;  // 입력값 개수
  int arr[CMAX] = {0,}; // counting 배열
  int p = 0;  // counting 배열 index(position)

  //입력
  scanf("%d", &N);

  //counting sort
  for(int i = 0; i < N; i++) {
    scanf("%d", &p);
    arr[p] += 1;
  }

  //출력
  for(int i = 1; i < CMAX; i++) {
    if(arr[i] > 0) {
      for(int j = 0; j < arr[i]; j++) {
        printf("%d ", i);
      }
    }
  }

  return 0;
}
```


#### 풀이 2
```swift
//[[swift]]

import Foundation

let n = Int(readLine()!)!
var array: [Int] = []
var sum = 0
var count: [Int:Int] = [:]
var mode = 0

for _ in 0..<n {
  let input = Int(readLine()!)!
  sum += input
  count[input] = ( count[input] != nil ? count[input]! : 0 ) + 1
  mode = mode < count[input]! ? count[input]! : mode
  array.append(input)
}

array = array.sorted()
let filtered = count.filter{ $0.value == mode }
let countSorted = filtered.sorted{ $0.key < $1.key }

print(Int(round(Double(sum) / Double(n))))
print(array[n / 2])
print(countSorted[countSorted.count > 1 ? 1 : 0].key)
print(array.last! - array.first!)
```


### 1427  소트인사이드
숫자들을 내림차순으로 정렬하는 문제

#### 문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

#### 입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

#### 출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.


#### 예제 입력 1
~~~
2143
~~~

#### 예제 출력 1
~~~
4321
~~~

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: bvba djm03178

#### 알고리즘 분류

#### 보기

#### 메모
> string vs char array
> sort() [!]
> [백준 1427 소트인사이드](http://blockdmask.tistory.com/152)


#### 풀이
```c++
// [[c++]]

// sort() include <algorithm>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

char arr[10];
int main() {

  cin>>arr;

  sort(arr, arr+strlen(arr), greater<int>());
  for(int i=0; i<strlen(arr); i++){
    cout <<arr[i];
  }

  return 0;
}



```


### 1181  단어 정렬 [#]
단어들을 정렬하는 문제

#### 문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

#### 입력
첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

#### 출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.


#### 예제 입력 1
~~~
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
~~~

#### 예제 출력 1
~~~
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
~~~

#### 힌트

#### 출처
문제를 만든 사람: author5

#### 알고리즘 분류

#### 보기

#### 메모
> [백준 1181번: 단어 정렬(vector, array, sort)](http://blockdmask.tistory.com/99)


#### 풀이
```c++
// [[c++]]

#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

//구조체: 단어 저장
struct Word{
  int len;
  char arr[51];
};

//sort 기준이 되는 비교 함수
bool comp(const Word &s1,const Word &s2){
  if(s1.len == s2.len){ //길이가 같으면, 사전순 앞으로
    for(int i=0; i< s1.len; i++){
      if(s1.arr[i] == s2.arr[i]) continue;
      else if(s1.arr[i] < s2.arr[i]) return true;
      else return false;
    }
  }
  return s1.len < s2.len;  //길이가 짧은 게 앞으로
}

int main(void){
  int n;
  scanf("%d", &n);

  Word *word = new Word[n]; //동적할당

  for(int i=0; i<n; i++){
    scanf("%s", word[i].arr);
    word[i].len = strlen(word[i].arr);

  }

  sort(word, word+n , comp);  //정렬(<algorithm>)

  for(int i=0; i<n; i++){ //배열을 이용한 비교
    if(i!=0){
      if(!strcmp(word[i].arr, word[i-1].arr)){ //중복제거
        continue;
      }
    }
    printf("%s\n", word[i].arr);
  }

  delete []word; //메모리 할당 해제
  return 0;
}

```



## 소수 구하기
소수를 구하는 여러 방법을 사용해 봅니다


### 1978  소수 찾기
소수 판별법을 연습해 봅니다

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

예제 입력 1 
4
1 3 5 7
예제 출력 1 
3
힌트
출처
데이터를 추가한 사람: bclim9108
문제의 오타를 찾은 사람: djm03178
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 2581  소수
소수 판별법을 연습해 봅니다

문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최소값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최소값을 출력한다. 

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

예제 입력 1 
60
100
예제 출력 1 
620
61
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 중등부 1번

데이터를 추가한 사람: hchanhong kyaryunha
문제의 오타를 찾은 사람: jh05013 sky1357
잘못된 데이터를 찾은 사람: myungwoo
메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 1929  소수 구하기
에라토스테네스의 체를 구현해 봅니다

문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1≤M≤N≤1,000,000)

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13
힌트
알고리즘 분류
보기

메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 4948  베르트랑 공준
n이 주어졌을때, n보다 크고 2n보다 작거나 같은 소수를 구하는 문제

문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)

입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

예제 입력 1 
1
10
13
100
1000
10000
100000
0
예제 출력 1 
1
4
3
21
135
1033
8392
힌트
출처
ACM-ICPC > Regionals > Asia > Japan > Domestic Contest > 2011 Domestic Contest A번

문제를 번역한 사람: baekjoon
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 9020  골드바흐의 추측
n이 주어졌을 때, 두 소수의 합으로 n을 표현하는 문제

문제
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 숫자를 골드바흐 숫자라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 숫자의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다. (4 ≤ n ≤ 10,000)

출력
각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

예제 입력 1 
3
8
10
16
예제 출력 1 
3 5
5 5
5 11
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2011 E번

문제를 번역한 사람: baekjoon
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



## 스택 사용하기 (기초)
스택을 구현해 봅니다

### 10828 스택
스택의 개념을 익히고 실습해 봅니다

문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
예제 출력 1 
2
2
0
2
1
-1
0
1
-1
0
3
힌트
출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: hshtop123
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 1874  스택 수열
스택이 가지는 성질에 대해 고민하고 관련 문제를 해결해 봅니다

문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 먼저 들어간 자료가 제일 나중에 나오는 (FILO, first in last out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
예제 입력 2 
5
1
2
5
3
4
예제 출력 2 
NO
힌트
1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

출처
문제를 만든 사람: author5
데이터를 추가한 사람: djm03178
알고리즘 분류
보기

메모
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 먼저 들어간 자료가 제일 나중에 나오는 (FILO, first in last out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
예제 입력 2 
5
1
2
5
3
4
예제 출력 2 
NO
힌트
1부터 n까지에 수에 대해 차례로 [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop] 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

출처
문제를 만든 사람: author5
데이터를 추가한 사람: djm03178
알고리즘 분류
보기

메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


### 9012  괄호
주어진 문자열이 올바른 괄호열인지 판단하는 문제

괄호
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 128 MB  20487 8018  6084  39.244%
문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력
출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

예제 입력 1 
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
예제 출력 1 
NO
NO
YES
NO
YES
NO
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2012 G번

데이터를 만든 사람: baekjoon
문제의 오타를 찾은 사람: marona
알고리즘 분류
보기

메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2504  괄호의 값
스택을 사용해, 주어진 문자열이 올바른 괄호열인지 판단하고, 그 괄호열의 값을 출력하는 문제

문제
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 

‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자.  ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로  ‘(()[[ ]])’의 괄호값은 2×11=22 이다. 그리고  ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다. 

입력
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

출력
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다. 

예제 입력 1 
(()[[]])([])
예제 출력 1 
28
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2008 > 초등부 4번

Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2008 > 중등부 2번

데이터를 추가한 사람: ftilrftilr12 sang7
알고리즘 분류
보기

메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



## 큐 사용하기
큐를 구현해 봅니다


### 10845  큐
큐의 개념을 익히고 실습해 봅니다

문제
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
예제 출력 1 
1
2
2
0
1
2
-1
0
1
-1
0
3
힌트
출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: compro0317
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1260  DFS와 BFS
스택과 큐를 이용한 그래프 탐색법을 실습해 봅니다

문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 한 간선이 여러 번 주어질 수도 있는데, 간선이 하나만 있는 것으로 생각하면 된다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
힌트
출처
문제를 만든 사람: author5
빠진 조건을 찾은 사람: pumpyboom
알고리즘 분류
보기

메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1966  프린터 큐
큐의 개념이 응용된 문제를 해결해 봅니다

문제
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력
첫 줄에 test case의 수가 주어진다. 각 test case에 대해서 문서의 수 N(100이하)와 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 어떤 위치에 있는지를 알려주는 M(0이상 N미만)이 주어진다. 다음줄에 N개 문서의 중요도가 주어지는데, 중요도는 적절한 범위의 int형으로 주어진다. 중요도가 같은 문서가 여러 개 있을 수도 있다. 위의 예는 N=4, M=0(A문서가 궁금하다면), 중요도는 2 1 4 3이 된다.

출력
각 test case에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

예제 입력 1 
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
예제 출력 1 
1
2
5
힌트
출처
ACM-ICPC > Regionals > Europe > Northwestern European Regional Contest > NWERC 2006 F번

링크
ACM-ICPC Live Archive
PKU Judge Online
TJU Online Judge
Sphere Online Judge
HDU Online Judge
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 11866 조세퍼스 문제 0
큐를 이용해 조세퍼스 수열을 출력하는 문제1

문제
조세퍼스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다. 이제 순서대로 M번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 1,000)

 

출력
예제와 같이 조세퍼스 순열을 출력한다.

 

예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
힌트
출처
문제를 만든 사람: baekjoon
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1158  조세퍼스 문제
큐를 이용해 조세퍼스 수열을 출력하는 문제2

문제
조세퍼스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 M(≤ N)이 주어진다. 이제 순서대로 M번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, M)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 M이 주어지면 (N,M)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ M ≤ N ≤ 5,000)

출력
예제와 같이 조세퍼스 순열을 출력한다.

예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
힌트
출처
문제를 만든 사람: author5
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



## 덱 사용하기
덱을 구현해 봅니다

###   10866 덱
덱의 개념을 익히고 실습해 봅니다

문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘쨰 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

예제 입력 1 
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
예제 출력 1 
2
1
2
0
2
1
-1
0
1
-1
0
3
힌트
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1021  회전하는 큐
덱을 활용하여 풀 수 있는 문제를 해결해 봅니다

문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이 때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
10 3
1 2 3
예제 출력 1 
0
힌트
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: dhdh6190
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 5430  AC
덱을 활용하여 풀 수 있는 문제를 해결해 봅니다

문제
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

출력
각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

예제 입력 1 
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
예제 출력 1 
[2,1]
error
[1,2,3,5,8]
error
힌트
출처
ACM-ICPC > Regionals > Europe > Northwestern European Regional Contest > Benelux Algorithm Programming Contest > BAPC 2012 I번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: chatterboy doju
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



##  피보나치 수
피보나치 수를 구해 봅니다

### 2747  피보나치 수
피보나치 수를 점화식을 이용하여 구합니다


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2748  피보나치 수 2
피보나치 수를 점화식을 이용하여 구합니다

문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

예제 입력 1 
10
예제 출력 1 
55
힌트
비슷한 문제
2748번. 피보나치 수 2
2749번. 피보나치 수 3
10826번. 피보나치 수 4
10870번. 피보나치 수 5
메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2749  피보나치 수 3
피보나치 수를 행렬 곱셈을 이용하여 빠르게 계산해봅니다

피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 출력한다.

예제 입력 1 
10
예제 출력 1 
55
힌트
비슷한 문제
2747번. 피보나치 수
2749번. 피보나치 수 3
10826번. 피보나치 수 4
10870번. 피보나치 수 5
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1003  피보나치 함수
피보나치 수를 구할 때, 특정 함수가 몇번 사용되는지 구하는 문제

문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

1
2
3
4
5
6
7
8
9
10
11
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.

첫째 줄에 N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

예제 입력 1 
3
0
1
3
예제 출력 1 
1 0
0 1
1 2
힌트
출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: doju
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



## 이항 계수
이항 계수를 구해봅니다

### 11050 이항 계수 1
재귀 함수로 이항 계수를 계산해봅니다

문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
 를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
힌트
출처
문제를 만든 사람: baekjoon
메모



#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 11051 이항 계수 2
동적 계획법이나 메모이제이션으로 이항 계수를 계산해봅니다

문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 1,000, 0 ≤  ≤ )

출력
 를 10,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
힌트
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: emiyagugizzada
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 11401 이항 계수 3
곱셈의 역원을 사용하여 이항 계수를 빠르게 계산해봅니다

문제
자연수 과 정수 가 주어졌을 때 이항 계수 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )

출력
 를 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
힌트
출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: kjo7811
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 10872 팩토리얼
N!을 구하는 문제

문제
0보다 크거나 같은 정수 N이 주어진다. 이 때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력 1 
10
예제 출력 1 
3628800
힌트
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1676  팩토리얼 0의 개수
N!의 뒤에서 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구하는 문제

문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1 
10
예제 출력 1 
2
힌트
출처
문제를 만든 사람: author6
데이터를 추가한 사람: his130
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2407  조합
nCm을 구하는 문제1

문제
nCm을 출력한다.

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.

예제 입력 1 
100 6
예제 출력 1 
1192052400
힌트
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 6591  이항 쇼다운
nCm을 구하는 문제2

문제
n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 두 자연수 n(n ≥ 1)과 k(0 ≤ k ≤n)로 이루어져 있다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 정답을 출력한다. 항상 정답이 231보다 작은 경우만 입력으로 주어진다.

예제 입력 1 
4 2
10 5
49 6
0 0
예제 출력 1 
6
252
13983816
힌트
출처
Contest > University of Ulm Local Contest > University of Ulm Local Contest 1997 B번

문제를 번역한 사람: baekjoon
링크
PKU Judge Online
ZJU Online Judge
TJU Online Judge
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 9375  패션왕 신해빈
이항계수를 사용해 옷 입는 조합의 가짓수를 출력하는 문제

문제
해빈이는 패션에 매우 민감해서 한번 입었던 옷들의 조합을 절대 다시 입지 않는다. 예를 들어 오늘 해빈이가 안경, 코트, 상의, 신발을 입었다면, 다음날은 바지를 추가로 입거나 안경대신 렌즈를 착용하거나 해야한다. 해빈이가 가진 의상들이 주어졌을때 과연 해빈이는 알몸이 아닌 상태로 몇 일동안 밖에 돌아다닐 수 있을까?

입력
첫째 줄에 테스트 케이스가 주어진다. 테스트 케이스는 최대 100이다.

각 테스트 케이스의 첫째 줄에는 해빈이가 가진 의상의 수 n(0 ≤ n ≤ 30)이 주어진다.
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분되어 주어진다. 같은 종류의 의상은 하나만 입을 수 있다.
모든 문자열은 1이상 20이하의 알파벳 소문자로 이루어져있으며 같은 이름을 가진 의상은 존재하지 않는다.

출력
각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우를 출력하시오.

예제 입력 1 
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
예제 출력 1 
5
3
힌트
첫번째 테스트 케이스는 headgear에 해당하는 의상이 hat, turban이며 eyewear에 해당하는 의상이 sunglasses이므로   (hat), (turban), (sunglasses), (hat,sunglasses), (turban,sunglasses)로 총 5가지 이다.

출처
ACM-ICPC > Regionals > Europe > Northwestern European Regional Contest > Benelux Algorithm Programming Contest > BAPC 2013 I번

문제를 번역한 사람: lll4592
문제의 오타를 찾은 사람: sunsal0704
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



##  동적 계획법 기초
기초적인 동적 계획법 문제들을 풀어봅니다

### 1003  피보나치 함수
피보나치 수열을 동적계획법으로 계산해봅니다


#### 풀이



### 1149  RGB거리
i번째 집을 각각의 색으로 칠할 때, 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제를 정의해봅니다

문제
RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다. 또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다. 집 i의 이웃은 집 i-1과 집 i+1이다. 처음 집과 마지막 집은 이웃이 아니다.

각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용, 파랑으로 드는 비용이 주어질 때, 모든 집을 칠할 때 드는 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 수 N이 주어진다. N은 1,000보다 작거나 같다. 둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때, 초록으로 칠할 때, 파랑으로 칠할 때 드는 비용이 주어진다. 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
힌트
출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: djm03178
데이터를 추가한 사람: rdd6584
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1932  숫자삼각형
아랫층으로만 갈 수 있는 점에 착안하여 부분문제를 정의해봅니다

문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 숫자 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 숫자는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1줄까지 숫자 삼각형이 주어진다.

출력
첫째 줄에는 최대가 되는 합을 출력한다.

예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
힌트
출처
Olympiad > International Olympiad in Informatics > IOI 1994 1번

잘못된 조건을 찾은 사람: djm03178
데이터를 추가한 사람: hwangtmdals
문제의 오타를 찾은 사람: Martian
잘못된 데이터를 찾은 사람: thanatos0128
링크
PKU Judge Online
Sphere Online Judge
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2579  계단 오르기
i번째 계단에 오를 때, 몇 개의 연속한 계단을 올랐는지를 고려하여 부분문제를 정의해봅니다

문제
계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

![stair1.png](images/stair1.png)

예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째, 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.

![stair2.png](images/stair2.png)

계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최대값을 구하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최대값을 출력한다.

예제 입력 1 
6
10
20
15
25
10
20
예제 출력 1 
75
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 초등부 4번

알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1463  1로 만들기
메모이제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최소값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최소값을 출력한다.

예제 입력 1 
2
예제 출력 1 
1
예제 입력 2 
10
예제 출력 2 
3
힌트
10의 경우에 10 -> 9 -> 3 -> 1 로 3번 만에 만들 수 있다.

출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: dynamiseus
문제의 오타를 찾은 사람: jugol
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1005  ACM Craft
동적 계획법을 이용해 특정 건물을 짓기 위해 걸리는 최단시간을 계산하는 문제

문제
서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction Manager Craft)가 발매되었다.

이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는 순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.

![acm_craft](images/acm_craft.jpg)

위의 예시를 보자.

이번 게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이 가능하다) 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.

따라서 4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다. 그리고 2번 건물과 3번 건물을 동시에 건설하기 시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 3번 건물이 완성되고 나면 그때 4번 건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다.

프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다. 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고 있었다. 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.

 

입력
첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다) 

둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 

마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다. (1 ≤ N ≤ 1000, 1 ≤ K ≤ 100000 , 1≤ X,Y,W ≤ N, 0 ≤ D ≤ 100000)

출력
건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

모든 건물을 지을 수 없는 경우는 없다.

예제 입력 1 
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
예제 출력 1 
120
39
힌트
출처
잘못된 조건을 찾은 사람: annaria
문제를 만든 사람: author1
데이터를 추가한 사람: djm03178 minshogi zzaa9898
잘못된 데이터를 찾은 사람: tncks0121
문제의 오타를 찾은 사람: xivnick
빠진 조건을 찾은 사람: yclock
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 10844 쉬운 계단 수
동적 계획법을 이용해 계단 수를 구하는 문제

문제
45656이란 수를 보자.

이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.

세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
1
예제 출력 1 
9
예제 입력 2 
2
예제 출력 2 
17
힌트
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2293  동전 1
메모이제이션으로 동전들을 적당히 사용해 가치의 합이 k원이 되는 경우의 수를 구하는 문제

문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. (각각의 동전은 몇 개라도 사용할 수 있다.)

입력
첫째줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.

예제 입력 1 
3 10
1
2
5
예제 출력 1 
10
힌트
출처
빠진 조건을 찾은 사람: goodcrane3
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2156  포도주 시식
규칙에 따라 포도주를 마실 때, 최대로 마실 수 있는 포도주의 양을 구하는 문제

문제
효주는 포도주 시식회에 갔다. 그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다. 효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.

포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다. 1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 

예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.

입력
첫째 줄에 포도주 잔의 개수 n이 주어진다. (1≤n≤10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.

예제 입력 1 
6
6
10
13
9
8
1
예제 출력 1 
33
힌트
출처
빠진 조건을 찾은 사람: keith
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1520  내리막 길
내리막길로만 이동하는 경우의 수를 구하는 문제

내리막 길
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  14445 3052  2259  25.823%
문제
여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.



현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

![downway1](images/downway1.png)

![downway2](images/downway2.png)

![downway3](images/downway3.png)

![downway4](images/downway4.png)



지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 지도의 세로의 크기 M과 가로의 크기 N이 빈칸을 사이에 두고 주어진다. 이어 다음 M개 줄에 걸쳐 한 줄에 N개씩 위에서부터 차례로 각 지점의 높이가 빈 칸을 사이에 두고 주어진다. M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수이다.

출력
첫째 줄에 이동 가능한 경로의 수 H를 출력한다. 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수이다.

예제 입력 1 
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
예제 출력 1 
3
힌트
출처
[Olympiad](https://www.acmicpc.net/category/2) > [한국정보올림피아드시․도지역본선](https://www.acmicpc.net/category/57) > [지역본선 2006](https://www.acmicpc.net/category/70) > [고등부](https://www.acmicpc.net/category/detail/369) 3번

데이터를 추가한 사람: doju
잘못된 데이터를 찾은 사람: hotehrud tncks0121
문제의 오타를 찾은 사람: imgosari
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 9251  LCS
LCS를 구하는 문제1

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
힌트
출처
문제를 만든 사람: baekjoon
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 11066 파일 합치기
파일들의 길이를 규칙에 따라 합치는 데 필요한 최소 비용을 구하는 문제

문제
소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다. 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다. 이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, C1, C2, C3, C4가 연속적인 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이 때 비용 60이 필요하다. 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 다른 방법으로 파일을 합치면 비용을 줄일 수 있다. 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이 때 필요한 총 비용은 70+80+150=300 이다.

소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.

입력
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데, T는 입력의 맨 첫 줄에 주어진다.각 테스트 데이터는 두 개의 행으로 주어지는데, 첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 500)가 주어진다. 두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다. 파일의 크기는 10,000을 초과하지 않는다.

출력
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행에 출력하는데, 모든 장을 합치는데 필요한 최소비용을 출력한다.

예제 입력 1 
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
예제 출력 1 
300
864
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2015 F번

알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1912  연속합
주어진 수 중 연속된 숫자를 선택해 구할 수 있는 합 중 가장 큰 합을 구하는 문제

연속합
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  28952 7636  5313  26.985%
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 숫자를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 숫자는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1≤n≤100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
33
힌트
출처
데이터를 추가한 사람: dohyeokkim doju kimdr123
빠진 조건을 찾은 사람: isac322 Qwaz
잘못된 데이터를 찾은 사람: tncks0121
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 9461  파도반 수열
파도반 수열을 구하는 문제

문제
오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

![pandovan](images/pandovan.png)

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

출력
각 테스트 케이스 마다 P(N)을 출력한다.

예제 입력 1 
2
6
12
예제 출력 1 
3
16
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Daejeon 2013 G번

문제를 번역한 사람: baekjoon
링크
ACM-ICPC Live Archive
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 9252  LCS 2 [##]
LCS를 구하는 문제2

문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러가지인 경우에는 아무거나 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
ACAK
힌트
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


@@@
##  구현

###   10871 X보다 작은 수
수열과 X가 주어질 때, 수열에서 X보다 작은 수를 모두 출력하는 문제

#### 메모
- if문 사용해보기 10871번과 중복


### 2490  윷놀이
윳짝의 상태를 보고 출력하는 문제

문제
우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

입력
첫째 줄부터 셋째 줄까지 각 줄에 각각 한 번 던진 윷짝들의 상태를 나타내는 네 개의 정수(0 또는 1)가  빈칸을 사이에 두고 주어진다.

출력
첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를  도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력 한다.

예제 입력 1 
0 1 0 1
1 1 1 0
0 0 1 1
예제 출력 1 
B
A
B
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2009 > 초등부 1번

알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2577  숫자의 개수
세 수가 주어졌을 때 세 수의 곱에서 각각의 숫자가 사용된 횟수를 구하는 문제

#### 메모
- 1차원 배열 사용하기 2577번과 중복


### 1022  소용돌이 예쁘게 출력하기
소용돌이 모양을 출력하는 문제

문제
크기가 무한인 정사각형 모눈종이가 있다. 모눈종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.

이 모눈종이 전체를 양의 정수를 소용돌이 모양으로 채울 것이다. 일단 숫자 1을 0행 0열에 쓴다. 그리고 나서 0행 1열에 숫자 2를 쓴다. 거기서 부터 소용돌이는 반시계 방향으로 시작된다. 다음 숫자는 다음과 같이 채우면 된다.

~~~
    -3 -2 -1  0  1  2  3
    --------------------
-3 |37 36 35 34 33 32 31
-2 |38 17 16 15 14 13 30
-1 |39 18  5  4  3 12 29
 0 |40 19  6  1  2 11 28
 1 |41 20  7  8  9 10 27
 2 |42 21 22 23 24 25 26
 3 |43 44 45 46 47 48 49
~~~

이 문제는 위와 같이 채운 것을 예쁘게 출력하면 된다. r1, c1, r2, c2가 입력으로 주어진다. r1, c1은 가장 왼쪽 위 칸이고, r2, c2는 가장 오른쪽 아래 칸이다.

예쁘게 출력한다는 것은 다음과 같이 출력하는 것이다.

출력은 r1행부터 r2행까지 차례대로 출력한다.
각 원소는 공백으로 구분한다.
모든 행은 같은 길이를 가져야 한다.
공백의 길이는 최소로 해야 한다.
모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 한다.
만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.
입력
첫째 줄에 r1, c1, r2, c2가 주어진다. 모두 절대값이 5000보다 작거나 같은 정수이고, r2-r1은 0보다 크거나 같고, 49보다 작거나 같으며, c2-c1은 0보다 크거나 같고, 4보다 작거나 같다.

출력
r2-r1+1개의 줄에 소용돌이를 예쁘게 출력한다.

예제 입력 1 
-3 -3 2 0
예제 출력 1 
37 36 35 34
38 17 16 15
39 18  5  4
40 19  6  1
41 20  7  8
42 21 22 23
힌트
출처
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: lobo_prix
빠진 조건을 찾은 사람: myungwoo
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 3053  택시 기하학
원의 넓이를 출력하는 문제

문제
19세기 독일 수학자 헤르만 민코프스키는 비유클리드 기하학 중 택시 기하학을 고안했다.

택시 기하학에서 두 점 T1(x1,y1), T2(x2,y2) 사이의 거리는 다음과 같이 구할 수 있다.

D(T1,T2) = |x1-x2| + |y1-y2|

두 점 사이의 거리를 제외한 나머지 정의는 유클리드 기하학에서의 정의와 같다.

따라서 택시 기하학에서 원의 정의는 유클리드 기하학에서 원의 정의와 같다.

원: 평면 상의 어떤 점에서 거리가 일정한 점들의 집합

반지름 R이 주어졌을 때, 유클리드 기하학에서 원의 넓이와, 택시 기하학에서 원의 넓이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 반지름 R이 주어진다. R은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 유클리드 기하학에서 반지름이 R인 원의 넓이를, 둘째 줄에는 택시 기하학에서 반지름이 R인 원의 넓이를 출력한다.

넓이는 소수점 여섯째 자리까지 출력한다.

예제 입력 1 
1
예제 출력 1 
3.141593
2.000000
힌트
유클리드 기하학: 한국어 위키 영문 위키 Wolfram Mathworld

비유클리드 기하학: 한국어 위키 영문 위키 Wolfram Mathworld

택시 기하학: 한국어 위키 영문 위키 Wolfram Mathworld

출처
Contest > Croatian Open Competition in Informatics > COCI 2006/2007 > Contest #1 2번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: onjo0127
링크
TJU Online Judge
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



##  최대공약수/최소공배수

### 1934  최소공배수
최소공배수를 구하는 문제1

문제
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

출력
첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

예제 입력 1 
3
1 45000
6 10
13 17
예제 출력 1 
45000
30
221
힌트
출처
문제의 오타를 찾은 사람: jason9319 kyo20111
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 13241 최소공배수
최소공배수를 구하는 문제2

문제
정수 A는 정수 B를 0보다 큰 정수인 N회 곱해 A를 구할 수 있다면 A는 B의 배수이다.

예:

10은 5의 배수이다 (5*2 = 10)
10은 10의 배수이다(10*1 = 10)
6은 1의 배수이다(1*6 = 6)
20은 1, 2, 4,5,10,20의 배수이다.
다른 예:

2와 5의 최소공배수는 10이고, 그 이유는 2와 5보다 작은 공배수가 없기 때문이다.
10과 20의 최소공배수는 20이다.
5와 3의 최소공배수는 15이다.
당신은 두 수에 대하여 최소공배수를 구하는 프로그램을 작성 하는 것이 목표이다.

입력
한 줄에 두 정수 A와 B가 공백으로 분리되어 주어진다.

50%의 입력 중 A와 B는 1000(103)보다 작다. 다른 50%의 입력은 1000보다 크고 100000000(108)보다 작다.

추가: 큰 수 입력에 대하여 변수를 64비트 정수로 선언하시오. C/C++에서는 long long int를 사용하고, Java에서는 long을 사용하시오.

출력
A와 B의 최소공배수를 한 줄에 출력한다.

예제 입력 1 
1 1
예제 출력 1 
1
예제 입력 2 
3 5
예제 출력 2 
15
예제 입력 3 
1 123
예제 출력 3 
123
예제 입력 4 
121 199
예제 출력 4 
24079
힌트
출처
Olympiad > All-Ireland Programming Olympiad > 2016 AIPO National Finals 2번

문제를 번역한 사람: n_agi
메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2609  최대공약수와 최소공배수
최대공약수와 최소공배수를 구하는 문제

문제
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를,둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

예제 입력 1 
24 18
예제 출력 1 
6
72
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 중등부 1번

Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 고등부 1번

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1850  최대공약수
111,11111 이런 형식의 꼴의 수의 최대공약수를 구하는 문제

최대공약수
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  7923  1683  1322  23.169%
문제
모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이 때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.

예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.

입력
첫째 줄에 두 자연수 A와 B를 이루는 1의 개수가 주어진다. 입력되는 수는 19자리를 넘지 않는 자연수이다.

출력
첫째 줄에 A와 B의 최대공약수를 출력한다. 정답은 천만 자리를 넘지 않는다.

예제 입력 1 
3 4
예제 출력 1 
1
예제 입력 2 
3 6
예제 출력 2 
111
힌트
출처
문제의 오타를 찾은 사람: effectiveservice
빠진 조건을 찾은 사람: koosaga
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 2981  검문
N개의 수를 M으로 나누었을 때, 나머지가 전부 같은 M을 찾는 문제

문제
트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다. 경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에, 검문하는데 엄청나게 오랜 시간이 걸린다.

상근이는 시간을 떼우기 위해서 수학 게임을 하기로 했다.

먼저 근처에 보이는 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을 모두 찾으려고 한다. M은 1보다 커야 한다.

N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.

입력
첫째 줄에 종이에 적은 수의 개수 N이 주어진다. (2 ≤ N ≤  100)

다음 줄부터 N개 줄에는 종이에 적은 수가 하나씩 주어진다. 이 수는 모두 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다. 같은 수가 두 번 이상 주어지지 않는다.

항상 M이 하나 이상 존재하는 경우만 입력으로 주어진다.

출력
첫재 줄에 가능한 M을 공백으로 구분하여 모두 출력한다. 이 때, M은 증가하는 순서이어야 한다.

예제 입력 1 
3
6
34
38
예제 출력 1 
2 4
힌트
출처
Contest > Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #6 3번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: winan305 xohzzwn6kcj9
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 3036  링
첫번째 링을 한 바퀴 돌렸을 때, 나머지 링이 몇바퀴 도는 지 구하는 문제

문제
상근이는 창고에서 링 N개를 발견했다. 상근이는 각각의 링이 앞에 있는 링과 뒤에 있는 링과 접하도록 바닥에 내려놓았다. 

![ring](images/ring.png)

상근이는 첫 번째 링을 돌리기 시작했고, 나머지 링도 같이 돌아간다는 사실을 발견했다. 나머지 링은 첫 번째 링 보다 빠르게 돌아가기도 했고, 느리게 돌아가기도 했다. 이렇게 링을 돌리다 보니 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 도는지 궁금해졌다.

링의 반지름이 주어진다. 이 때, 첫 번째 링을 한 바퀴 돌리면, 나머지 링은 몇 바퀴 돌아가는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 링의 개수 N이 주어진다. (3 ≤ N ≤ 100)

다음 줄에는 링의 반지름이 상근이가 바닥에 놓은 순서대로 주어진다. 반지름은 1과 1000를 포함하는 사이의 자연수이다.

출력
출력은 총 N-1줄을 해야 한다. 첫 번째 링을 제외한 각각의 링에 대해서, 첫 번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력한다.

예제 입력 1 
4
12 3 8 4
예제 출력 1 
4/1
3/2
3/1
힌트
출처
Contest > Croatian Open Competition in Informatics > COCI 2006/2007 > Contest #4 3번

문제를 번역한 사람: baekjoon
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



##  시뮬레이션

### 2455  지능형 기차
기차에 탄 사람과 내린 사람의 수가 주어질 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 문제

문제
최근에 개발된 지능형 기차가 1번역(출발역)부터 4번역(종착역)까지 4개의 정차역이 있는 노선에서 운행되고 있다. 이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다. 이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산하려고 한다. 단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여, 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.

![stations](images/stations.png)

  내린 사람 수 탄 사람 수
1번역(출발역)  0 32
2번역 3 13
3번역 28  25
4번역(종착역)  39  0

예를 들어, 위와 같은 경우를 살펴보자. 이 경우, 기차 안에 사람이 가장 많은 때는 2번역에서 3명의 사람이 기차에서 내리고, 13명의 사람이 기차에 탔을 때로, 총 42명의 사람이 기차 안에 있다.

이 기차는 다음 조건을 만족하면서 운행된다고 가정한다.

기차는 역 번호 순서대로 운행한다.
출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0이다.
각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다.
4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

입력
각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 

출력
첫째 줄에 최대 사람 수를 출력한다.  

예제 입력 1 
0 32
3 13
28 25
39 0
예제 출력 1 
42
힌트
출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2011 > 초등부 1번

알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1094  막대기
64cm인 막대를 잘라 길이 x의 막대기로 바꾸는 문제

문제
지민이는 길이가 64cm인 막대를 가지고 있다. 어느날, 그는 길이가 Xcm인 막대가 가지고 싶어졌다. 지민이는 원래 가지고 있던 막대를 더 작은 막대로 자른다음에, 풀로 붙여서 길이가 Xcm인 막대를 만드려고 한다.

막대를 자르는 가장 쉬운 방법은 절반으로 자르는 것이다. 지민이는 아래와 같은 과정을 거쳐서 막대를 자르려고 한다.

지민이가 가지고 있는 막대의 길이를 모두 더한다. 처음에는 64cm 막대 하나만 가지고 있다. 이 때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
X가 주어졌을 때, 위의 과정을 거친다면, 몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 구하는 프로그램을 작성하시오. 

입력
첫째 줄에 X가 주어진다. X는 64보다 작거나 같은 자연수이다.

출력
문제의 과정을 거친다면, 몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 출력한다.

예제 입력 1 
23
예제 출력 1 
4
예제 입력 2 
32
예제 출력 2 
1
예제 입력 3 
64
예제 출력 3 
1
예제 입력 4 
48
예제 출력 4 
2
힌트
출처
문제의 오타를 찾은 사람: alphago92 jjacks
문제를 번역한 사람: baekjoon
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1057  토너먼트
N명이 토너먼트를 할 때, X,Y가 몇번째 토너먼트에서 대결할 지 구하는 문제

문제
김지민은 N명이 참가하는 스타 토너먼트에 진출했다. 토너먼트는 다음과 같이 진행된다. 일단 N명의 참가자는 번호가 1번부터 N번까지 배정받는다. 그러고 난 후에 서로 인접한 번호끼리 스타를 한다. 이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서 떨어진다. 만약 그 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출한다. 다음 라운드에선 다시 참가자의 번호를 1번부터 매긴다. 이 때, 번호를 매기는 순서는 처음 번호의 순서를 유지하면서 1번부터 매긴다. 이 말은 1번과 2번이 스타를 해서 1번이 진출하고, 3번과 4번이 스타를 해서 4번이 진출했다면, 4번은 다음 라운드에서 번호 2번을 배정받는다. 번호를 다시 배정받은 후에 한 명만 남을 때까지 라운드를 계속 한다.

마침 이 스타 대회에 임한수도 참가했다. 김지민은 갑자기 스타 대회에서 우승하는 욕심은 없어지고, 몇 라운드에서 임한수와 대결하는지 궁금해졌다. 일단 김지민과 임한수는 서로 대결하기 전까지 항상 이긴다고 가정한다. 1 라운드에서 김지민의 번호와 임한수의 번호가 주어질 때, 과연 김지민과 임한수가 몇 라운드에서 대결하는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다. N은 100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.

출력
첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.

예제 입력 1 
16 8 9
예제 출력 1 
4
힌트
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: dreammusic23
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1021  회전하는 큐
큐로 주어진 연산을 수행하는 최소 횟수를 구하는 문제

회전하는 큐
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  6573  2154  1775  34.688%
문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이 때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
10 3
1 2 3
예제 출력 1 
0
힌트
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: dhdh6190
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1024  수열의 합
합이 N이며 길이가 L 이상인 가장 짧은 정수 리스트를 구하는 문제

수열의 합
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
2 초 128 MB  5035  1090  886 25.178%
문제
N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L이면서 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 L이 주어진다. N은 1000000000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

예제 입력 1 
18 2
예제 출력 1 
5 6 7
힌트
출처
문제를 번역한 사람: baekjoon
알고리즘 분류
보기

메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 10253 헨리
주어진 분수를 헨리 표현식으로 표현하는 문제

문제
이제 10 살이 된 헨리(Henry)는 수학에 소질이 있다. 수학선생님인 아메스(Ahmes)는 오늘 헨리에게 분수에 대해 가르쳐줬고, 헨리는 분수를 이리저리 계산해보는 것이 너무 재미있었다. 그러던 중에 헨리는 1 보다 작은 분수를 여러 개의 서로 다른 단위분수의 합으로 표현할 수 있다는 것을 알아내었다. 여기서 단위분수란 분자가 1 인 분수를 말한다. 헨리는 여러 개의 분수에 대해 이를 시도해봤고, 시도해본 분수들은 모두 서로 다른 단위분수의 합으로 표현할 수 있었다. 예를 들어, 은 와 같이 두 개의 단위 분수의 합으로 나타낼 수 있다. 

헨리는 이런 발견을 선생님인 아메스에게 자랑스럽게 이야기했다. 아메스는 이를 듣고는 크게 기뻐하며 어린 제자를 칭찬했고, 이와 같이 하나의 분수를 서로 다른 단위분수의 합으로 표현한 것을 헨리식 표현법(Henry representation)이라고 이름 지었다. 즉, 분수 의 헨리식 표현법은 총합이  와 같게 되는 서로 다른 단위분수의 나열이다. 헨리와 아메스는 헨리식 표현법에 대하여 더욱 연구하였고, 마침내 모든 1 보다 작은 분수는 헨리식 표현법이 가능함을 증명하였다. 또한 헨리식 표현법이 유일하지 않다는 것도 알 수 있었다. 예를 들면,  와 같이 여러가지 다른 헨리식 표현법이 존재할 수 있다. 단, 정의에 의해, 헨리식 표현법에는 같은 단위분수가 두 개 이상 포함될 수 없으므로  는 헨리식 표현법이 아님을 유념해야 한다.

아메스와 헨리는 또한 주어진 분수의 헨리식 표현법을 구하는 간단한 방법도 고안해냈다.  인 양의 정수 와 로 이루어진 분수 가 주어질 때에, 먼저 를 만족하는 가장 큰 단위 분수 를 계산한다. 그런 다음  에서 를 뺀 나머지에 대하여 위의 과정을 반복한다. 즉, 를 만족하는 가장 큰 단위분수 를 계산하고 뺀다. 이러한 과정을 나머지가 남지 않을 때까지 반복한다. 그러면 서로 다른 단위분수들 을 순서대로 얻게 되며 그들의 합은 정확히 와 같아진다. 아메스와 헨리는 이 알고리즘이 항상 종료하며 합이 가 되는 서로 다른 단위분수들, 즉 헨리식 표현법을 출력함을 증명하였다.

아메스와 헨리는 당신에게 그들의 알고리즘을 컴퓨터 프로그램으로 구현해줄 것을 부탁했다. 입력으로 주어지는 1 보다 작은 분수  를 아메스와 헨리의 알고리즘을 수행하여 헨리식 표현법을 계산할 때에 마지막 단위 분수의 분모를 출력하는 프로그램을 작성하시오. 예를 들어. 라면, 아메스와 헨리의 알고리즘은  을 출력하게 되므로 당신의 프로그램은 반드시 70 을 출력해야 한다.

입력
입력 데이터는 표준입력을 사용한다. 입력은 T 개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 테스트 데이터의 개수 T 가 정수로 주어진다. 각 테스트 데이터는 한 줄로 구성되며, 여기에는 입력 분수 를 의미하는 두 개의 정수 와  (1 ≤  <  ≤ 10,000) 가 주어진다. 이 때, 와 는 서로소이며, 입력분수  에 대해 아메스와 헨리의 알고리즘을 실행했을 때에 출력되는 단위 분수가 순서대로  라면,  의 부등식을 만족한다고 가정할 수 있다.

출력
출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 정확히 한 줄을 출력해야 하며 여기에는 정수 하나만을 출력한다. 이 정수는 아메스와 헨리의 알고리즘을 입력 분수 에 대해 실행했을 때, 출력되는 헨리식 표현법의 마지막 단위분수의 분모와 같아야 한다. 

예제 입력 1 
3
4 23
5 7
8 11
예제 출력 1 
138
70
4070
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2014 D번

데이터를 만든 사람: baekjoon
문제의 오타를 찾은 사람: myungwoo
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1107  리모컨
버튼을 가장 적게 누르며 N까지 이동하는 방법을 구하는 문제

문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 중복되서 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

예제 입력 1 
5457
3
6 7 8
예제 출력 1 
6
예제 입력 2 
100
5
0 1 2 3 4
예제 출력 2 
0
예제 입력 3 
500000
8
0 2 3 4 6 7 8 9
예제 출력 3 
11117
힌트
5455++ 또는 5459--

출처
문제를 번역한 사람: baekjoon
잘못된 조건을 찾은 사람: jh05013
문제의 오타를 찾은 사람: traveler
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 10219 Meats On The Grill
불판을 뒤집는 문제

문제
Coders High 2014가 끝났다. 저녁 회식은 취소되었기 때문에 참가자들은 뿔뿔이 흩어져 저녁식사를 하기 위해 떠났다. 사람들이 모여서 먹는 저녁식사 중에서도 가장 대중적인 것은 고기! Coders High의 출제진들도 고깃집에 와서 고기를 시켰다. 명우는 고기를 굽어야 하는 중책을 맡게 되었으므로 불판 위에 고기들을 얹었다. 뛰어난 문제 해결 능력을 가진 명우는 불판 위의 고기를 다음과 같이 모델링하기로 했다.

편의상 불판을  H × W개의 칸으로 이루어진 격자로 나타내기로 하고, 고기는 격자의 여러 칸 위에 걸쳐 있는 것으로 표현한다. 또한 고기가 격자 위에 올라와 있으면, 격자를 가득 채우게 된다고 생각한다.

 시간이 지나 현재 아래쪽 면은 적당히 구워졌기 때문에 고기를 뒤집을 시간이 되었다.

![fireplate](images/fireplate.png)

같은 덩이에 속하는 고기는 뒤집을 경우 모두 같이 뒤집히게 된다. 첫 번째 그림이 원래 고기가 불판 위에 있었던 상태라고 하자. 두 번째 그림은 고기를 좌우 대칭으로 뒤집은 그림이라고 할 수 있다. 세 번째 그림은 고기를 뒤집었지만, 고기가 불판의 격자 칸 위에 제대로 위치하고 있지 않다. 명우는 이런 경우를 끔찍히 싫어하기 때문에 저렇게 뒤집지 않을 것이다. 네 번째 그림은 뒤집은 후 오른쪽으로 90˚돌려진 형태인데, 이런 형태도 가능하며, 180˚, 270˚로 돌리는 것도 가능하다.

명우는 고기가 불판 위에 올려진 상태가 주어질 때, 한 덩이에 속하는 고기 각각이 뒤집힌 상태가 되도록 만들고 싶다. 명우는 완벽주의자이기 때문에 뒤집은 후에 고기가 겹쳐져 있는 경우가 생기는 것을 끔찍히 싫어한다. 명우에게 어떻게 뒤집어야 고기를 겹치지 않게 뒤집을 수 있는지 알려주자!

입력
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 격자의 크기를 의미하는 두 정수 H, W (1 ≤ H, W ≤ 11)가 공백으로 구분되어 주어진다.

다음 H개의 줄에 현재 불판의 상태가 주어지는데, 각 줄에는 W개의 문자가 공백 없이 주어져 있다. 문자는 알파벳 소문자 혹은 '.'으로 주어지며, 알파벳 소문자가 같은 경우에는 같은 덩이에 속하는 고기라는 것을 의미한다. 같은 덩이에 속한다는 것은 이 격자들만을 이용하여 상하좌우로 움직이는 것으로 다른 모든 같은 덩이의 격자를 방문 가능하다는 것을 의미한다.

출력
각 테스트 케이스마다 각 고기덩이를 뒤집은 후의 불판의 상태를 H줄에 걸쳐서 출력한다. 각 줄에는 W개의 문자가 있어야 하며, 입력에서 주어진 각 고기 덩이가 뒤집힌 채로 있어야 한다. 이를 만족하는 어느 답을 출력해도 정답으로 인정한다.

예제 입력 1 
1
3 4
abbb
aabb
aa..
예제 출력 1 
.abb
aabb
aa.b
힌트
출처
Contest > Coder's High > Coder's High 2014 F번

Contest > Coder's High > Coder's high 2016 Round 2: Nexon Arena PB번

문제를 만든 사람: august14
문제의 오타를 찾은 사람: jh82582
메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 1547  공
컵을 공 안에 넣고, 컵의 위치를 M번 바꾸고 공이 들어있는 위치를 찾는 문제

문제
세준이는 컵 3개를 탁자위에 일렬로 놓았다. 컵의 번호는 가장 왼쪽 컵부터 순서대로 1번, 2번 3번이고, 세준이는 이 컵을 이용해서 게임을 하려고 한다.

먼저 1번컵의 아래에 공을 하나 넣는다. 세준이는 두 컵을 고른 다음, 그 위치를 바꾸려고 한다. 예를 들어, 고른 컵이 1번과 2번이라면, 1번 컵이 있던 위치에 2번 컵을 이동시키고, 동시에 2번 컵이 있던 위치에 1번 컵을 이동시켜야 한다. 위치를 바꿀 때, 컵을 먼저 들고 이동해야 한다. 따라서, 공의 위치는 가장 처음 1번컵이 있던 위치와 같다.

세준이는 컵의 위치를 총 M번 바꿀 것이며, 컵의 위치를 바꾼 방법이 입력으로 주어진다. 위치를 M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 컵의 위치를 바꾼 횟수 M이 주어지며, M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 컵의 위치를 바꾼 방법 X와 Y가 주어지며, X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미한다.

컵을 이동시키는 중에 공이 컵에서 빠져나오는 경우는 없다. X와 Y의 값은 3보다 작거나 같고, X와 Y가 같을 수도 있다.

출력
첫째 줄에 공이 들어있는 컵의 번호를 출력한다. 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.

예제 입력 1 
4
3 1
2 3
3 1
3 2
예제 출력 1 
3
힌트
출처
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: emiyagugizzada friendof865
문제의 오타를 찾은 사람: hwonjoon
알고리즘 분류
보기

메모


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



### 3163  떨어지는 개미
k번째로 떨어지는 개미를 구하는 문제

문제
개미 N마리가 막대 위에 올라가 있다. 일부 개미는 왼쪽을 바라보고 있고, 나머지 개미는 오른쪽을 바라보고 있다. 모든 개미는 매우 작아서 크기가 없는 점으로 나타낼 수 있다. 시작 신호가 주어지면, 개미는 바라보고 있는 방향으로 행진을 시작한다. 모든 개미는 동일한 속도 초속 1mm로 이동한다. 두 개미가 한 점에서 충돌하는 경우가 발생할 수 있다. 이 경우에 두 개미는 행진하는 방향을 반대 방향으로 바꾸고, 행진을 계속하게 된다. 개미가 방향을 바꾸는데 걸리는 시간은 없다. 개미가 막대의 끝에 도착하는 경우에는, 막대에서 떨어지게 된다. 막대는 땅 위에 떠있다고 가정한다.

처음에 모든 개미의 위치는 서로 다르다. 즉, 두 개미가 막대 위의 한 점에 같이 있는 경우는 없다. 개미는 부호 있는 정수로 나타낼 수 있다. 이 정수를 개미의 ID라고 한다. 개미의 ID의 부호는 개미가 처음에 바라보고 있는 방향이다. -는 왼쪽을 바라보고 있는 것이고, +는 오른쪽을 바라보고 있는 것이다. 개미의 ID의 절대값은 1부터 109까지의 정수 중 하나이다. 또, 모든 개미의 ID의 절대값은 서로 다르다. 아래 그림에는 개미가 총 6마리가 있고, ID는 {+4, +5, -1, -3, -2, +6}이다. 각 개미의 초기 위치는 {5, 8, 19, 22, 24, 25}이며, 막대의 길이 L = 30이다. 화살표는 처음에 개미가 바라보고 있는 방향을 나타낸다. 왼쪽 끝의 좌표는 0이고, 오른쪽 끝의 좌표는 30이다. ID가 +6인 개미는 시간 t = 5일 때, 막대의 오른쪽 끝에 도착하며, t = 6에 막대에서 떨어지게 된다.

![ant1](images/ant1.png)

개미가 행진을 시작하기 전의 상태 (ID와 막대 상의 위치)가 주어진다. 두 개미가 동시에 막대의 양 끝에서 떨어지는 경우에는, ID가 작은 개미가 조금 더 먼저 떨어진다고 한다. 아래 그림은 이와 같은 경우를 나타낸 그림이다. 두 개미 {-1, +2}는 끝에 동시에 도착하게 된다. -1 < +2 이기 때문에, ID가 -1인 개미가 +2인 개미보다 조금 더 먼저 떨어지게 된다. 따라서, 아래 그림의 네 개미가 떨어지는 순서는 {-1, 2, 4, 3}이 된다.

![ant2](images/ant2.png)

양의 정수 1 ≤ k ≤ n이 주어졌을 때, k번째로 떨어지는 개미를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 N, L, k가 주어진다. 다음 N개 줄에는 pi와 ai가 주어진다. ai는 개미의 ID이고, pi는 그 개미의 초기 위치이다. 항상 pi가 증가하는 순서로 (pi<pi+1) 주어진다. (1 ≤ pi ≤ L-1, 3 ≤ N ≤ 100,000, 10 ≤ L ≤ 5,000,000, 1 ≤ k ≤ N)

출력
각 테스트 케이스마다, N마리 개미 중에서 k번째로 떨어지는 개미의 ID를 출력한다. 개미의 ID가 양수인 경우에 +를 출력하면 안된다.

예제 입력 1 
2
6 30 3
5 4
8 5
19 -1
22 -3
24 -2
25 6
4 35 2
5 -1
12 3
20 4
30 2
예제 출력 1 
-2
2
힌트
출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2013 E번

문제의 오타를 찾은 사람: arine taeyangkim
문제를 번역한 사람: baekjoon
데이터를 만든 사람: myungwoo
메모

#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```


@@@@
##  분할 정복

###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



###


#### 풀이
```c++
// [[c++]]

#include <cstdio>

int main() {

}
```



