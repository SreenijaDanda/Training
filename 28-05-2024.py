'''check number is prime or not'''
# num=int(input())
#1 o(n)
# count=0
# for deno in range(1,num+1):
#     if num % deno == 0:
#         count += 1
# if count == 2:
#     print("prime")
# else:
#     print("not prime")

#2 o(n), o(n)
# for deno in range(2,num):
#     if num % deno == 0:
#         print("not a prime")
#         break
# else:
#     print("prime")

#3 o(n/2)
# for deno in range(2,(num//2)+1):
#     if num % deno == 0:
#         print("not a prime")
#         break
# else:
#     print("prime")

#4 o(sqrt(n))
# for deno in range(2,int(num**0.5)+1):
#     if num % deno == 0:
#         print("not a prime")
#         break
# else:
#     print("prime")


'''power of 6. given an integer n, return true if it is a power of six.otherwise return false. an integer
n is a power of six, if there exists an integer x such that n==6^x.
input: 36
output: true'''
# num=int(input())
# while num !=1:
#     if num % 6 == 0:
#         num //= 6
#     else:
#         print("false")
#         break
# else:
#     print("true")

'''recursion'''
# def greet(n):
#     if n <= 0:
#         return
#     print("hello")
#     greet(n-1)
# greet(2)

#[5, 4, 3, 2, 1]
# def display(n):
#     if n <= 0:
#         return
#     print(n,end = " ")
#     display(n-1)
# display(5)

# def display(n):
#     if n <= 0:
#         return
#     display(n-1)
#     print(n,end = " ")
# display(5)

'''print the string in reverse order using recursion'''
# def revStr(data):
#     if data == "":
#         return data
#     return data[-1] + revStr(data[:-1])
# strData= "why are you shy"
# print(revStr(strData))

# str1='"fisrt string"\n'
# str2="second string's\n"
# str3=''' they r best """ friends""" '''
# print(str1,str2,str3)

# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)

# import string
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)

'''check if data is a number or not'''
#123-true
#12m4-false
#1ab23-false
# import string
# strNum = input()
# for i in strNum:
#     if i not in string.digits:
#         print("false")
#         break
# else:
#     print("true")

'''generate a number from the given string,if no digit found return 0'''
#123av45b78   ->1234578  ->[int]
# import string
# a=input()
# num=""
# for i in a:
#     if i in string.digits:
#         num+=i
# if num == "":
#     print('0')
# else:
#     print(int(num))

'''replaceing''' 
# str1 = "hungry??"
# print(str1.replace('?','.'))

'''partition'''
# str1 = "hello everyone"
# print(srt1.partition('o'))

'''splitlines'''
# str2 = """hello
# good afternoon
# this is siri"""
# print(str2.splitlines())

'''format'''
# n = input()
# a,b = 5, 8
# print("this",b,"is a",n,"demo",a,"output")
# print("this {2} is {2} a {0} demo {1} output{1}{2}".format(n,a,b))

# str1 = "this is 2020";
# str2 = "2020"
# print(str1.isdigit())
# print(str2.isdigit())

'''write a program to remove all consecutive duplicates from a given string
input: read a string
output: print string after removing all consecutive duplicates'''
# data = input()
# res = data[0]
# k = 0
# for i in range(1,len(data)):
#     if data[i] != res[k]:
#         res += data[i]
#         k += 1
# print(res)

# other
# str1=input()
# new_str1=""
# prev_char = None  
# for char in str1:
#   if char!= prev_char:  
#     new_str1+= char
#   prev_char = char  
# print(f"Original string: {str1}")
# print(f"String without consecutive duplicates: {new_str1}")

'''shortest distance to a charactor'''
# class Solution(object):
#     def shortestToChar(self, s: str, c: str) -> List[int]:
#         appear = [inx for inx in range(len(s)) if s[inx] == c]
#         return[abs(min(appear,key = lambda x: abs(x-i))-1) for i in range(len(s))]

'''Rotate a given String in the specified direction by specified magnitude. After each rotation make noteofthe
first character of the rotated String, After all rotation are performed the accumulated first character as
noted previously will form another string, say FIRSTCHARSTRING. Check If FIRSTCHARSTRING is an Anagram of any
substring of the Original string. If yes print neg YE S^ prime prime otherwise "NO".

Input: The first line contains the original string s. The second line contains a single integer q.
The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.
Constraints: 1 <= Length of original string C = 30
1 <= q <= 10
Output: YES or NO

#2 Input:
carrace
3
L2
R2
L3
Output:NO
Explanation:
After applying all the rotations the FIRSTCHARSTRING string will be "rcr" which is not anagram of any sub
string of original string "carrace".'''
# data=input()
# rot=int(input())
# res=''
# for i in range(rot):
#     di,mag=input().split()
#     if di.upper()=='L':
#         res+=(data[int(mag):]+data[:int(mag)])[0]
#     elif di.upper()=='R':
#         res+=(data[:int(mag)]+data[int(mag):])[0]
# subList=[data[i:i+rot] for i in range(0,len(data)-rot + 1)]
# print(res, subList)
# #Anagram:
# for subele in subList:
#     if sorted(subele)==sorted(res):
#         print("Yes")
#         break
# else:
#     print("No")

'''Anagram'''
# from collections import deque
# data = input()
# qStr=deque(data)
# rot=int(input())
# res = ""
# for i in range(rot):
#     di,mag=input().split()
#     if di == 'l' or di == 'L':
#         qStr.rotate(-int(mag))
#         res += qStr[0]
#     elif di == 'r' or di == 'R':
#         qStr.rotate(int(mag))
#         res += qStr[0]
# subList=[data[i:i+rot] for i in range(0,len(data)-rot + 1)]
# for subele in subList:
#     if sorted(subele)==sorted(res):
#         print("Yes")
#         break
# else:
#     print("No")

'''grom given list make a single word'''
# stringList = ['w','e','l','c','o','m','e']
# res = "*".join(stringList)
# print(res)

