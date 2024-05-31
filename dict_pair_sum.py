# Using dictionary find the pair sum.. 
A=[10,20,35,75,50,80]
x=30
d={}
for i in A:
    d[i]=1
for i in A:
    if x-i in d:
        print("true",i,x-i)
        c=1
        break
if(c==0):
    print("False") 