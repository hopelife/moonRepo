N = int(input())  # 입력 문자열 개수
c = '0'  # 이전 문자(for 동일 문자인지 비교)
a = [0]*26  # a[0]: 'a'가 있는지 확인(0: 없음, 1: 있음)
M = ord('a')  # 'a' 아스키 코드 값
cnt = 0  # 그룹 단어 개수

for i in range(N) :
  s = input()
  cnt += 1  # 그룹단어로 가정
  for j in range(len(s)) :
    if a[ord(s[j]) - M] == 0 :
      a[ord(s[j]) - M] = 1
      c = s[j]
    else :
      if s[j] == s[j-1] :
        continue
      else :
        cnt -= 1  # 그룹단어가 아니면 -1
        break;
  for k in range(26) :
    a[k] = 0

print(cnt)  # 출력: 그룹 단어 개수
