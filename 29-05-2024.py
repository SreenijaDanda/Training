'''class'''
# class Person:
#     def __init__(self,name):
#         self.name= name
#     def say_hi(self):
#         print('hello,my name is',self.name)
# p=Person('siri')
# p.say_hi()

#2
# class Student:
#     def __init__(self,roll,name,phone,address):
#         self.roll=roll
#         self.name=name
#         self.phone=phone
#         self.address=address
#     
#     def displayInfo(self):
#         print("name:",self.name,"address:",self.address)
# st1=Student(2072,'siri',9059916565,'hanamkonda')
# st1.displayInfo()
# st2=Student(2051,'chikki',9876543210,'wrg')
# st2.displayInfo()

'''problem 1'''
# class test:
#     def __init__(self,a="hello"):
#         self.a=a
#     def display(self):
#         print(self.a)
# obj=test()
# obj.display()

'''write a python program to get a list,sorted in incerasing oder by the last element in each tuple from a
given list of non empty tuples.
sample input:[(2,5),(1,2),(4,4),(2,3),(2,1)]
output:[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''
# def end(tup):
#     return tup[-1]
# n=int(input())
# data=[tuple(map(int,input().split())) for i in range(n)]
# res=sorted(data,key=end)
# print(res)

'''input a list and sort the elements in the list based on its length.
input: hi 1 425 2104
output: ['1','hi','425','2104']'''
# dataList= input().split()
# print(sorted(dataList,key=len))

'''inheritence'''
'''single'''
# class Parent():
#     def first(self):
#         print('first function')
# class Child(Parent):
#     def second(self):
#         print('second function')
# ob=Child()
# ob.first()
# ob.second()

'''multiple'''
# class Parent:
#     def fun1(self):
#         print("this is function")
# class Parent2:
#     def fun2(self):
#         print("this is function2")
# class Child(Parent,Parent2):
#     def fun3(self):
#         print("this is")
# ob=Child()
# ob=func1()
# ob=func2()
# ob=func3()

'''problem 2'''
# class Test:
#     def __init__(self):
#         self.x=0
# class Derived_Test(Test):
#     def __init__(self):
#         self.y=1
# def main():
#     b=Derived_Test()
#     print(b,x,b,y)
# main()

# class Test:
#     def __init__(self):
#         self.x=0
# class Derived_Test(Test):
#     def __init__(self):
#         Test.__init__(self)
#         self.y=1
# def main():
#     b=Derived_Test()
#     print(b.x,b.y)
# main()

# class A:
#     n=10
#     def __init__(self,z,y=5):
#         self.zee=z
#         self.yee=y
#     def disp(self):
#         print(self.zee,self.n)
# class B(A):
#     def __init__(self,m,x,p):
#         super().__init__(x,p)
#         self.my=m
#     def p(self):
#         print(A.n,super().n)
# obj=B(10,15,21)
# obj.disp()
# obj.p()

# class A:
#     def __init__(self,z):
#         self.zee=z
# class B(A):
#     def __init__(self,z,x):
#         super().__init__(x)
#         self.zee=z
#     def p(self):
#         print(self.zee,A(12).zee)
# obj=B(10,15)
# obj.p()

# class A:
#     def __init__(self,x=3):
#         self._x=x
# class B(A):
#     def __init__(self):
#         super().__init__(5)
#     def display(self):
#         print(self._x)
# def main():
#     obj=B()
#     obj.display()
# main()

'''write a python program to remove duplicates from a list
input: 1 4 2 5 5 3 4 7
output: [1,4,2,5,3,7]'''
# numList=list(map(int,input().split()))
# resList=[]
# for i in numList:
#     if i not in resList:
#         resList.append(i)
# print(resList)

'''overriding'''
# class Product:
#     def disp(self):
#         print("this is product info")
# class Cal(Product):
#     def disp(self):
#         print("this is a calculation info")
#         super().disp()
# p1=Cal()
# p1.disp()

'''problem 3'''
# class A:
#     def __str__(self):
#         return'1'
# class B(A):
#     def __init__(self):
#         super().__init__()
# class C(B):
#     def __init__(self):
#         super().__init__()
# def main():
#     obj1=B()
#     obj2=A()
#     obj3=C()
#     print(obj1,obj2,obj3)
# main()

'''problem 4'''
# class A:
#     def __init__(self):
#         self.m='hi'
#     def __str__(self):
#         return 'hello'
#    
# objA=A()
# print(objA.m)

'''problem 5'''
# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return 1
#     def __eq__(self,other):
#         return self.x*self.y==other.x*other.y
# obj1=A(5,2)
# obj2=A(2,5)
# print(obj1==obj2)

'''problem 6'''
'''Some prime numbers can be expressed as a sum of other consecutive prime numbers
For example
5-2+3,
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N
subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above
mentioned property in a given range
Input Format: The first line contains a number N
Output Format: Print the total number of all such prime numbers which are less
than or equal to N
Constraints: 2<N<=12000000000'''
# def isPrime(num):
#     if num == 0 or num == 1:
#         return False
#     for deno in range(2,int(num**0.5)+1):
#         if num% deno==0:
#             return False
#     return True
# num = int(input())
# primeList=[i for i in range(2,num+1) if isPrime(i)]
# print(primeList)
# count,pSum=0,primeList[0]
# for p in primeList[1:]:
#     pSum += p
#     if pSum > num:
#         break
#     if isPrime(pSum):
#         count += 1
# print(count)

# class Shape(metaclass=ABCMeta):
#     def __init__(self):
#         print("i am in init")
#     def draw_shape(self):
#         pass
#     def set_color(self):
#         pass
# class Circle(Shape):
#     def draw_shape(self):
#         print("Draw Circle")