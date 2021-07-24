import sys

N = int(sys.stdin.readline())
stack = []

def stack_processing(order, stack):
  if order.startswith('push'):
    command, num = order.split()
    stack.append(num)
  if order == 'pop':
    try:
      print(stack.pop())
    except:
      print(-1)
  if order == 'size':
    print(len(stack))
  if order == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  if order == 'top':
    if stack:
      print(stack[-1])
    else:
      print(-1)
  return stack

for _ in range(N):
  order = sys.stdin.readline().rstrip()
  stack = stack_processing(order, stack)