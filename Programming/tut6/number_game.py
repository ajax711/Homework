import random
import number_check as no
n=random.randrange(1,5)
a=int(input("Enter "))
print(n)
if n==1:
    print (no.Perfectnumber(a))

elif n==2:
    print (no.perfectsquare(a))

elif n==3:
    print (no.Fib(a))

elif n==4:
    print (no.Arm(a))


