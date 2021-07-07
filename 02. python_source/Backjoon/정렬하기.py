
import sys

n = int(input())

points = []

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    points.append((x,y))

for i in range(len(points)):
    min_key_index = i
    for j in range(i+1, len(points)):
        if points[min_key_index][0] == points[j][0]:
            if points[min_key_index][1] > points[j][1]:
                points[j], points[min_key_index] = points[min_key_index], points[j]
        if points[min_key_index][0] > points[j][0]:
            min_key_index = j
    points[i], points[min_key_index] = points[min_key_index], points[i]

for (x,y) in points:
    print(x, y, sep=' ')
