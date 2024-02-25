#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new
    def print(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
    def Reverse(self):
        prev=None
        curr=self.head
        ptr=curr.next
        while curr.next != None:
            curr.next=prev
            prev=curr
            curr=ptr
            ptr=ptr.next
        curr.next=prev
        self.head=curr
        print("The Reverse of Linked List is:")
        l.print()
l=LinkedList()
while True:
    print("1.Insertion  2.Reverse of linked list  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==2:
        l.Reverse()
    elif ch==3:
        break


        

        









# In[ ]:





# In[ ]:




