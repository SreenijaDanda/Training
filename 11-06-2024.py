'''leetcode 1863'''
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         subset = []
#         for i in range(n+1):
#             subset.extend(list(itertools.combinations(nums,i)))
#         res = 0
#         for sset in subset:
#             sslen = len(sset)
#             if sslen <= 1 and sslen >= 0:
#                 res += sum(sset)
#             else:
#                 XOR = sset[0]
#                 for i in sset[1:]:
#                     XOR ^= i
#                 res += XOR
#         return res

'''leetcode 409'''
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         countList = [s.count(i) for i in set(s)]
#         evenList = [i for i in countList if i%2==0]
#         oddList = [i-1 for i in countList if i%2!=0]
#         res = sum(evenList)
#         if oddList != []:
#             res += sum(oddList) + 1
#         return res

'''leetcode 1720'''
# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         res = [first]
#         for i in range(len(encoded)):
#             res.append(encoded[i] ^ res[i])
#         return res

'''leetcode 2574'''
# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         return [abs(sum(nums[:i])-sum(nums[i+1:])) for i in range(len(nums))]

'''leetcode 942'''
# class Solution:
#     def diStringMatch(self, s: str) -> List[int]:
#         resList = []
#         high,low = len(s),0
#         k = 1
#         for ch in s:
#             if ch=='i' or ch=='I':
#                 resList.insert(k,low)
#                 k += 1
#                 low += 1
#             elif ch == 'd' or ch == 'D':
#                 resList.insert(k,high)
#                 k += 1
#                 high -= 1
#         resList.append(high)
#         return resList