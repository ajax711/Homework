def Perfectnumber(n):
    if (n<1):
        return "Error"
    sum=1
    i=2
    while i * i <= n: 
        if n % i == 0: 
            sum = sum + i + n/i 
        i += 1
    return (True if sum == n and n!=1 else False)

def perfectsquare(n):
     g=pow(n,0.5)
     if(int(g)==g):
         return True
     else:
         return False

def Arm(n):
    alt=n
    sum=0
    l=len(str(n))
    while n>0:
        dig=n%10
        sum=sum+(dig**l)
        n=n//10

    if alt==sum:
        return True
    else:
        return False

def Fib(n):
    one = 5*n*n + 4
    two = 5*n*n - 4
    if perfectsquare(one) or perfectsquare(two):
        return True
    else:
        return False
