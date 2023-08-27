# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
AB=[]
lastDay = 0
# N=4
# AB=[[1,2],
# [2,3],
# [5,7],
# [8,15]]
# N=3
# AB=[[1,4],
# [5,6],
# [3,7]]
for i in range(N):
    AB.append([ int(s) for s in input().split(' ')])
    # print(max(AB[-1]))
    endDay = max(AB[-1])
    if lastDay<endDay:
        lastDay = endDay
# print(lastDay)



# print(N)
# print(AB)

kinmuDays=[0 for i in range(lastDay)]

for i in range(N):
    for j in range(AB[i][0],AB[i][1]+1):
        # print(j)
        kinmuDays[j-1]=1
# print(kinmuDays)

lastCounts = []
counter = 0
for i in kinmuDays:
    if i>0:
        counter+=1
    else:
        lastCounts.append(counter)
        counter=0
lastCounts.append(counter)
# print(lastCounts)
print(max(lastCounts))

