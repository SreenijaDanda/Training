'''Problem Statement No. 3: Lexi String
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this
list to find the smallest lexicographical string that can be made out of this new order.
Can you help him?
You are given a string P that denotes the new order of letters in the English
dictionary.
You need to print the smallest lexicographic string made from the given string S.
Constraints: 1 <= T <= 1000
Length (P) 261 <= length (S) <= 100
All characters in the string S, P are in lowercase
Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S
Output
Print a single string in a new line for every test case giving the result.
input:
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezxvbintma
ativedoc
o/p:
bdca
codevita'''
# tcase=int(input())
# for i in range(tcase):
#     lexi=input()
#     s=input()
#     for i in range(len(lexi)):
#         c=lexi[i]
#         if c in s:
#             print(c,end='')

'''codeforce sum in binary tree'''
# def totalSum(self,root):
#     if root is None:
#         return 0
#     else:
#         leftSum=totalSum(root.left)
#         rightSum=totalSum(root.right)
#         #return root.data+leftSum+rightSum
#         return root.data+leftSum+rightSum
# 
# def totalMax(self,root):
#     if root is None:
#         return 0
#     else:
#         leftMax=totalMax(root.left)
#         rightMax=totalMax(root.right)
#     return max(root.data,leftMax,rightMax)
# 
# def treeHeight(self,root):
#     if rrot is None:
#         return 0
#     else:
#         leftHeight=treeHeight(root.left)
#         rightHeight=treeHeight(root.right)
#         return 1+max(leftHeight,rightHeight)
# 
# def existInTree(self,root,value):
#     if root is None:
#         return False
#     else:
#         inLeft=existInTree(root.left,value)
#         inRight=existInTree(root.right,value)
#         return root.data==value or inLeft or inRight
# 
# def reverseTree(self,root):
#     if root is None:
#         return
#     else:
#         reverseTree(root.left)
#         reverseTree(root.right)
#         root.left,root.right=root.right,root.left

'''Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.
Example 1:
Input: n = 5
Output: 2
Explanation: 5=2+3

Example 2
Input: n = 9
Output: 3
Explanation: 9-4+5-2+3+4

Example 3:
Input: n = 15
Output: 4
Explanation:15=8+7=4+5+6=1+2+3+4+5'''