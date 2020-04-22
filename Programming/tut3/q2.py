for i in range(1000,3000):
    num=str(i)
    a=0
    for j in range(len(num)):
        if int(num[j])%2==0:
            a=a+1
    if a==4:
        print (i,end=",")

