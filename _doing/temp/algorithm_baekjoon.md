~~~
^[ \t]+\n  \n
\n+```nodejs  \n\n\n```javascript\n// [[nodejs]]\n
\n+```c\+\+  \n\n\n```c++\n// [[c++]]\n
\n+```swift  \n\n\n```swift\n// [[swift]]\n
\n+## +  \n\n\n\n##
\n+(문제|입력|출력)$  \n\n#### $1
\n+예제 입력 (\d+) *$  \n\n#### 예제 입력 $1
\n+예제 출력 (\d+) *$  \n\n#### 예제 출력 $1
\n+(힌트|출처|보기|메모)$  \n\n#### $1
\n+비슷한 문제 $  \n\n#### 비슷한 문제
\n+알고리즘 분류 * \n\n#### 알고리즘 분류
~~~



## 입/출력 받아보기
입력과 출력만 사용하는 문제들로 입출력을 해봅니다

### 2557  Hello World
Hello World! 를 화면에 출력하는 문제

#### 문제
Hello World!를 출력하시오.

#### 입력
없음

#### 출력
Hello World!를 출력하시오.

#### 예제 입력 1

#### 예제 출력 1
Hello World!


```javascript
// [[nodejs]]

console.log("Hello World!")
```


```swift
// [[swift]]

print("Hello World!")
```


```c++
// [[c++]]

#include <iostream>

int main() {
  std::cout << "Hello World!\n";
  return 0;
}
```

### 1000  A+B
두 수를 입력받고 합을 출력하는 문제

#### 문제
두 수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A+B를 출력한다.

#### 예제 입력 1
1 2

#### 예제 출력 1
3

#### 힌트
여기를 누르면 1000번 예제 소스를 볼 수 있습니다.

#### 출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: doju
비슷한 문제
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


```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a+b);
```


```swift
// [[swift]]

let input =  readLine()!

let arr = input.split(separator: " ")

var a: Int = Int(arr[0])!
var b: Int = Int(arr[1])!

print(String(a+b))
```


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
3 2

#### 예제 출력 1
1

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
비슷한 문제
1000번. A+B
1008번. A/B
10998번. A×B

#### 알고리즘 분류
사칙연산
수학

#### 메모


```javascript
// [[nodejs]]

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);

console.log(a-b);
```


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

#### 예제 출력 1
123
Your_ICPC_Team_Name

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


```javascript
// [[nodejs]]

console.log("3\nhopelife")
```


```swift
// [[swift]]

print("8\nhopelife")
```



### 10172 개
그림을 출력하는 문제

#### 문제
아래 예제와 같이 개를 출력하시오.

#### 입력
없음.

#### 출력
개를 출력한다.

#### 예제 입력 1

#### 예제 출력 1
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|

#### 힌트

#### 출처
High School > PLU High School Programming Contest > PLU 2014 - Novice 3번

#### 알고리즘 분류

#### 출력

#### 메모


```javascript
// [[nodejs]]

console.log('|\\_/|\n|q p|   \/}\n( 0 )"""\\\n|"^"`    |\n||_/=\\\\__|');
```


```swift
// [[swift]]

print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
```


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

#### 예제 출력 1
강한친구 대한육군
강한친구 대한육군

#### 힌트

#### 출처
Contest > Coder's High > Coder's High 2015 Side Contest P1번

문제를 만든 사람: tae

#### 알고리즘 분류

#### 출력

#### 메모


```javascript
// [[nodejs]]

console.log("강한친구 대한육군\n강한친구 대한육군");
```


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
Hello
Baekjoon
Online Judge

#### 예제 출력 1
Hello
Baekjoon
Online Judge

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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
    Hello

Baekjoon
   Online Judge

#### 예제 출력 1
    Hello

Baekjoon
   Online Judge

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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


```swift
// [[swift]]


```



### 1001  A-B [@]
두 수의 뺄셈


```swift
// [[swift]]


