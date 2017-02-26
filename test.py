mList = [0,31,28,31,30,31,30,31,31,30,31,30,31]
wDay = {1 : 'MON', 2 : 'TUE', 3 : 'WED',4 : 'THU',5 : 'FRI',6 : 'SAT',0 : 'SUN'}
sum =0
month, day = map(int, raw_input().split(" "))
 
for i in range(month):
    sum += mList[i]sum += dayprint wDay.get(sum%7)


