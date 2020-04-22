def no_2_word(n):
    if n==2:
        return "Second"
    elif n==3:
        return "Third"
    else:
        return str(n)+"st"

def polAr(X,Y,n):
    area = 0
    for i in range(n):
        area += ((X[i]*Y[i+1])-(Y[i]*X[1+i]))
    return area/2

n = input("Number of vertices")
n=int(n)
for i in range(1,n):
    X[i],Y[i]=int(input("Enter the"+ no_2_word(i) + "pair of coordinate separated by a comma").split())
#print(polyAr(X[],Y[],n))
