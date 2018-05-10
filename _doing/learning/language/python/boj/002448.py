# -*- coding: utf-8 -*-

import math
s = ['  *   ', ' * *  ', '***** ']  # 기본 삼각형


def make_stars(shift):  # http://lazineer.tistory.com/179
  for i in range(len(s)):
    s.append(s[i] + s[i])  # 현 단계 삼각형 2개를 뒤에 붙이고
    s[i] = ' '*shift + s[i] + ' '*shift  # 현 단계 삼각형을 오른쪽으로 민다

N = int(input())  # 입력 값(출력 줄 수) N = 3 × 2^k

k = int(math.log(N/3, 2))

for i in range(k):
  make_stars(2**i*3)

for i in range(len(s)):  # 출력
  print(s[i])

