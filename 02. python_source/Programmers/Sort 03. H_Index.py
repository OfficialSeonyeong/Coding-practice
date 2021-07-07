# 2021.07.07

def solution(citations):
    n = len(citations)
    for order in range(0,n+1):
        bigger = [x for x in citations if x >= order]
        if len(bigger) >= order:
            answer = order
    return answer