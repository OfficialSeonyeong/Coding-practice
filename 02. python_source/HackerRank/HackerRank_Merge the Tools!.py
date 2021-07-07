# 2021.07.06

def merge_the_tools(string, k):
    # your code goes here
    lst = [string[i:i+k] for i in range(0, len(string), k)]
    
    answers = []
    for word in lst:
        temp = []
        for c in word:
            if c in temp:
                pass
            else:
                temp.append(c)
        answers.append(temp)
    for answer in answers:
        print(''.join(answer))
