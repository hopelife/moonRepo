# -*- coding: utf-8 -*-
N = int(input())

for i in range(N):
  s = input()
  cnt = 0
  sum = 0
  for j in range(len(s)):
    if s[j] == 'O' :
      cnt += 1
      sum += cnt
    else :
    	cnt = 0
  print(sum)
