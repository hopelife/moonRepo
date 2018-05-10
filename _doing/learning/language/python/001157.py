# -*- coding: utf-8 -*-
s = input()  # 입력 문자열
a = [0]*26  # a[0]: 'a' 개수, ... a[25]: 'z' 개수
M = ord('a')  # 'a' 아스키 코드 값

for i in range(len(s)) :
	a[ord(s[i]) - M] += 1

#print(a)  #
#print(chr(a.index(max(a)) + M))
