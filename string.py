a=input().split(",")
b=""
for i in a:
    i=i.split(":")
    if(str(len(i[0])) in i[1]):
        b=b+i[0][-1]
    else:
        b=b+"x"
print(b)