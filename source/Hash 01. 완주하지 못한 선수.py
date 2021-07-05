# 시간 초과
def solution(participant, completion):
    answer = {}
    for i in participant :
        if i in answer :
            answer[i] += 1
        else :
            answer[i] = 1
    for t in completion :
        if answer[t] == 1 :
            del answer[t]
        else :
            answer[t] -= 1
    real_answer = list(answer.keys())
    return real_answer[0]


# 또 다른 풀이(시간 초과)
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i in completion :
                if participant.count(i) > completion.count(i):
                    answer = i
                else:
                    pass
        else :
            answer = i
    return(answer)


# 시간 효율성 통과(2021.07.05)
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for a,b in zip(participant, completion):
        if a != b:
            answer = a
            break
        else:
            answer = participant[-1]
    return answer