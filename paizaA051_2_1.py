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
    digit =1
    for i in range(H):
        p = int(n/digit)%W
        if digit>=W:
            q = int(n/digitOld)%W
            if(abs(p-q))>1:
                # print("out")
                score = 0
                break
        score +=S[H-i-1][p]
        digitOld =digit
        digit *=W
    if maxScore < score:
        maxScore = score
print(maxScore)

