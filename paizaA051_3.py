# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
HW = [ int(s) for s in input().split(' ')]
H = HW[0]
W = HW[1]
# print(HW)
S = []
for i in range(H):
    S.append([ int(s) for s in input().split(' ')])
# print(S)

route = [[int(i)] for i in range(W)]
# print(route)

def newRouteMake(rt,w,h):
    newRt=[]
    for r in rt:
        rLast = r[-1]
        # print(rLast)
        if rLast>0:
            r2=r.copy()
            r2.append(rLast-1)
            newRt.append(r2)
        r1 = r.copy()
        r1.append(rLast)
        newRt.append(r1)
        if rLast<w-1:
            r3 = r.copy()
            r3.append(rLast+1)
            newRt.append(r3)
    if len(r1)==h: 
        return newRt
    else:
        return newRouteMake(newRt,w,h)
    
route = newRouteMake(route,W,H)
# print(route)

maxScore = 0
for r in route:
    score=0
    for i in range(len(r)):
        score+=S[i][r[i]]
    # print(score,r)
    if score > maxScore:
        maxScore = score


print(maxScore)

