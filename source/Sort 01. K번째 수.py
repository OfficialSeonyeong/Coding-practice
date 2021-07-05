def solution(array, commands):
    answer = []
    for n in commands:
        list1 = array[n[0]-1:n[1]]
        list1.sort()
        answer.append(list1[n[2]-1])
    return answer


# 2021.07.05
def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]-1
        j = command[1]
        k = command[2]-1
        ar = sorted(array[i:j])
        answer.append(ar[k])
    return answer