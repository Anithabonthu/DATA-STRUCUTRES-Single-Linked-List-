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
    def insert_begin(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new
    def insert_end(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new
    def traverse(self):
        if self.head is None:
            print("List is Empty")
        print("The Linked List is: ")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
    def ToFindLength(self):
        len=0
        temp=self.head
        while temp:
            len+=1
            temp=temp.next
        return len
l=LinkedList()
while True:
    print("1.Insert at the beginning   2. Insert at the end   3.Traverse  4.Length of Linked list 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert_begin(value)
    elif ch==2:
        value=int(input("Enter data value: "))
        l.insert_end(value)
    elif ch==3:
        l.traverse()
    elif ch==4:
        print("Length Of The Linked list: ",l.ToFindLength())
    elif ch==5:
        break
        


# In[ ]:




