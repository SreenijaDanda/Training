'''Raj is a great programmer he works in multinational company. he has been working for past
2.5 years and is expecting a hike in salary. So, his manager gave him a task and a
stipulation that if he completes the code within 1 day he will get hike in salary.
Help Raj in the task to get salary hike using stacks.
[HINT-Raj is good with strings and reversal techniques)
Input Format
The input contains a string.
Output Format
Print it is a palindrome if the string is a palindrome,else print it is not a palindrome
i/p:MADAM O/P:it is a palindrome'''
# def is_palindrome(s):
#     stack = []
#     for char in s:
#         stack.append(char)
#     reversed_s = ""
#     while stack:
#         reversed_s += stack.pop()
#     return s == reversed_s
# string =input()
# if is_palindrome(string):
#     print(f'"{string}" is a palindrome.')
# else:
#     print(f'"{string}" is not a palindrome.')

'''2'''
# strData=input()
# stack=list(strData)
# print(stack)
# for i in strData:
#     if stack.pop()!=i:
#         print("not palindrome")
#         break
# else:
#     print('palindrome')

'''leetcode
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine
if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false'''

# class Solution:
#     def isValid(self,s:str)->bool:
#         stack=[]
#         for i in s:
#             if i=='(':
#                 stack.append(')')
#             elif i=='{':
#                 stack.append('}')
#             elif i=='[':
#                 stack.append(']')
#             elif not stack or stack.pop() !=i:
#                 return False
#         return not stack

'''codeforce
DevG likes too much fun to do with numbers. Once his friend Arya came and gave him a
challenge, he gave DevG an array of digits which is forming a number currently
(will be called as given number). DevG was challanged to find the just next greater number
which can be formed using digits of given number. Now DevG needs your help to find that just
next greater number and win the challenge.

Input
The first line have t number of test cases (1 <= t <= 100). In next 2*t lines for each test
case first there is number n (1 <= n <= 1000000) which denotes the number of digits in given
number and next line contains n digits of given number separated by space.

Output
Print the just next greater number if possible else print -1 in one line foreach test case'''
# t=int(input())
# for i in range(t):
#     n=int(input())
#     numList=list(map(int,input().split()))
#     for i in range(n-1,-1,-1):
#         if numList[i]>numList[i-1]:
#             numList[i],numList[i-1]=numList[i-1],numList[i]
#             index=i
#             break
#     res=[str(ele) for ele in (numList[:index]+(numList[index:])[::-1])]
#     print(''.join(res))

'''682.baseball '''
# class Solution:
#     def calPoints(self,operations:List[str])->int:
#         resStack=[]
#         for i in operations:
#             if i not i.isdecimal():
#                 match1:
#                     case 'D':resStack.append(2*resStack[-1])
#                     case '+':resStack.append(resStack[-1]+resStack[-2])
#                     case 'C':resStack.pop()
#             else:
#                 resStack.append(int(i))
#         return sum(resStack)
# s=

'''plug-in codeforce'''
# dStr=input()
# stack=[]
# for i in dStr:
#     if stack and stack[-1]==i:
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))

'''STPAR - Street Parade'''
# n=int(input())
# trucks=list(map(int,input().split()))
# side=[]
# result=[]
# for i in range(0,len(trucks)-1):
#     if trucks[i]>trucks[i+1]:
#         side.append(trucks[i])
#     else:
#         result.insert(0,trucks[i])
# result.insert(0,trucks[-1])
# result=side+result
# if sorted(trucks,reverse=True)==result:
#     print("yes")
# else:
#     print("No")