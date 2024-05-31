l=list(map(int,input("enter elements in to list:").split()))
key=int(input("Enter the number to search:"))
found = False
for index in range(len(l)):
    if l[index]==key:
        found = True
        break
if found==True:
     print("Element found at location=",index)
else:
    print("Element not found")
    