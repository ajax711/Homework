import math

c = 2*math.sqrt(2)/9801

def sqrt_fact(k):
    return ((math.factorial(k))^2)

def add(k):
    return (1103+(26390*k))

def power(k):
    return math.pow(396,(4*k))

def numerator(k):
    return (math.factorial(4*k)*add(k))

def denominator(k):
    return (sqrt_fact(k)*power(k))
a=0
while (a<(10^15)):
    k=1
    a = numerator(k)/denominator(k)
    print a
    k=k+1

pi = 1/(c*a)

print (pi)
