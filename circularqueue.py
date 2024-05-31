#insert:rear=rear+1--We add new person at end of the queue
#delete:front=front+1--FIFO
class circularQueue():
    def __init__(self,size):
        #initializinf the class
        self.size=size
        #can use self.queue=[None]*size
        self.queue=[None for i in range(size)]
    def enqueue(self,data):
        #condition if queue is full
        if ((self.rear+1) % self.size==self.front):
            print("Queue is Full\n")
        #condition foe empty queue
        elif(self.front==-1):
            self.front=0
            self.rear=0
            sef.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=dataa
    def dequeue(self):
        if (self.front==-1):
            print("Queue is Empty\n")
        elif(self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front +1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("Queue is Empty")
        elif(self.rear >=self.front):
            print("Elements in the circular Queue are:",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements in circular Queue are:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if ((self.rear+1)%self.size ==self.front):
            print("queue is Full")
ob=circularQueue(5)
ob.enqueue(11)
ob.enqueue(22)
ob.enqueue(33)
ob.enqueue(44)
ob.display()
print("Deleted value=",ob.dequeue())
print("Deleted value=",ob.dequeue())
ob.display()
ob.enqueue(55)
ob.enqueue(66)
ob.enqueue(77)
ob.display()
ob.enqueue(88)


                
            
            
    
            
            