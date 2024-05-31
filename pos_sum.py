#function accept an integer arrvof size length,writ python code for returning the sume
# of second largest element from odd position and second largest from  even position
length=int(input())
Arr=list(map(int,input().split()))
Even_Arr=[]
Odd_Arr=[]
for i in range(length):
    if i%2==0:
        Even_Arr.append(Arr[i])
    else:
        Odd_Arr.append(Arr[i])
Even_Arr=sorted(Even_Arr)
Odd_Arr=sorted(Odd_Arr)
output=Even_Arr[-2] + Odd_Arr[-2]
print(output)
        