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