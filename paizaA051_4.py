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

#Dynamic Program
def dynamicProgram(array,w):
    maxArray = [ ]
    for i in range(w):
        if i==0:
            maxArray.append(max(array[0][0:2]))
            # print(i,array[0][0:2])
        elif i==w-1:
            maxArray.append(max(array[0][w-2:w]))
            # print(i,array[0][w-2:w])
        else:
            maxArray.append(max(array[0][i-1:i+2]))
            # print(i,array[0][i-1:i+2])
    # print(maxArray)
        
    array[1] = [x + y for (x, y) in zip(array[1],maxArray)]
    array.pop(0)
    if len(array)==1:
        return max(array[0])
    else:
        return dynamicProgram(array,w)

print(dynamicProgram(S,W))

