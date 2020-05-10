t=int(input("Enter a number"))
n1=count=0
n2=1
if t<0:
    print("Enter a positive value")
elif t==1:
    print(n1)
else:
    while count<t:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1

