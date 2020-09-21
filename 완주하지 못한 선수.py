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


# 또 다른 풀이
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