```



### 10998 A×B
두 수의 곱셈

#### 문제
두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

#### 출력
첫째 줄에 A×B를 출력한다.

#### 예제 입력 1
1 2

#### 예제 출력 1
2

#### 예제 입력 2
3 4

#### 예제 출력 2
12

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
비슷한 문제
1000번. A+B
1001번. A-B
1008번. A/B

#### 알고리즘 분류
사칙연산

#### 메모


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
1 3

#### 예제 출력 1
0.33333333333333333333333333333333

#### 예제 입력 2
4 5

#### 예제 출력 2
0.8

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
비슷한 문제
1000번. A+B
1001번. A-B
10998번. A×B

#### 알고리즘 분류
사칙연산
수학

#### 메모


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
7 3

#### 예제 출력 1
10
4
21
2
1

#### 힌트

#### 알고리즘 분류
사칙연산

#### 메모


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

나머지 성공
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 256 MB  27126 16482 15308 62.056%

#### 문제
(A+B)%C는 (A%C + B%C)%C 와 같을까?

(A×B)%C는 (A%C × B%C)%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네가지 값을 구하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

#### 출력
첫째 줄에 (A+B)%C, 둘째 줄에 (A%C + B%C)%C, 셋째 줄에 (A×B)%C, 넷째 줄에 (A%C × B%C)%C를 출력한다.

#### 예제 입력 1
5 8 4

#### 예제 출력 1
1
1
0
0

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류
사칙연산
나머지 연산

#### 메모


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
1
2

#### 예제 출력 1
3

#### 힌트
비슷한 문제
1000번. A+B
10950번. A+B - 3
10951번. A+B - 4
10952번. A+B - 5
10953번. A+B - 6
11021번. A+B - 7
11022번. A+B - 8

#### 메모


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
18

#### 예제 출력 1
4

#### 예제 입력 2
4

#### 예제 출력 2
-1

#### 예제 입력 3
6

#### 예제 출력 3
2

#### 예제 입력 4
9

#### 예제 출력 4
3

#### 예제 입력 5
11

#### 예제 출력 5
3

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2010/2011 > Contest #7 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013

#### 알고리즘 분류
수학
구현

#### 메모


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
5

#### 예제 출력 1
1
2
3
4
5

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
비슷한 문제
2742번. 기찍 N

#### 알고리즘 분류

#### 출력

#### 메모


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
5

#### 예제 출력 1
5
4
3
2
1

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
비슷한 문제
2741번. N 찍기

#### 알고리즘 분류

#### 출력

#### 메모


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
2

#### 예제 출력 1
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

#### 힌트

#### 알고리즘 분류

#### 출력

#### 메모


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
5

#### 예제 출력 1
*
**
***
****
*****

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: grace0068 hchanhong

#### 알고리즘 분류

#### 출력

#### 메모


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
5

#### 예제 출력 1
    *
   **
  ***
 ****
*****

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: namnamseo

#### 알고리즘 분류

#### 출력

#### 메모


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
5

#### 예제 출력 1
*****
****
***
**
*

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
잘못된 데이터를 찾은 사람: jms100300

#### 알고리즘 분류

#### 출력

#### 메모


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
5

#### 예제 출력 1
*****
 ****
  ***
   **
    *

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모


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
1 1

#### 예제 출력 1
MON

#### 힌트

#### 알고리즘 분류
구현

#### 메모


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
3

#### 예제 출력 1
6

#### 힌트

#### 출처
Contest > Algorithmic Engagements > PA 2006 0-1번

문제를 번역한 사람: baekjoon

#### 메모


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
1
1

#### 예제 출력 1
1

#### 예제 입력 2
5
54321

#### 예제 출력 2
15

#### 예제 입력 3
25
7000000000000000000000000

#### 예제 출력 3
7

#### 예제 입력 4
11
10987654321

#### 예제 출력 4
46

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
데이터를 추가한 사람: jh05013

#### 알고리즘 분류

#### 출력

#### 메모


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
BaekjoonOnlineJudge

#### 예제 출력 1
BaekjoonOn
lineJudge

#### 예제 입력 2
OneTwoThreeFourFiveSixSevenEightNineTen

#### 예제 출력 2
OneTwoThre
eFourFiveS
ixSevenEig
htNineTen

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: eric00513

#### 알고리즘 분류

#### 출력

#### 메모


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
5
1 1
12 34
5 500
40 60
1000 1000

#### 예제 출력 1
2
46
505
100
2000


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
100

#### 예제 출력 1
A

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류
구현

#### 메모


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
20 30 10

#### 예제 출력 1
20

#### 예제 입력 2
30 30 10

#### 예제 출력 2
30

#### 예제 입력 3
40 40 40

#### 예제 출력 3
40

#### 예제 입력 4
20 10 10

#### 예제 출력 4
10

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모


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

### 10871 X보다 작은 수
정수 N개 중에서 X보다 작은 수 모두 출력해보기

#### 문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이 때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)

둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

#### 출력
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

#### 예제 입력 1
10 5
1 10 4 9 2 3 8 5 7 6

#### 예제 출력 1
1 4 2 3

#### 힌트

#### 출처
문제의 오타를 찾은 사람: jh82582 thinksong1

#### 알고리즘 분류

#### 보기

#### 메모


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
3
40 80 60

#### 예제 출력 1
75.00

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: ho94949
빠진 조건을 찾은 사람: powdragon1

#### 메모


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


### 4344 평균은 넘겠지
평균이 넘는 학생들의 퍼센테이지를 출력하는 문제

#### 문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

#### 입력
첫째 줄에는 테스트케이스 C가 주어진다.

둘째 줄부터 각 테스트케이스 마다 첫 수로 정수 N(1 <= N <= 1000)명의 학생이 주어지고 그 다음으로 N명의 0부터 100 사이의 점수가 이어서 주어진다.

#### 출력
각 케이스마다 한줄씩 평균을 넘는 학생들의 비율을 소수점 넷째자리에서 반올림하여 출력한다.

#### 예제 입력 1
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

#### 예제 출력 1
40.000%
57.143%
33.333%
66.667%
55.556%

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


### 더하기 사이클
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
26

#### 예제 출력 1
4

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
어색한 표현을 찾은 사람: doju

#### 알고리즘 분류

#### 보기

#### 메모


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



## 함수 사용하기

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

#### 예제 출력 1
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

#### 힌트

#### 출처
ACM-ICPC > Regionals > North America > Mid-Central Regional > 1998 Mid-Central Regional Programming Contest D번

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
각 자리수가 등차수열을 이루는 지 판별하는 함수를 구현해 문제를 해결해봅니다

#### 문제
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

#### 출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

#### 예제 입력 1
110

#### 예제 출력 1
99

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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
24

#### 예제 출력 1
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

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 메모


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



## 1차원 배열 사용하기

### 	1152	단어의 개수
일차원 문자열 배열에서 단어의 개수를 구해봅니다

#### 문제
영어 대소문자와 띄어쓰기만으로 이루어진 문장이 주어진다. 이 문장에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.

#### 입력
첫 줄에 영어 대소문자와 띄어쓰기로 이루어진 문장이 주어진다. 이 문장의 길이는 1,000,000을 넘지 않는다. 단어는 띄어쓰기 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.

#### 출력
첫째 줄에 단어의 개수를 출력한다.

#### 예제 입력 1
The Curious Case of Benjamin Button

#### 예제 출력 1
6

#### 힌트

#### 출처
문제를 만든 사람: author5
빠진 조건을 찾은 사람: his130

#### 알고리즘 분류

#### 보기

#### 메모


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


### 2577	숫자의 개수
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
150
266
427

#### 예제 출력 1
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

#### 힌트

#### 출처
Olympiad > 한국정보올림피아드시․도지역본선 > 지역본선 2006 > 초등부 2번

문제의 오타를 찾은 사람: pineapple
잘못된 데이터를 찾은 사람: tncks0121

#### 알고리즘 분류

#### 보기

#### 메모


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


### 8958	OX퀴즈
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
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

#### 예제 출력 1
10
9
7
55
30

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Seoul 2005 A번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jh82582
링크
ACM-ICPC Live Archive
TJU Online Judge

#### 메모


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


### 2920	음계 [#]
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
1 2 3 4 5 6 7 8

#### 예제 출력 1
ascending

#### 예제 입력 2
8 7 6 5 4 3 2 1

#### 예제 출력 2
descending

#### 예제 입력 3
8 1 7 2 6 3 5 4

#### 예제 출력 3
mixed

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2009/2010 > Contest #1 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013
문제의 오타를 찾은 사람: thinksong1

#### 알고리즘 분류

#### 보기

#### 메모


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


### 10039	평균 점수
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
10
65
100
30
95

#### 예제 출력 1
68

#### 힌트
숭과 원섭이는 40점 미만이고, 보충학습에 참여할 예정이기 때문에 40점을 받게 된다. 따라서, 점수의 합은 340점이고, 평균은 68점이 된다.

#### 출처
Olympiad > 일본정보올림피아드 예선 > JOI 2014 예선 1번

문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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


### 11654	아스키 코드
알파벳의 아스키 코드 값을 출력해봅니다

#### 문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

#### 입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

#### 출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.

#### 예제 입력 1
A

#### 예제 출력 1
65

#### 예제 입력 2
C

#### 예제 출력 2
67

#### 예제 입력 3
0

#### 예제 출력 3
48

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: eric00513

#### 알고리즘 분류

#### 보기

#### 메모


```c++
// [[c++]]

