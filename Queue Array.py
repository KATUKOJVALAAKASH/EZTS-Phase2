#queue implementataion using list or Array!!
queue=[]
def enqueue():
    element=input("Enter Element")
    queue.append(element)
    print(element,"is added in q")
def dequeue():
    if not queue:
        print("Q is Empty")
    else:
        e=queue.pop(0)
        print("Removed element",e)
def display():
    print(queue)
while True:
    print("Select option 1.Add 2.Remove 3.Display 4. Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct option")
        