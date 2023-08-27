# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import numpy as np
HW = [ int(s) for s in input().split(' ')]
H = HW[0]
W = HW[1]
# print(HW)
S = []
for i in range(H):
    S.append([ int(s) for s in input().split(' ')])
S = np.array(S)
# print(S)

# route = np.zeros((H,W))
N = W**H
route = np.zeros((N,H,W),dtype = int)
routeInVarid = np.zeros(N,dtype = int)
maxScore = 0
for n in range(N):
    for i in range(H):
        p = int(n/W**i)%W
        # print(p)
        if i-1>=0:
            if(abs(int(n/W**i)%W-int(n/W**(i-1))%W))>1:
                # print("out")
                routeInVarid[n]=1
                break
        route[n,H-i-1,p]=1
    if routeInVarid[n]==0:
    #     print(str(n)+"NG")
    # else:
        # print(str(n)+"OK")

        score = route[n]*S
        # print(score)
        score = sum((route[n]*S).reshape(H*W))
        if maxScore < score:
            maxScore = score
        # print(score)
        # print(sum(sum(score)))
print(maxScore)

