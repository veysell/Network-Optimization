
##############  KRUSKAL #############
#region Kruskal
# def takeSecond(elem):
#     return elem[1]
# #the method doing make circle control
# def isCircle(Ln):
#         if Ln is None:
#             return True
#         else:
#             nodes[Ln[0][0]]+=1
#             nodes[Ln[0][1]]+=1
#             if nodes[Ln[0][0]]<max_node_count and nodes[Ln[0][1]]<max_node_count:
#                 return True
#             else:
#                 nodes[Ln[0][0]]-=1
#                 nodes[Ln[0][1]]-=1
#                 return False

# ways=[("AB",2),("AC",5),("AD",4),("BC",6),("BE",7),("CE",4),("CF",3),("CD",1),
# ("DF",4),("EF",1),("EG",5),("FG",7)]
# nodes={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0}
# max_node_count=int(len(nodes)/2)
# route=[]
# def kruskal_sort(list):
#     L=[]
#     list.sort(key=takeSecond)
#     for i in list:
#         if(isCircle(i)):
#             L.append(i)
#         if(len(nodes)-1==len(L)):
#             break
#     for i in L:
#         route.append(i[0])
#     print(L)

#kruskal_sort(ways)
#endregion

##############  PRIM    #############
#region PRIM
# dict={
#     "A":[("B",2),("C",5),("D",4)],
#     "B":[("A",2),("C",6),("E",7)],
#     "C":[("A",5),("B",6),("E",4),("D",1),("F",3)],
#     "D":[("A",4),("C",1),("F",4)],
#     "E":[("B",7),("C",4),("F",1),("G",5)],
#     "F":[("D",4),("C",3),("E",1),("G",7)],
#     "G":[("E",5),("F",7)]
# }

# Ck=[]
# Co=["A","B","C","D","E","F","G"]
# weight=[]

# while len(Co)>0:
#     if len(Ck)==0:
#         Ck.append(Co[0])
#         search_min=dict[Co[0]]
#         x=min(search_min,key=lambda search_min: search_min[1])
#         #circle control
#         Ck.append(x[0])
#         Co.remove(Co[0])
#         Co.remove(x[0])
#     else:
#         for i in Ck:
#             values=dict[i]
#             x=sorted(values,key=lambda values: values[1])
#             for j in x:
#                 if j[0] not in Ck:
#                     Ck.append(j[0])
#                     Co.remove(j[0])
#                     break
#                 else:
#                     continue
# print(Ck)

#endregion

##############  DIJKSTRA    #############
#region Dijkstra
import math
from matplotlib import pyplot as plt
import numpy as np
dict={
    "1":[("2",5),("3",7)],
    "2":[("4",3),("5",6)],
    "3":[("4",4),("5",5)],
    "4":[("6",2)],
    "5":[("7",4)],
    "6":[("7",2)],
    "7":[]
}
inf=math.inf
nodes=["1","2","3","4","5","6","7"]
marker=[0,inf,inf,inf,inf,inf,inf]
way=['1']
def get_min(val):
    minValue=inf
    minKey=""
    for j in dict[val]:
        if(j[1]<minValue):
            minValue=j[1]
            minKey=j[0]
    if(minKey!=""):
        way.append(minKey)
        get_min(minKey)
            
    
for i in nodes:
    a=((dict[i]))
    for j in range(len(a)):
        b=a[j]
        index=nodes.index(b[0])
        index2=nodes.index(i)
        result=min((b[1]+marker[index2]),marker[index])
        marker[index]=result 

get_min(nodes[0])

print("Yol Guzergahi ve Mesafe")
for i in way:
    print(i,end=' --> ')
print(marker[-1]*100," km")
#endregion      
    
    

       
