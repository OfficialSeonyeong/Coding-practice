# 2021.07.08

def solution(brown, yellow):
    # 가로 x, 세로 y
    # 2x + 2y -4 = brown
    # x*y - brown = yellow
    answer = []
    for x in range(1,brown):
        if x*(-x+2 +brown/2)==yellow+brown:
            answer.append(x)
    if len(answer) == 1:
        answer = answer*2
    answer.sort(reverse=True)
    return answer