# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# import time
# clock = time.time()
#prepare Initial Conditional Parameter
HW = [ int(s) for s in input().split(' ')]
H = HW[0]
W = HW[1]
# print(HW)
S = []
for i in range(H):
    S.append([ int(s) for s in input().split(' ')])
# print(S)

#saiki yobidashi
def newRouteMake(rt,w,h):
    newRt=[]
    for r in rt:
        rLast = r[-1]
        # print(rLast)
        if rLast>0:
            rTemp=r.copy()
            rTemp.append(rLast-1)
            newRt.append(rTemp)
        rTemp = r.copy()
        rTemp.append(rLast)
        newRt.append(rTemp)
        if rLast<w-1:
            rTemp = r.copy()
            rTemp.append(rLast+1)
            newRt.append(rTemp)
    if len(rTemp)==h: 
        return newRt
    else:
        return newRouteMake(newRt,w,h)

#make route    
route = [[int(i)] for i in range(W)]
route = newRouteMake(route,W,H)
# print(route)

#calc Score
maxScore = 0
for r in route:
    score=0
    for i in range(len(r)):
        score+=S[i][r[i]]
    # print(score,r)
    if score > maxScore:
        maxScore = score
print(maxScore)
# print(time.time()-clock)

