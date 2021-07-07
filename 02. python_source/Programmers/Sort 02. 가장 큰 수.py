2021.07.05
def solution(numbers):
    n = list(map(str, numbers))
    n.sort(key=lambda x: x*3, reverse=True) # 글자순으로 크기순 정렬
    answer = str(int(''.join(n)))
    return answer