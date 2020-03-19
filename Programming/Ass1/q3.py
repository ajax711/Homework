import math

def perf_sq(n):
    k=math.sqrt(n)
    if k/int(k) != 1:
            return "It is not a perfect square"

    else:
        return 'It is a perfect square'


def perf_num(n):
    a=1
    for i in range(1,n):
        if n%i==0:
            a=a+i
    if a==n:
        return 'It is a perfect number'
    else:
        return 'Not a perfect number'

n = str(input("Enter a natural number"))

if n.isdigit()==False:
    print ('Invalid input')
else:
    n=int(n)
    print perf_sq(n)
    print perf_num(n)

