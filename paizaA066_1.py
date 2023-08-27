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
    newAB = [ int(s) for s in input().split(' ')]
    # print(AB,newAB,len(AB))
    removeCount = 0
    for i in range(len(AB)):
        ABi=AB[i-removeCount]
        incheck0 = (ABi[0] - newAB[0])*(ABi[1] - newAB[0])<0
        incheck1 = (ABi[0] - newAB[1])*(ABi[1] - newAB[1])<0
        contacktCheck0 = (newAB[0]-ABi[1])==1
        contacktCheck1 = (ABi[0] - newAB[1])==1
        # print("incheck"+str([incheck0,incheck1]))
        # print("contactcheck"+str([contacktCheck0,contacktCheck1]))
        if incheck0 or incheck1 or contacktCheck0 or contacktCheck1:
            # print("max="+str(max(ABi[1],newAB[1])))
            # print("min="+str(min(ABi[0],newAB[0])))
            newAB = [min(ABi[0],newAB[0]),max(ABi[1],newAB[1])]
            # AB[i] = newAB
            # removeIndex.append(i)
            AB.pop(i-removeCount)
            removeCount +=1
    # for j in removeIndex:
    #     AB.pop(j)
    AB.append(newAB)

# print(N)
# print(AB)

#calc maxDayLength
maxDayLength = 0
for ab in AB:
    length = ab[1]-ab[0]+1
    if length > maxDayLength:
        maxDayLength = length
print(maxDayLength)