#include <iostream>

int main() {
  char c;

  scanf("%c", &c);
  printf("%d", (int)c);
}
```


### 10809	알파벳 찾기
한 단어에서 각 알파벳이 처음 등장하는 위치를 찾아봅니다

#### 문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

#### 출력
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

#### 예제 입력 1
baekjoon

#### 예제 출력 1
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

#### 힌트

#### 출처
문제를 만든 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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


### 2675	문자열 반복
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
2
3 ABC
5 /HTP

#### 예제 출력 1
AAABBBCCC
/////HHHHHTTTTTPPPPP

#### 힌트

#### 출처
ACM-ICPC > Regionals > North America > Greater New York Region > 2011 Greater New York Programming Contest A번

문제를 번역한 사람: baekjoon
잘못된 데이터를 찾은 사람: pichulia
링크
ACM-ICPC Live Archive
HDU Online Judge

#### 메모


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


### 1157	단어 공부
주어진 단어 중 가장 많이 사용된 알파벳을 출력하는 문제

#### 문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#### 입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

#### 출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

#### 예제 입력 1
Mississipi

#### 예제 출력 1
?

#### 예제 입력 2
zZa

#### 예제 출력 2
Z

#### 예제 입력 3
z

#### 예제 출력 3
Z

#### 예제 입력 4
baaa

#### 예제 출력 4
A

#### 힌트

#### 출처
문제를 만든 사람: author5
데이터를 추가한 사람: jh05013

#### 알고리즘 분류

#### 보기

#### 메모


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


### 1316	그룹 단어 체커
규칙에 맞는 알파벳의 개수를 출력하는 문제1

#### 문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

#### 출력
첫째 줄에 그룹 단어의 개수를 출력한다.

#### 예제 입력 1
3
happy
new
year

#### 예제 출력 1
3

#### 예제 입력 2
4
aba
abab
abcabc
a

#### 예제 출력 2
1

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: jh05013
문제의 오타를 찾은 사람: joonas

#### 알고리즘 분류

#### 보기

#### 메모


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


### 1152	단어의 개수
단어의 개수를 구하는 문제


```c++
// [[c++]]


