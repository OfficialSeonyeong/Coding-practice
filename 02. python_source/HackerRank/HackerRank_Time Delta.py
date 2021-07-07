# 2021.07.07

from datetime import datetime
t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'

# 시간 차이 계산
first = ' '.join(t1.split()[1:5])
first = datetime.strptime(first, '%d %b %Y %H:%M:%S')

second = ' '.join(t2.split()[1:5])
second = datetime.strptime(second, '%d %b %Y %H:%M:%S')

date_differ = first - second

# 시차 차이 계산
f = int(t1[-5:])
t = int(t2[-5:])
time_differ = f-t
print(time_differ)