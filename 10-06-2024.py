# numList=[1,6,3,89,4,7,0]
# for i in numList:
#     numList.remove(i)
# print(numList)

# for i in range(6):
#     print(i)
#     i+=2

'''121 leetcode'''
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         mimPrice, maxProfit = 99999,0
#         for amt in prices:
#             if amt < minPrice:
#                 minPrice = amt
#             elif amt - minPrice > maxProfit:
#                 maxProfit = amt - minPrice
#         return maxProfit

'''sum of all the elements in array using recursion'''
# def recursive_sum(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + recursive_sum(arr[1:])
# numList = [15, 3, 6, 12, 8, 5]
# total = recursive_sum(numList)
# print(total)

#2
# numList=[15, 3, 6, 12, 8, 5]
# def totalSum(i):
#     if i>=len(numList):
#         return 0
#     return numList[i]+totalSum(i+1)
# print(totalSum(0))

'''palindrome of a number or not using recursion'''
# def is_palindrome(n):
#   if n < 0:
#     return False
#   num_str = str(n)
#   if num_str == num_str[::-1]:
#     return True
#   else:
#     return False
# number = 12210
# if is_palindrome(number):
#   print("True")
# else:
#   print("False")

# 2
# def palindrome(data):
#     if len(data)==0:
#         return True
#     elif data[0]==data[-1]:
#         return palindrome(data[1:-1])
#     return False
# data=input()
# print(palindrome(data))

'''display the largest palindrome from the given number'''
# data=input()
# def largestPal():
#   maxLen=0
#   larPal=''
#   for i in range(len(data)):
#     for j in range(i+1,len(data)+1):
#       subStr=data[i:j]
#       if isPalindrome(subStr):
#         if len(subStr)>maxLen:
#           maxLen=len(subStr)
#           larPal=subStr
#   return larPal
# print(largestPal())

'''1512 leetcode'''
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         [1,2,3,1,1,3]
#         counter = 0
#         pairs = {}
#         for num in nums:
#             if num not in pairs:
#                 pairs[num] = 1
#             else:
#                 counter += pairs[num]
#                 pairs[num] += 1
#         return counter

'''prime number or not using recursion'''
# num=int(input())
# def isPrime(deno=2):
#     if num<2:
#         return False
#     if deno==int(num**0.5)+1:
#         return True
#     if num % deno==0:
#         return False
#     return isPrime(deno+1)
# print(isPrime())

'''check whether a number can be represented as a sum of two prime numbers'''
'''12, 7, 5, 9 ->2+7'''
# num=int(input())
# primelist=[i for i in range(2,num+1) if is_prime(i)]
# flag=False
# for i in range(len(primelist)):
#     for ele in primelist[i::-1]:
#         if sum(primelist[i],ele)==num:
#             flag=True
#             break
# if flag:
#     print('yes')
# else:
#     print('no')

'''find the highest factor of a number with recursion'''
'''find gcd of two numbers with recursion'''
'''check whether 2 numbers are co-primes or not with recursion'''

'''Problem Statement No. 12
Constraints:-
N <10^9
Example 1
Input:-
20
Output:
3
Explanation
N=20
If we list the numbers that divide 20, they are 1, 2, 4, 5, 10, 20
1 is not a square free number, 4 is a perfect square, and 20 is divisible by 4, a perfect
square. 2 and 5, being prime, are square free, and 10 is divisible by 1,2,5 and 10, none
of which are perfect squares. Hence the square free numbers that divide 20 are 2, 5, 10.
Hence the result is 3'''
