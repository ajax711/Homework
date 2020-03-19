from math import factorial as fact

def ncr(n,r):
    return fact(n)/((fact(n-r))*fact(r))

def print_row(n):
    for i in  range(n+1):
        print (ncr(n,i)),

n=str(input("How many rows of the pascal triangle :"))

if n.isdigit()==False:
    print ('Invalid input')
else:
    n=int(n)
    for i in range (n):
        print_row(i)
        print ("\n")
