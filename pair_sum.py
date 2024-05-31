a=[10,20,35,75,50,80]
x=30
for i in range(0,len(a),1):
    for j in range(i+1,len(a),1):
        if(a[i]+a[j]==x):
            print("yes\n",a[i],a[j])
            break
            
            