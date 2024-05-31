#stack is LIFO-last in first out
stack=[]
def push():
    element=int(input("Enter the Element:"))
    stack.append(element)
    
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("Removed element:",e)
        
def display():
    print(stack)

def peek():
    if not stack:
        print("stack Empty")
    else:
        print("Peek Element",stack.pop())
    
while True:
    print("select operation 1.Push 2.Pop 3.display 4.Peek 5. Quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("Enter the correct option")
    