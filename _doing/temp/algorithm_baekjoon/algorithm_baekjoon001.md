~~~
^(\d)  \n\n\n\n### $1
\n\n###   #### 풀이\n\n```c++\n// [[c++]]\n\n#include <cstdio>\n\nint main() {\n  \n\n  return 0;\n}\n```\n\n\n###


\n+(문제|입력|출력)$  \n\n#### $1
\n예제 입력 (\d+) *$  \n\n~~~\n#### 예제 입력 $1\n~~~\n
\n예제 출력 (\d+) *$  \n\n~~~\n#### 예제 출력 $1\n~~~\n
\n힌트  \n~~~\n\n#### 힌트
~~~\n#### 예제 입력 1\n  \n#### 예제 입력 1\n
\n\n~~~  \n~~~\n
\n+(출처|보기|메모|링크)$  \n\n#### $1
\n+비슷한 문제  \n\n#### 비슷한 문제
\n+알고리즘 분류 * \n\n#### 알고리즘 분류
\n+(문제를 번역한 사람|문제의 오타를 찾은 사람|잘못된 조건을 찾은 사람)  \n-$1
\n+(문제를 만든 사람|데이터를 추가한 사람|잘못된 데이터를 찾은 사람|데이터를 만든 사람)  \n-$1

^[ \t]+\n  \n
\n+## +  \n\n\n\n##
\n+### +  \n\n\n###
\n\n\n####   \n\n####

