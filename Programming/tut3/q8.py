try:
    num=int(input())
    a=str(num)
    n=0
    for i in range(len(a)):
        print (a[i])
        n = n + ( int(a[i])* int(a[i])* int(a[i]) ) 

    print(n)
    if n==num:
        print ("Yeahhhh boiiii")
    else:
        print ("Nah nigga")

except Value Error:
    print ("invalid input")
