def solution(phone_book):
    answer = True
    for i in phone_book :
        for num in phone_book :
            if num != i :
                if num.startswith(i):
                    answer = False
                    break
        if answer == False :
            break
    return answer


# 다른 풀이(2021.07.05)
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        if i < len(phone_book)-1:
            if phone_book[i+1].startswith(phone_book[i]):
                answer = False
                break
    return answer