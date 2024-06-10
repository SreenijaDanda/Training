'''fib using recursion'''
# def fibonacci(n):
#     if n <= 0:
#         print("incorrect input")
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(int(input())))

# fibVal=[0,1]
# def fib(n):
#     if n<0:
#         print("incorrect number")
#     elif n<len(fibVal):
#         return fibVal[n]
#     fibVal.append(fib(n-1)+fib(n-2))
#     return fibVal[n]
# print(fib(int(input())))

'''Problem Statement No. 08:
kth Largest factor of N
Problem Description
Question A positive integer d is said to be a factor of another positive Integer N if
when N is divided by d, the remainder obtained is zero. For example, for number 12,
there are 6 factors 1, 2, 3, 4, 6, 12. Every positive integer k has at least two factors,
1 and the number k itself. Given two positive integers N and k, write a program to print
the kth largest factor of N.
Input Format: The input is a comma-separated list of positive integer pairs (N, k).
Output Format: The kth highest factor of N. If N does not have k factors, the output
should be 1
Constraints:
1<k<600.
You can assume that N will have no prime factors which are larger than 13.
Example 1
Input: 12,3
Output: 4
Explanation: N is 12, k is 3. The factors of 12 are (1,2,3,4,6,12). The highest factor
is 12 and the third-largest factor is 4. The output must be 4.
Example 2
Input: 30,9
Output 1
Explanation: N is 30, k is 9. The factors of 30 are (1,2,3,5,6,10,15,30). There are only
8 factors. As k is more than the
number of factors, the output is 1.'''
# N,k=map(int,input().split())
# for deno in range(N,0,-1):
#     if N % deno==0:
#         k-=1
#     if k == 0:
#         print(deno)
#         break
# if k != 0:
#     print('1')
        
# def kFactor(N,k,):
#     if deno<=0:
#         return k
#     if N % deno == 0:
#         k -='1'
#     if k == 0:
#         print(deno)
#         return k 
#     return kFactor(N,k,deno-1)
#     
# if __name__ =='__main__':
#     N,k=map(int,input().split())
#     res = kFactor(N,k,N)
#     if k>0:
#         print('1')

'''[12, 3.45, 56, 8.90,7]->true oddindex->float,evenindex->int)
[0.0, 6, 7, 8.9, 60, 9.9]->false'''
# numList=list(input().split())
# for i in range(len(numList)):
#     #if '.' not in str(ele):
#     #if ele % != ele:
#     if i % 2 == 0:
#         if '.' in str(numList[i]):
#             print('False')
#             break
#     else:
#         #if numList[i].is integer() == 'int':
#         if '.' not in str(numList[i]):
#             print('False')
#             break
# else:
#     print('True')

'''leetcode 62.unique paths'''
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         orows=[1]*n
#         for i in range(m-1):
#             nrows=[1]*n
#             for j in range(n-2,-1,-1):
#                 nrows[j]=nrows[j+1]+orows[j]
#             orows=nrows
#         return orows[0]

'''Mani is given an n-by-n matrix of O's and 1's where all 1's in each row come before
all O's, his task is to find the most efficient way to return the row with the maximum
number of O's.
Input:
First line of input contains a single integer T which denotes the number of test cases.
First line of each test case contains a single integer N which represents a size of
matrix and next matrix elements.
Output:
Example:
For each test case, print the row number
Input:
1
((1,1,1,1), (1,1,0,0), (1,0,0,0), (1,1,0,0));
Output: 2'''
# for i in range(int(input())):
#     nestList=list(map(int,input().split()))
#     n=len(nestList)
#     nestList=[nestList]
#     for i in range(n-1):
#         nestList.append(list(map(int,input().split())))
#     mcount=0
#     for i in range(n):
#         if mcount<nestList[i].count(0):
#             mcount=nestList[i].count(0)
#             index=i
#     print(index)

'''2390 leetcode'''
# class Solution:
#   def removeStars(self, s: str) -> str:
#     ans = []
#     for a in s:
#       if a == '*':
#         ans.pop()
#       else:
#         ans.append(a)
#     return ''.join(ans)

'''151 leetcode'''
# class Solution:
#   def reverseWords(self, s: str) -> str:
#     return ' '.join(reversed(s.split()))

'''1046 leetcode'''
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones) > 1:
#             stones.sort()
#             chk = abs(stones.pop() - stones.pop())
#             if chk != 0:
#                 stones.append(chk)
#         return stones[0]

'''1832 leetcode'''
# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:2
#         return len(set(list(sentence))) == 26

'''171 leetcode'''
# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         col_num = 0
#         for char in columnTitle:
#             col_num = col_num * 26 + (ord(char) - 64)
#         return col_num

'''1207 leetcode'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in set(srr):
            d[i] = arr.count(i)
        if len(d.values()) == len(set(d.values()))
            return True
        else:
            False