^(#### 예제 )\n~~~\n  $1\n~~~ `
~~~





### 1000	A+B	성공 원문 풀이 분류	39398	114121	47.370%




### 1001	A-B	성공 풀이 분류	32549	52383	71.890%




### 1002	터렛	풀이 분류	5125	41340	18.099%

문제
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.



이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 구성되어있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.

출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

예제 입력 1
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
예제 출력 1
2
1
0
힌트
출처
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: baemin0103 koyh1200
알고리즘 분류
기하 알고리즘
메모


#### 풀이

```c++
// [[c++]]

#include <cstdio>

#include <cstdio>

int main() {
  int T;
  int x1, y1, r1, x2, y2, r2;  // 입력값 좌표, 거리
  int n=0, dp=0, rp=0, rp_=0;  // n: 가능한 위치 수, dp: p1-p2 거리의 제곱, rp: 거리합의 제곱 (r1+r2)*(r1+r2), rp2: 거리차의 제곱!!! (r1-r2)*(r1-r2)
  scanf("%d", &T);

  for(int i=0; i<T; i++) {
    scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

    dp = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
    rp = (r1+r2)*(r1+r2);
    rp_ = (r1-r2)*(r1-r2);

    //printf("%d %d %d %d %d %d dp: %d R1: %d R2: %d \n", x1, y1, r1, x2, y2, r2, dp, r1*r1, r2*r2);

    if(x1 == x2 && y1 == y2) { // 같은 위치에 있는 경우(p1 = p2)
      if(r1 == r2) {  // 같은 거리에 있는 경우
        n = -1;
      } else {  // 다른 거리에 있는 경우(가능하지 않음, invalid data)
        n = 0;
      }
    } else { // 다른 위치에 있는 경우(d vs r1+r2)
      if (dp == rp || dp == rp_) {  // d = r1+r2
        n = 1;
      } else if (dp < rp && dp > rp_) {  // d < r1+r2 && d > |r1-r2|
        n = 2;
      } else {  // d > r1+r2
        n = 0;
      }
    }

    printf("%d\n", n); // 출력
  }

  return 0;
}
```


### 1003	피보나치 함수	풀이 분류	5857	40996	32.566%

문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

```c++
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
```

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
다이나믹 프로그래밍
메모


#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1004	어린 왕자	풀이	3207	10678	39.277%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1005	ACM Craft	풀이 분류	1730	20361	18.064%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1006	습격자 초라기	분류	279	4391	13.557%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1007	Vector Matching	스페셜 저지 풀이	374	1851	35.217%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1008	A/B	성공 스페셜 저지 풀이 분류	16654	66604	35.150%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1009	분산처리	풀이	4175	20465	26.158%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1010	다리 놓기	풀이 분류	4452	12932	44.667%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1011	Fly me to the Alpha Centauri	성공 풀이	2238	11627	26.694%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1012	유기농 배추	풀이 분류	4274	18562	32.701%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1013	Contact		550	2296	31.774%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1014	컨닝	출처 원문 풀이 분류	371	2427	36.089%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1015	수열 정렬	스페셜 저지 출처 풀이 분류	1082	3200	45.065%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1016	제곱 ㄴㄴ 수	출처 풀이 분류	1124	12407	18.609%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1017	소수 쌍	출처 풀이 분류	424	3372	17.928%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1018	체스판 다시 칠하기	출처 분류	1277	4610	36.351%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1019	책 페이지	출처 분류	493	3125	37.096%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1020	디지털 카운터	출처 풀이 분류	105	1109	23.864%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1021	회전하는 큐	출처 풀이 분류	1781	6606	34.657%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1022	소용돌이 예쁘게 출력하기	출처 풀이 분류	430	1941	33.568%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1023	괄호 문자열	출처 풀이 분류	124	787	28.118%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1024	수열의 합	출처 풀이 분류	886	5035	25.178%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1025	제곱수 찾기	출처 분류	89	427	28.526%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1026	보물	출처 풀이 분류	5072	10386	60.976%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1027	고층 건물	출처 풀이 분류	307	1554	28.139%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1028	다이아몬드 광산	출처 풀이 분류	272	1677	26.485%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1029	그림 교환	출처 풀이 분류	171	1071	21.701%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1030	프렉탈 평면	출처 분류	90	348	44.118%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1031	스타 대결	출처 분류	90	1058	15.050%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1032	명령 프롬프트	풀이 분류	3198	8824	45.381%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1033	칵테일	분류	72	461	25.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1034	램프	분류	106	440	41.245%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1035	조각 움직이기	분류	73	310	45.062%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1036	36진수	풀이 분류	75	1003	13.661%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1037	약수	분류	3381	8813	46.455%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1038	감소하는 수	풀이 분류	803	3969	29.158%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1039	교환	분류	170	1755	16.716%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1040	정수	분류	36	369	25.532%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1041	주사위	풀이 분류	213	1153	23.381%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1042	움	분류	22	126	35.484%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1043	거짓말	분류	154	837	30.986%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1044	팀 선발	분류	50	604	14.286%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1045	도로	분류	31	175	23.308%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1046	그림자	스페셜 저지 분류	19	142	38.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1047	울타리	분류	33	171	37.500%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1048	유니콘	분류	28	128	35.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1049	기타줄	분류	1079	4440	29.545%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1050	물약	분류	20	395	10.363%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1051	숫자 정사각형	풀이 분류	1203	4111	36.279%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1052	물병	분류	183	737	33.092%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1053	팰린드롬 공장	분류	93	391	33.574%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1054	팰린드롬 문장	분류	19	98	34.545%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1055	끝이없음	풀이 분류	26	296	20.968%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1056	수	분류	34	351	16.749%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1057	토너먼트	풀이 분류	2052	4913	53.901%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1058	친구	풀이 분류	400	1367	37.879%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1059	수2	분류	213	828	32.820%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1060	구간	분류	21	112	24.419%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1061	삼각형	분류	13	96	19.118%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1062	가르침	풀이 분류	374	2802	22.209%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1063	킹	분류	470	1992	29.616%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1064	평행사변형	스페셜 저지 분류	173	891	27.680%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1065	한수	성공 풀이 분류	6064	15469	45.738%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1066	에이한수	분류	16	57	69.565%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1067	이동	분류	93	639	37.805%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1068	트리	풀이 분류	1079	5711	26.240%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1069	집으로	스페셜 저지 풀이 분류	113	1131	17.069%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1070	김지민의 침략	풀이 분류	15	58	60.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1071	소트	풀이 분류	37	419	21.264%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1072	게임	풀이 분류	564	4984	17.865%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1073	도미노	분류	30	84	50.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1074	Z	풀이 분류	1561	5864	42.522%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1075	나누기	분류	1811	3967	54.829%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1076	저항	분류	2502	7624	39.272%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1077	넓이	스페셜 저지 분류	18	130	19.780%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1078	뒤집음	풀이 분류	16	267	14.815%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1079	마피아	분류	48	522	13.675%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1080	행렬	풀이 분류	678	1826	44.635%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1081	합	분류	176	1209	36.289%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1082	방 번호	분류	56	391	24.138%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1083	소트	풀이 분류	104	638	28.809%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1084	방 번호 2	분류	17	299	11.409%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1085	직사각형에서 탈출	풀이 분류	4002	8504	54.538%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1086	박성원	풀이 분류	157	969	26.701%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1087	쥐 잡기	스페셜 저지 풀이 분류	42	247	22.340%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1088	케이크	스페셜 저지 풀이 분류	29	357	22.835%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1089	엘리베이터	스페셜 저지 풀이 분류	70	494	21.472%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1090	체커	분류	21	123	63.636%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1091	카드 섞기	분류	22	239	31.429%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1092	배	분류	232	1171	29.109%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1093	스티커 수집	분류	17	107	26.154%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1094	막대기	분류	3188	5252	72.045%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1095	마법의 구슬	분류	36	260	21.687%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1096	종이 접기	분류	17	122	34.000%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1097	마법의 단어	분류	34	115	36.170%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1098	쌍둥이 마을	분류	14	121	26.923%




#### 풀이

```c++
// [[c++]]

#include <cstdio>

int main() {


  return 0;
}
```


### 1099	알 수 없는 문장	분류	143	1101	23.953%
