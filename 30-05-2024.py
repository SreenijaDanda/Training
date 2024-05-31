'''print sum of all odd numbers present in a large number
3446877846445566
output=27'''
# num=int(input())
# totsum = 0
# while num != 0:
#     rem = num % 10
#     if rem % 2 != 0:
#         totsum += rem
#     num //= 10
# print(totsum)

'''2'''
# num2 = input()
# oddList = ['1','3','5','7','9']  #oddstr='13579'
# totalsum = 0
# for i in num2:
#     if i in oddList:    #if i in oddstr:
#         totalsum += int(i)
# print(totalsum)

'''progeam to sort first half in ascending order and second half in descending order in an array
input:1 21 5 2 50 16
output:1 2 5 50 21 16'''
# numList = list(map(int,input().split()))
# n = len(numList)
# res = sorted(numList)[:n//2]
# print(res)
# res += sorted(numList,reverse=True)[:n//2]
# print(res)

'''police codeforce'''
# num = int(input())
# events = list(map(int,input().split()))
# avaPolice = 0
# unEvents = 0
# for event in events:
#     if event > 0:
#         avaPolice += event
#     elif event == -1:
#         if avaPolice <= abs(event):
#             unEvents += abs(event) - avaPolice
#             avaPolice = 0
#         else:
#             avaPolice -= abs(event)
# print(unEvents)

'''codeforce question(watermelon)'''
# weight=int(input())
# if weight%2==0 and weight>2:
#     print("YES")
# else:
#     print("NO")

'''reverse a string keeping its special character at the same place
i/p:h@ello o/p:o@lleh'''
# import re
# string = input()
# string_list = re.findall("[a-zA-Z]",string)
# string_list.reverse()
# for i in range(len(string)):
#     if(string[i]=='#' or string[i]== "@"):
#         string_list.insert(i,string[i])
# print("".join(string_list))