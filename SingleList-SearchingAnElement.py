#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
    def Search_Element(self,ele):
        ptr=self.head
        flag=0
        while ptr is not None:
            if ptr.data == ele:
                print(ele," is present in the list.")
                flag=1
                break
            ptr=ptr.next
        if flag==0:
            print(ele," is not present in the list.")
   
l=LinkedList()
while True:
    print("1.Insertion  2.Search an element  3.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        value=int(input("Enter data value: "))
        l.insert(value)
    elif ch==2:
        search_ele=int(input("Enter element to be search: "))
        l.Search_Element(search_ele)   
    elif ch==3:
        break
        
        


# In[ ]:




