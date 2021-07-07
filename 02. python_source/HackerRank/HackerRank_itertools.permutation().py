from itertools import permutations

word, k = input().split()
k = int(k)
lst = list(permutations(word, k))
lst.sort()

for w in lst:
  print(''.join(w))