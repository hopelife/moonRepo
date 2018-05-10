# -*- coding: utf-8 -*-
n = [0]*3  # 입력 : 세 수 A, B, C
a = [0]*10  # a[0]: 0 개수, ... a[9]: 9 개수

for i in range(3) :  # 입력 : 세 수 A, B, C
	n[i] = int(input())

s = str(n[0]*n[1]*n[2])  # A*B*C

for i in range(len(s)) :  # counting
	a[int(s[i])] += 1

for i in range(10) :  # 출력
	print(a[i])
