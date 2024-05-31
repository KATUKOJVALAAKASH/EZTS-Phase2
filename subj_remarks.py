l1=list(map(int,input("Enter your marks details :").split()))
mini=l1[-1]
if len(l1)>4:
    print("inavlid input")
else:
    if(l1[0] and l1[1] and l1[2] >mini):
        print("pass")
    else:
        print("nice try")