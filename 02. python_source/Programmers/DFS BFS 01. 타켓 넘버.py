# 2021.07.07 풀지 못했음

# 완전 탐색

from itertools import product # 모든 경우의 곱셈

def solution(numbers, target):
  l = [(x,-x) for x in numbers]
  s = list(map(sum, product(*l))) # 모든 경우의 덧셈
  return s.count(target)



# DFS

def solution(numbers, target):
  sup = [0]
  for i in numbers:
    sub = []
    for j in sup:
      sub.append(j+i)
      sub.append(j-i)
    sup = sub
  return sup.count(target)