'''linked list'''
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return self.data   
# class LinkedList:
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next
#     def __iter__(self):
#         node=self.head
#         while node is not None:
#             yield node
#             node=node.next
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)
           
#     def add_last(self,node):
#         if self.head is None:
#             self.head = node
#             return
#         for current_node in self:
#             pass
#         current_node.next=node
# llist=LinkedList(['a','b'])
# llist.add_last(Node('c'))
# print(llist)

''' 466A Cheap Travel codeforce'''
# n,m,a,b=list(map(int,input().split()))
# if m*a<=b:
#     print(n*a)
# else:
#     print((n//m)*b+min((n%m)*a,b))

'''swap of 2 numbers in linked list'''
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#     def __repr__(self):
#         return self.data   
# class LinkedList:
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next
#     def __iter__(self):
#         node=self.head
#         while node is not None:
#             yield node
#             node=node.next
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)
#     def add_last(self,node):
#         if self.head is None:
#             self.head = node
#             return
#         for current_node in self:
#             pass
#         current_node.next=node
#     def swap_elements(self):
#         node=self.head
#         while node and node.next:
#             node.data,node.next.data=node.next.data,node.data
#             node=node.next.next
# LList=LinkedList(['12','76','43','8','56','3','9','88'])
# LList.swap_elements()
# print(LList)

#647 667 o/p:1->3->1->4
#56 1000 o/p:1->0->5->6
#swapping nodes in pairs
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data   
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def add_last(self,node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next=node
    def swap_elements(self):
         node=self.head
         while node and node.next:
             node.data,node.next.data=node.next.data,node.data
             node=node.next.next
    def addNumber(self,other):
        resList=LinkedList()
        temp=resList
        carry=0
        self=self.head
        other=other.head
        while (self !=None or other != None) or carry:
            sum = 0
            if self != None:
                sum += int(self.data)
                self = self.next
            if other != None:
                sum += int(other.data)
                other = other.data
            sum += carry
            carry= sum//10
            node = LinkedList([sum%10])
            temp.next = node
            temp = temp.next
        return resList.next

n1,n2=input().split()
Llist1=LinkedList(list(n1))
Llist2=LinkedList(list(n2))
LList1.addnumber(LList2)
print(Llist1)
print(Llist2)