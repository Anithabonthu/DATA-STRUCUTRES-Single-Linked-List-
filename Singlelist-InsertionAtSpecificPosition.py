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
    def insert_End(self,value):
        new=Node(value)
        if self.head is None:
            self.head=new
        else:
            curr=self.head
            while curr.next != None:
                curr=curr.next
            curr.next=new
    def insertAt_Position(self,pos,val):
        index=0
        if pos==index:
            self.insert_begin(val)
        else:
            prev=None
            ptr=self.head
            index=1
            flag=0
            while ptr:
                if index == pos:
                    new=Node(val)
                    prev.next=new
                    new.next=ptr
                    flag=1
                    break
                index+=1
                prev=ptr
                ptr=ptr.next
            if flag==0:
                print("Index is not found.")
    def print(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next
l=LinkedList()
while True:
    print("1.Insert at the beginning   2. Insert at the end   3.Insert at Specific Position  4.Traverse 5.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert_begin(value)
    elif ch==2:
        value=int(input("Enter data value: "))
        l.insert_End(value)
    elif ch==3:
        value=int(input("Enter data value: "))
        position=int(input("Enter Position to insert the data: "))
        l.insertAt_Position(position,value)
    elif ch==4:
        l.print()
    elif ch==5:
        break

        
        

        

