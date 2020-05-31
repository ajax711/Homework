dic={'a':'abra', 'b':'barbara', 'k':'kite', 'i':'index'}
def print_hist():
    z=(sorted(dic))
    for i in z:
        k=[]
        k.append(dic[i])
    new=dict(zip(z,k))
    print (new) 
print_hist()
