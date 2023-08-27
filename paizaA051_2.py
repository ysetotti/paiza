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
# print(S)

N = W**H
# print(N)
maxScore = 0
for n in range(N):
    score = 0
    # route = np.zeros((H,W),dtype=int)
    # routeInVarid=0
    digit =1
    for i in range(H):
        p = int(n/digit)%W
        if digit>=W:
            q = int(n/digitOld)%W
            if(abs(p-q))>1:
                # print("out")
                score = 0
                # routeInVarid=1
                break
        # route[H-i-1,p]=S[H-i-1][p]
        score +=S[H-i-1][p]
        # route[H-i-1,p]=1
        digitOld =digit
        digit *=W
    # if routeInVarid==1:
    #     print(str(n)+"NG")
    # if routeInVarid<1:
    #     print(str(n)+"OK")
        # score = route*S
        # print(score)
        # score = sum((route*S).reshape(H*W))
    if maxScore < score:
        maxScore = score
    # print(score)
        # print(sum(sum(score)))
    # print(route)
print(maxScore)