```


### 2908	상수
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
734 893

#### 예제 출력 1
437

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2009/2010 > Contest #3 1번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: jongfighter

#### 알고리즘 분류

#### 보기

#### 메모


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


### 5622	다이얼
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
UNUCIC

#### 예제 출력 1
36

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2012/2013 > [Contest #6](https://www.acmicpc.net/category/detail/560) 1번

문제를 번역한 사람: baekjoon

#### 알고리즘 분류

#### 보기

#### 메모


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


### 2941	크로아티아 알파벳
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
ljes=njak

#### 예제 출력 1
6

#### 예제 입력 3
ddz=z=

#### 예제 출력 3
3

#### 예제 입력 4
nljj

#### 예제 출력 4
3

#### 예제 입력 5
c=c=

#### 예제 출력 5
2

#### 힌트

#### 출처
Contest > Croatian Open Competition in Informatics > COCI 2008/2009 > Contest #5 1번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: handong jh05013 jms100300 veydpz zzangho

#### 알고리즘 분류

#### 보기

#### 메모


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


### 2438	별찍기 - 1
출력 예시의 별 모양을 보고 규칙을 유추해 봅니다


### 2292	벌집
벌집이 형성되는 규칙을 유추해 문제를 해결해 봅니다

#### 문제

![beehouse](images/beehouse.png)
위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

#### 입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

#### 출력
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

#### 예제 입력 1
13

#### 예제 출력 1
3

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - [Daejeon Nationalwide Internet Competition 2004](https://www.acmicpc.net/category/detail/1089) B번

문제의 오타를 찾은 사람: waylight3

#### 메모


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

@@@
### 1193	분수찾기
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
14

#### 예제 출력 1
2/4

#### 힌트

#### 출처
문제를 만든 사람: author6
문제의 오타를 찾은 사람: deadlylaid

#### 메모


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
```


