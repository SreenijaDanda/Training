'''Zayn purchased an array A having N Integer values. After playing it for a while, he was
bored of it and decided to update value of its element. In one second he can Increase value
of each array element by 1. He wants each array element's value to become greater than or
equal to K. Please help Zayn to find out the minimum amount of time it will take, for him to
do so.
Input:
First line consists of a single integer, T, denoting the number of test cases.
First line of each test case consists of two space separated integers denoting Nand K.
Second line of each test case consists of N space separated integers denoting the array A.
Output:
For each test case, print the minimum time in which all array elements will become greater
than or equal to K. Print a new line after each test case.'''
# t=int(input())
# for t in range(t):
#     n,k=list(map(int,input().split()))
#     array=list(map(int,input().split()))
#     print(k-min(array))

'''Sandhir was into aviation industry and she was trying to check with some tale off rules.
There are three planes A, B and C. Plane A will takeoff on every pth day Le. p. 2p, 3p and
so on. Plane B will takeoff on every ath day and plane C will takeoff on every rth day.
There is only one runway and the takeoff timing is same for each of the three planes on each
day. Now her task is to find out the maximum number of flights that will successfully takeoff
in the period of N days.
Note: If there is collision between the flights no flight will take off on that day
Input
1 10247
Input Format
The first line of the input contains a single Integer T, the number of test cases
Then T lines follow each containing four space-separated integers N, p, q and as denoted in
the statement.
Output Format
For each test case print a single integer representing the maximum number of flights that
will successfully takeoff in the period of N days'''
# t=int(input())
# tsum=0
# for i in range(t):
#     days,p,q,r=list(map(int,input().split()))
#     for i in range(1,days+1):
#         a=i%p
#         b=i%q
#         c=i%r
#         if a==0 or b==0 or c==0:
#             if a==0 or b==0:
#                 continue
#             elif a==0 and c==0:
#                 continue
#             elif b==0 and c==0:
#                 continue
#             tsum+=1
#     print(tsum)

'''leetcode 232''' 
# class MyQueue:
# 
#     def _init_(self):
#         self.queue=[]
#         
# 
#     def push(self, x: int) -> None:
#         self.queue.append(x)
# 
#     def pop(self) -> int:
#         return self.queue.pop(0)
#     def peek(self) -> int:
#         return self.queue[0]
#         
# 
#     def empty(self) -> bool:
#         return self.queue==[]
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''933 leetcode'''
# class RecentCounter:
# 
#     def _init_(self):
#         self.request = collections.deque()
#         
# 
#     def ping(self, t: int) -> int:
#         while self.request and t-self.request[0]>3000:
#             self.request.popleft()
#         self.request.append(t)
#         return len(self.request)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)