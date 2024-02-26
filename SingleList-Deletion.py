#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
    def delete_Begin(self):
        print(self.head.data," is Deleted")
        self.head=self.head.next
    def delete_End(self):
        current = self.head
        Ptr=None
        while current.next is not None:
            ptr=current
            current=current.next
        ptr.next=None
        print(current.data,"is Deleted")
l=LinkedList()
while True:
    print("1.Insertion  2.delete_Begin 3.delete_End 4.traverse 5.exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==2:
        l.delete_Begin()
    elif ch==3:
        l.delete_End()
    elif ch==4:
        l.print()
    elif ch==5:
        break

