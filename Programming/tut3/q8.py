
   num=int(input())
    a=str(num)
    n=0
    b=len(a)
    for i in range(len(a)):
        print (a[i])
        n = n +(int(a[i])**b) 

    print(n)
    if n==num:
        print ("Yeahhhh boiiii")
    else:
        print ("Nah")



