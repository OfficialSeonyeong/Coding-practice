# 2021.07.06

def solution(answers):
    # 최대 문제 수인 10,000개로 맞추기
    first = [1,2,3,4,5]*2000
    second = [2,1,2,3,2,4,2,5]*1250
    third = [3,3,1,1,2,2,4,4,5,5]*1000
    
    total = [0,0,0]
    
    for one, two, three, ans in zip(first, second, third, answers):
        lst = [one, two, three]
        for i in range(len(lst)):
            if ans == lst[i]:
                total[i] += 1            
            
    answer = [idx+1 for idx in range(len(total)) if total[idx] == max(total)]
    
    return answer