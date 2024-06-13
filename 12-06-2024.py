'''Problem Statement:Bhojon is a restaurant company and has started a new wing in a city. They have every type of cook except the meatball
artist. They had fired their last cook because the sale of meatballs in their restaurant is really great, and they can't afford to malie
meatballs again and again every time their stock gets empty. They have arranged a hining program, where you can apply with their meatball.
They will add the meatball in their seekh (a queue) and everytime they cut the meatball they take it and cut it on the day's quantity and
then re-add the meatball in the peels. You are the hiring manager there and you are going to say who is gonna be hired.
Day's quantity means, on that very day the company sells only that kg of meatballs to every pachet
If someone has less than a day's quantity, it will be counted as a sell
Function Description:
Complete the function with the following parameters:
Input Format:
First line contains N.
Second line contains D.
After that N lines contain The ith person's meatball weight
Output Format: The I based index of the man whose meatball is served at the last.
Sample Input:
4
2
[7893]
Sample Output:3
Explanation:
The seekh or meatball queue has [7893] this distribution. At the first serving they will cut 2 kgs of meatball from the first meatball
and add it to the last of the seekh, so after Ist time is [8935]
Then, it is: [9356] [3567] [5671] [6713] [7134], [1345] [345] [451] [512] [123] [23] [3] [1] [0]
So the last served meatball belongs to the 3rd person.'''
# n=int(input())
# d=int(input())
# mbList=list(map(int,input().split()))
# soldqty=[(i-1)//d for i in mbList]
# print(soldqty.index(max(soldqty))+1)

'''Abhijeet is one of those students who tries to get his own money by part time jobs in various places to fill up the expenses for buying
books. He is not placed in one place, so what he does, he tries to allocate how much the book he needs will cost, and then work to earn that much money only. He works and then buys the book respectively. Sometimes he gets more money than he needs so the money is saved for the next book. Sometimes he doesn’t. In that time, if he has stored money from previous books, he can afford it, otherwise he needs money from his parents.
Now His parents go to work and he can’t contact them amid a day. You are his friend, and you have to find how much money minimum he can
borrow from his parents so that he can buy all the books.
He can Buy the book in any order.
Constraints:
1 <= N <= 10^3
1 <= EarnArray[i] <= 10^3
1 <=  CostArray[i] <= 10^3
Input Format:
First line contains N.
Second N lines contain The ith earning for the ith book.
After that N lines contain The cost of the ith book.
Output Format:
The minimum money he needs to cover the total expense.
Sample Input 1:
3
[3 4 2]
[5 3 4]
Sample Output 1:
3
Explanation:
At first he buys the 2nd book, which costs 3 rupees, so he saves 1 rupee. Then he buys the 1st book, that takes 2 rupees more.
So he spends his stored 1 rupee and hence he needs 1 rupee more. Then he buys the last book.'''
# n=int(input())
# elist=list(map(int,input().split()))
# clist=list(map(int,input().split()))
# costing=sum(elist)-sum(clist)
# if costing < 0:
#     print(abs(costing))
# else:
#     print("0")

'''Parallel Columbus prepinsta'''
# import math
# n=int(input())-1
# m=int(input())-1
# x=int(input())-1
# y=int(input())-1
# def validpath():
#     total_path=math.factorial(n+m) // (math.factorial(n) * math.factorial(m))
#     path_to_xy=math.factorial(x+y) // (math.factorial(x) * math.factorial(y))
#     xy_to_mn=math.factorial(n-x+y) // (math.factorial(n-x) * math.factorial(m-y))
#     return total_path-(path_to_xy * xy_to_mn)
# print(validpath())

'''leetcode 605'''
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         size=len(flowerbed)
#         i=0
#         while i<size:
#             if(i==0 or flowerbed[i-1]==0)and(flowerbed[i]==0)and(i==size-1 or flowerbed[i+1]==0):
#                 n=n-1
#                 i+=2
#             else:
#                 i+=1
#         return n<=0

'''leetcode 1217'''
# class Solution:
#     def minCostToMoveChips(self, position: List[int]) -> int:
#         evencount=len([i for i in position if i%2==0])
#         oddcount=len(position)-evencount
#         return min(evencount,oddcount)

'''leetcode 1403'''