### 1011	Fly me to the Alpha Centauri
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
3
0 3
1 5
45 50

#### 예제 출력 1
3
3
4

#### 힌트

#### 출처
문제를 번역한 사람: AIAI

#### 메모


```c++
// [[c++]]


```


### 10250	ACM 호텔
호텔 방 번호의 규칙을 찾아 출력하는 문제

#### 문제
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 여러분은 지우를 도와 줄 프로그램을 작성하고자 한다. 즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.

문제를 단순화하기 위해서 호텔은 직사각형 모양이라고 가정하자. 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99). 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고). 이런 형태의 호텔을 H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 정문에서 엘리베이터까지의 거리는 무시한다. 또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.

![acmhotel](images/acmhotel.png)

그림 1. H = 6 이고 W = 12 인 H × W 호텔을 간략하게 나타낸 그림

방 번호는 YXX 나 YYXX 형태인데 여기서 Y 나 YY 는 층 수를 나타내고 XX 는 엘리베이터에서부터 세었을 때의 번호를 나타낸다. 즉, 그림 1 에서 빗금으로 표시한 방은 305 호가 된다.

손님은 엘리베이터를 타고 이동하는 거리는 신경 쓰지 않는다. 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다. 예를 들면 102 호 방보다는 301 호 방을 더 선호하는데, 102 호는 거리 2 만큼 걸어야 하지만 301 호는 거리 1 만큼만 걸으면 되기 때문이다. 같은 이유로 102 호보다 2101 호를 더 선호한다.

여러분이 작성할 프로그램은 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다. 첫 번째 손님은 101 호, 두 번째 손님은 201 호 등과 같이 배정한다. 그림 1 의 경우를 예로 들면, H = 6이므로 10 번째 손님은 402 호에 배정해야 한다.

#### 입력
프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W).

#### 출력
프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행을 출력하는데, 내용은 N 번째 손님에게 배정되어야 하는 방 번호를 출력한다.

#### 예제 입력 1
2
6 12 10
30 50 72

#### 예제 출력 1
402
1203

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2014 A번

데이터를 만든 사람: baekjoon
어색한 표현을 찾은 사람: hidonggi
문제의 오타를 찾은 사람: joonas startup

#### 메모


```swift
// [[swift]]


```


### 1924	2007년
2007년도 어느 날의 요일의 규칙을 찾아 출력하는 문제


```swift
// [[swift]]


```


### 2775	부녀회장이 될테야
층과 거주자 수의 규칙을 찾는 문제

부녀회장이 될테야
시간 제한 메모리 제한  제출  정답  맞은 사람 정답 비율
1 초 128 MB  5816  3238  2880  58.088%

#### 문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a 층의 b 호에 살려면 자신의 아래(a-1)층에 1호부터 b 호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정 했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있나를 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층에 i호에는 i명이 산다.

#### 입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다. (1 <= k <= 14, 1 <= n <= 14)

#### 출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

#### 예제 입력 1
2
1
3
2
3

#### 예제 출력 1
6
10

#### 힌트

#### 출처
문제의 오타를 찾은 사람: sunhmj44
어색한 표현을 찾은 사람: veydpz

#### 메모


```c++
// [[c++]]


```


### 1475	방 번호
주어진 단어를 만들기 위한 규칙을 찾는 문제

#### 문제
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

#### 입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

#### 출력
첫째 줄에 필요한 세트의 개수를 출력한다.

#### 예제 입력 1
9999

#### 예제 출력 1
2

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
데이터를 추가한 사람: doju
빠진 조건을 찾은 사람: newdeal
문제의 오타를 찾은 사람: waylight3

