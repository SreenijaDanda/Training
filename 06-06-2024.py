'''leetcode 210'''
# def findorder(self,numcourses: int, prerequisites: List[List[int]])->List[int]:
#     dmap=defaultdict(list)
#     inD={1:0 for i in range(0,numcourse)}
#     for val in prerequisites:
#         dmap[val[1]].append(val[0])
#         inD[val[0]]+=1
#     flag=True
#     res=[]
#     while(flag):
#         flag=False
#         for key in inD.keys():
#             if inD[key]==0:
#                 flag=True
#                 res.append(key)
#                 for val in dmap[key]:
#                     inD[val]-=1
#                 inD[key]=-1
#     for key in inD.keys():
#         if inD[key]>0:
#             return[]
#     return res

'''1971 leetcode'''
# tcase=int(input())
# for i in range(tcase):
#     n=int(input())
#     bot=list(input())
#     george=list(input())
#     counter=0
#     for i in range(n):
#         if george[i]=='0':
#             continue
#         if i>0 and bot[i-1]=='1':
#             george[i-1]='x'
#             counter+=1
#         elif bot[i]=='0':
#             bot[i]=='x'
#             counter+=1
#         elif i+1<n and bot[i+1]=='1':
#             bot[i+1]='x'
#             counter+=1
#     print(counter)

'''codeforce 1797A'''
# tcase=int(input())
# for i in range(tcase):
#     n,m=map(int,input().split())
#     x1,y1,x2,y2=map(int,input().split())
#     a=4-(x1==1 or x1==n)-(y2==1 or y1==m)
#     b=4-(x2==1 or x2==n)-(y2==1 or y2==m)
#     if a<b:
#         print(a)
#     else:
#         print(b)

'''ARRAY MANIPUATION
Problem Statement No. 07:
Explanation for sample input-output 1:
4 boxes, each containing 1, 2, 3 and 4 candies respectively Adding 1+2 in a new box
takes 3 seconds. Adding 3+3 in a new box takes 6 seconds. Adding 4+ 6 in a new box takes
10. seconds. Hence total time taken is 19 seconds. There could be other combinations
also, but overall time does not go below 19 seconds.
Explanation for sample input-output 2.
5 boxes, each containing 1, 2, 3, 4 and 5 candies respectively Adding 1+2 in a new box
takes 3 seconds Adding 3+3 in a new box takes 6 seconds. Adding 4+6 in a new box takes
10 seconds. Adding 5+10 in a new box takes 15 seconds. Hence total time taken is 34
seconds. There could be other combinations also, but overall time does not go below 33
seconds.'''
for i in range(int(input())):
    N=int(input())
    containers=list(map(int,input().split()))
    totSum=containers[0]
    totTime=0
    for i in containers[1:]:
        totSum+=i
        totTime+=totSum
    print(totTime)