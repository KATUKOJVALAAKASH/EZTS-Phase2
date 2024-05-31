#CREATING NODE-DECLARATION & DEFINITION
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    
    def __init__(self):
        self.head=None
        
    def deletefirst(self):
       temp=self.head
       self.head=temp.next
       temp.next=None
       
    def deletelast(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
            prev.next=temp.next
            temp.next=None
            
    def search(num):
        temp=self.head
        while temp:
            if temp.data==num:
                print("yes")
                break
            temp=temp.next
            print("Not present")
            
            
    def display(self):
        if self.head is None:
            print('linked list empty')
        else:
            temp=self.head #temp is first node
            while temp:
                print(temp.data,end=" ")#temp data means first nod's data
                temp=temp.next
                
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
obj.delete_position(3)
print('\n')
obj.display()
obj.deletelast()
print('\n')
obj.display()
obj.deletefirst()
print('\n')
obj.display()
obj.search(10)