#### 알고리즘 분류

#### 보기

#### 메모


```c++
// [[c++]]


```


### 6064	카잉 달력
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
3
10 12 3 9
10 12 7 2
13 11 5 6

#### 예제 출력 1
33
-1
83

#### 힌트

#### 출처
ACM-ICPC > Regionals > Asia > Korea > Nationwide Internet Competition > Asia Regional - Daejeon Nationalwide Internet Competition 2013 B번

문제의 오타를 찾은 사람: 2e718 roeniss
데이터를 만든 사람: baekjoon

#### 메모


```c++
// [[c++]]


```



## 정렬해보기
정렬을 해 봅니다

### 2750	수 정렬하기
삽입 정렬, 거품 정렬 등의 간단한 정렬 알고리즘을 구현해 봅니다

#### 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절대값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#### 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

#### 예제 입력 1
5
5
2
3
4
1

#### 예제 출력 1
1
2
3
4
5

#### 힌트

#### 출처
문제의 오타를 찾은 사람: lazy_ren
비슷한 문제
2751번. 수 정렬하기 2
10989번. 수 정렬하기 3

#### 메모


```c++
// [[c++]]


```


### 2751	수 정렬하기 2
병합정렬(Merge Sort) 혹은 힙 정렬(Heap Sort)을 사용해 봅니다

#### 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

#### 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절대값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

#### 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

#### 예제 입력 1
5
5
4
3
2
1

#### 예제 출력 1
1
2
3
4
5

#### 힌트
비슷한 문제
2750번. 수 정렬하기
10989번. 수 정렬하기 3

#### 메모


```c++
// [[c++]]


```


### 10989	수 정렬하기 3
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

#### 예제 출력 1
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

#### 힌트

#### 출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: joonas
비슷한 문제
2750번. 수 정렬하기
2751번. 수 정렬하기 2

#### 알고리즘 분류

#### 보기

#### 메모


```c++
// [[c++]]


```


### 2108	통계학
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
5
1
3
8
-2
2

#### 예제 출력 1
2
2
1
10

#### 힌트

#### 출처
문제의 오타를 찾은 사람: cpp05013 skynet
데이터를 추가한 사람: yungoon

#### 메모


```c++
// [[c++]]


```


### 1427	소트인사이드
숫자들을 내림차순으로 정렬하는 문제

#### 문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

#### 입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

#### 출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

#### 예제 입력 1
2143

#### 예제 출력 1
4321

#### 힌트

#### 출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: bvba djm03178

#### 알고리즘 분류

#### 보기

#### 메모


```c++
// [[c++]]


```


### 1181	단어 정렬
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

#### 예제 출력 1
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

#### 힌트

#### 출처
문제를 만든 사람: author5

#### 알고리즘 분류

#### 보기

#### 메모


```c++
// [[c++]]


```



## 소수 구하기
소수를 구하는 여러 방법을 사용해 봅니다


### 1978	소수 찾기
소수 판별법을 연습해 봅니다


```c++
// [[c++]]


```


### 2581	소수
소수 판별법을 연습해 봅니다


```c++
// [[c++]]


```


### 1929	소수 구하기
에라토스테네스의 체를 구현해 봅니다


```c++
// [[c++]]


```


### 4948	베르트랑 공준
n이 주어졌을때, n보다 크고 2n보다 작거나 같은 소수를 구하는 문제


```c++
// [[c++]]


```


### 9020	골드바흐의 추측
n이 주어졌을 때, 두 소수의 합으로 n을 표현하는 문제


```c++
// [[c++]]


```



## 스택 사용하기 (기초)
스택을 구현해 봅니다

### 10828	스택
스택의 개념을 익히고 실습해 봅니다


```c++
// [[c++]]


```


### 1874	스택 수열
스택이 가지는 성질에 대해 고민하고 관련 문제를 해결해 봅니다


```c++
// [[c++]]


```


### 9012	괄호
주어진 문자열이 올바른 괄호열인지 판단하는 문제


```c++
// [[c++]]


```



### 2504	괄호의 값
스택을 사용해, 주어진 문자열이 올바른 괄호열인지 판단하고, 그 괄호열의 값을 출력하는 문제


```c++
// [[c++]]


```



## 큐 사용하기
큐를 구현해 봅니다


###


```c++
// [[c++]]


```



### 10845	큐
큐의 개념을 익히고 실습해 봅니다


```c++
// [[c++]]


```



### 1260	DFS와 BFS
스택과 큐를 이용한 그래프 탐색법을 실습해 봅니다


```c++
// [[c++]]


```



### 1966	프린터 큐
큐의 개념이 응용된 문제를 해결해 봅니다


```c++
// [[c++]]


```



### 11866	조세퍼스 문제 0
큐를 이용해 조세퍼스 수열을 출력하는 문제1


```c++
// [[c++]]


```



### 1158	조세퍼스 문제
큐를 이용해 조세퍼스 수열을 출력하는 문제2


```c++
// [[c++]]


```



## 덱 사용하기
덱을 구현해 봅니다

### 	10866	덱
덱의 개념을 익히고 실습해 봅니다


```c++
// [[c++]]


```



### 1021	회전하는 큐
덱을 활용하여 풀 수 있는 문제를 해결해 봅니다


```c++
// [[c++]]


```



### 5430	AC
덱을 활용하여 풀 수 있는 문제를 해결해 봅니다


```c++
// [[c++]]


```



## 	피보나치 수
피보나치 수를 구해 봅니다

### 2747	피보나치 수
피보나치 수를 점화식을 이용하여 구합니다


```c++
// [[c++]]


```



### 2748	피보나치 수 2
피보나치 수를 점화식을 이용하여 구합니다


```c++
// [[c++]]


```



### 2749	피보나치 수 3
피보나치 수를 행렬 곱셈을 이용하여 빠르게 계산해봅니다


```c++
// [[c++]]


```



### 1003	피보나치 함수
피보나치 수를 구할 때, 특정 함수가 몇번 사용되는지 구하는 문제


```c++
// [[c++]]


```



## 이항 계수
이항 계수를 구해봅니다

### 11050	이항 계수 1
재귀 함수로 이항 계수를 계산해봅니다


```c++
// [[c++]]


```



### 11051	이항 계수 2
동적 계획법이나 메모이제이션으로 이항 계수를 계산해봅니다


```c++
// [[c++]]


```



### 11401	이항 계수 3
곱셈의 역원을 사용하여 이항 계수를 빠르게 계산해봅니다


```c++
// [[c++]]


```



### 10872	팩토리얼
N!을 구하는 문제


```c++
// [[c++]]


```



### 1676	팩토리얼 0의 개수
N!의 뒤에서 처음 0이 아닌 숫자가 나올 때까지의 0의 개수를 구하는 문제


```c++
// [[c++]]


```



### 2407	조합
nCm을 구하는 문제1


```c++
// [[c++]]


```



### 6591	이항 쇼다운
nCm을 구하는 문제2


```c++
// [[c++]]


```



### 9375	패션왕 신해빈
이항계수를 사용해 옷 입는 조합의 가짓수를 출력하는 문제


```c++
// [[c++]]


```



## 	동적 계획법 기초
기초적인 동적 계획법 문제들을 풀어봅니다

### 1003	피보나치 함수
피보나치 수열을 동적계획법으로 계산해봅니다


```c++
// [[c++]]


```



### 1149	RGB거리
i번째 집을 각각의 색으로 칠할 때, 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제를 정의해봅니다


```c++
// [[c++]]


```



### 1932	숫자삼각형
아랫층으로만 갈 수 있는 점에 착안하여 부분문제를 정의해봅니다


```c++
// [[c++]]


```



### 2579	계단 오르기
i번째 계단에 오를 때, 몇 개의 연속한 계단을 올랐는지를 고려하여 부분문제를 정의해봅니다


```c++
// [[c++]]


```



### 1463	1로 만들기
메모이제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제


```c++
// [[c++]]


```



### 1005	ACM Craft
동적 계획법을 이용해 특정 건물을 짓기 위해 걸리는 최단시간을 계산하는 문제


```c++
// [[c++]]


```



### 10844	쉬운 계단 수
동적 계획법을 이용해 계단 수를 구하는 문제


```c++
// [[c++]]


```



