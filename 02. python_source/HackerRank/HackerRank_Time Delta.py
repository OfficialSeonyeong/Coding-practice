# 2021.07.08 풀지 못했음

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    answer = int(abs((f.strptime(t1, fmt)-f.strptime(t2, fmt)).total_seconds()))
    return str(answer)