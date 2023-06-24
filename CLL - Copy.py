#CREATING NODE-DECLARATION & DEFINITION
class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
     
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print('linked list empty')
        else:
            temp=self.head #temp is first node
            while temp.next:
                print(temp.data,"->",end="")
                #temp data means first nod's data
                temp=temp.next
            print(temp.data)
            
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4
n5=node(60)
n4.next=n5
n5.next=n
obj.display()