### 2293	동전 1
메모이제이션으로 동전들을 적당히 사용해 가치의 합이 k원이 되는 경우의 수를 구하는 문제


```c++
// [[c++]]


```



### 2156	포도주 시식
규칙에 따라 포도주를 마실 때, 최대로 마실 수 있는 포도주의 양을 구하는 문제


```c++
// [[c++]]


```



### 1520	내리막 길
내리막길로만 이동하는 경우의 수를 구하는 문제


```c++
// [[c++]]


```



### 9251	LCS
LCS를 구하는 문제1


```c++
// [[c++]]


```



### 11066	파일 합치기
파일들의 길이를 규칙에 따라 합치는 데 필요한 최소 비용을 구하는 문제


```c++
// [[c++]]


```



### 1912	연속합
주어진 수 중 연속된 숫자를 선택해 구할 수 있는 합 중 가장 큰 합을 구하는 문제


```c++
// [[c++]]


```



### 9461	파도반 수열
파도반 수열을 구하는 문제


```c++
// [[c++]]


```



### 9252	LCS 2
LCS를 구하는 문제2


```c++
// [[c++]]


```



## 	구현

### 	10871	X보다 작은 수
수열과 X가 주어질 때, 수열에서 X보다 작은 수를 모두 출력하는 문제


```c++
// [[c++]]


```



### 2490	윷놀이
윳짝의 상태를 보고 출력하는 문제


```c++
// [[c++]]


```



### 2577	숫자의 개수
세 수가 주어졌을 때 세 수의 곱에서 각각의 숫자가 사용된 횟수를 구하는 문제


```c++
// [[c++]]


```



### 1022	소용돌이 예쁘게 출력하기
소용돌이 모양을 출력하는 문제


```c++
// [[c++]]


```



### 3053	택시 기하학
원의 넓이를 출력하는 문제


```c++
// [[c++]]


```



## 	최대공약수/최소공배수

### 1934	최소공배수
최소공배수를 구하는 문제1


```c++
// [[c++]]


```



### 13241	최소공배수
최소공배수를 구하는 문제2


```c++
// [[c++]]


```



### 2609	최대공약수와 최소공배수
최대공약수와 최소공배수를 구하는 문제


```c++
// [[c++]]


```



### 1850	최대공약수
111,11111 이런 형식의 꼴의 수의 최대공약수를 구하는 문제


```c++
// [[c++]]


```



### 2981	검문
N개의 수를 M으로 나누었을 때, 나머지가 전부 같은 M을 찾는 문제


```c++
// [[c++]]


```



### 3036	링
첫번째 링을 한 바퀴 돌렸을 때, 나머지 링이 몇바퀴 도는 지 구하는 문제


```c++
// [[c++]]


```



## 	시뮬레이션

### 2455	지능형 기차
기차에 탄 사람과 내린 사람의 수가 주어질 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 문제


```c++
// [[c++]]


```



### 1094	막대기
64cm인 막대를 잘라 길이 x의 막대기로 바꾸는 문제


```c++
// [[c++]]


```



### 1057	토너먼트
N명이 토너먼트를 할 때, X,Y가 몇번째 토너먼트에서 대결할 지 구하는 문제


```c++
// [[c++]]


```



### 1021	회전하는 큐
큐로 주어진 연산을 수행하는 최소 횟수를 구하는 문제


```c++
// [[c++]]


```



### 1024	수열의 합
합이 N이며 길이가 L 이상인 가장 짧은 정수 리스트를 구하는 문제


```c++
// [[c++]]


```



### 10253	헨리
주어진 분수를 헨리 표현식으로 표현하는 문제


```c++
// [[c++]]


```



### 1107	리모컨
버튼을 가장 적게 누르며 N까지 이동하는 방법을 구하는 문제


```c++
// [[c++]]


```



### 10219	Meats On The Grill
불판을 뒤집는 문제


```c++
// [[c++]]


```



### 1547	공
컵을 공 안에 넣고, 컵의 위치를 M번 바꾸고 공이 들어있는 위치를 찾는 문제


```c++
// [[c++]]


```



### 3163	떨어지는 개미
k번째로 떨어지는 개미를 구하는 문제


```c++
// [[c++]]


```


@@@



## 	분할 정복

###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



###


```c++
// [[c++]]


```



