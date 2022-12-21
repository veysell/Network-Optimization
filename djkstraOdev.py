# import math
# from traceback import print_tb
# x=math.inf
# matris=[
#     [x,x,450,154,x,x,x,x,x,x],
#     [x,x,403,x,x,x,x,x,x,x,x],
#     [450,403,x,388,x,319,262,x,x,1001],
#     [154,x,388,x,345,183,x,x,x,x],
#     [x,x,x,345,x,335,x,460,x,x],
#     [x,x,319,183,335,x,x,x,x,x],
#     [x,x,262,x,x,x,x,x,345,x],
#     [x,x,x,x,460,x,x,x,609,x],
#     [x,x,x,x,x,x,345,609,x,523],
#     [x,x,1001,x,x,x,x,x,523,x] 
# ]
# maliyet=[]
# yol=[]


# for i in range(len(matris)):
#     yol.append(0)
#     maliyet.append([0])
# def yolara(index):
#     # if(index==9):
#     #     return
#     # else:
#     #     temp=matris[index][index]
#     #     matris[index][index]=x
#     #     minY=min(matris[index])
#     #     minIndex=matris[index].index(min(matris[index]))
#     #     maliyet.append(minY)
#     #     yol.append(minIndex)
#     #     matris[minIndex][index]=x
#     #     matris[index][index]=temp
#     #     yolara(minIndex)

import math
from matplotlib import pyplot as plt
import numpy as np


x=math.inf
matris=[
    [x,x,450,154,x,x,x,x,x,x],
    [x,x,403,x,x,x,x,x,x,x,x],
    [450,403,x,388,x,319,262,x,x,1001],
    [154,x,388,x,345,183,x,x,x,x],
    [x,x,x,345,x,335,x,460,x,x],
    [x,x,319,183,335,x,x,x,x,x],
    [x,x,262,x,x,x,x,x,345,x],
    [x,x,x,x,460,x,x,x,609,x],
    [x,x,x,x,x,x,345,609,x,523],
    [x,x,1001,x,x,x,x,x,523,x] 
]
maliyet=[]
yol=[]

yol.append(0)
def yolAra(indis):
    if indis==10:
        return
    else:
        minIndis=matris[indis].index(min(matris[indis]))
        print(minIndis)
        i,j = matris[indis],matris[minIndis]
        yol.append(minIndis)
        
        for t in range(len(i)):
            top=i[t]+j[t]
            maliyet.append([top])
        indis=minIndis
        print(maliyet)
    

yolAra(0)