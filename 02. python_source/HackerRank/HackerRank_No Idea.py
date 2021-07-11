# 2021.07.09

# Define m, n.
m,n = map(int, input().split())
# Define array, A, B.
array = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0

for n in array:
  if n in A:
    happiness += 1
  if n in B:
    happiness -= 1
print(happiness)
