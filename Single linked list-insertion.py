#!/usr/bin/env python
# coding: utf-8

# In[14]:


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
l=LinkedList()
while True:
    print("1.Insert at the beginning   2. Insert at the end   3.Traverse  4.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert_begin(value)
    elif ch==2:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==3:
        l.print()
    elif ch==4:
        break
        
        

        


# In[ ]:





# In[ ]:




