# 2021.07.07

from itertools import permutations
import math

def solution(numbers):
    # 소수 판별 함수
    def is_prime_number(x):
        if x == 1 or x == 0:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
    # 만들 수 있는 숫자 조합 리스트 만들기
    possible_nums = []
    
    for i in range(1, len(numbers)+1):
        for word in list(permutations(numbers, i)):
            number = int(''.join(word))
            possible_nums.append(number)
    
    # 소수 골라내기        
    answers = []
    for num in possible_nums:
        if is_prime_number(num) == True:
            answers.append(num)
            answer = set(answers)
    return len(answer)