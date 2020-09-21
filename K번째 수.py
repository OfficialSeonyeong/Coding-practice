def solution(array, commands):
    answer = []
    for n in commands:
        list1 = array[n[0]-1:n[1]]
        list1.sort()
        answer.append(list1[n[2]-1])
    return answer