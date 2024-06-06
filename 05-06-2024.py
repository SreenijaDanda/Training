'''codeforce 136A'''
# n=int(input())
# fList=list(map(int,input().split()))
# info={}
# k=1
# for i in fList:
#     info[i-1]=k
#     k+=1
# for i in range(n):
#     print(info[i],end=' ')

'''codeforce 460c'''
# n,m,w=map(int,input().split())
# flower=list(map(int,input().split()))
# minH=min(flower)
# print(minH+abs(m-w))

'''codeforce 266B Queue at the school'''
# n,t=map(int,input().split())
# s=list(input())
# for _ in range(t):
#     i=1
#     while i<len(s):
#         if s[i]=='G' and s[i-1]=='B':
#             s[i]='B'
#             s[i-1]='G'
#             i+=1
#         i+=1
# print(''.join(s))

'''codeforce 336B'''
# m,r=map(int,input().split())
# ans=(m*(m+1)*(m+2)/3-m)*2
# ans+=(2.0**0.5-2)*((m*m-m)+(m*m-m-(m-1)*2))
# ans/=(m**2)
# ans*=r
# print("{:.10f}".format(round(ans,10)))

'''codeforce 337A'''
# n,m=map(int,input().split())
# f=list(map(int,input().split()))
# print(abs(min(f[:n])-max(f[:n])))

'''codeforce 78A haiku'''
data1=input()
data2=input()
data3=input()
vowels=['a','e','i','o','u']
haiku=[5,7,5]
res=[]
for i in (data1,data2,data3):
    count=0
    for c in i:
        if c in vowels:
            count+=1
    res.append(count)
if res==haiku:
    print("yes")
else:
    print("no")