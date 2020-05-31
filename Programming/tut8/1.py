import random
ls=[]
n=int(input("How many elements :"))
for i in range(n):
    k=input("Element" +str (i) +": ")
    ls.append(k)

#1
def nodupe(ls):
    nodupli=[]
    for a in ls:
        if a not in nodupli:
            nodupli.append(a)
    return nodupli


#2
def if_empty(ls):
    if len(ls)==0:
        return "Empty list"
    else:
        return "List not empty"

#3
def clone(ls):
    clone=[]
    for i in ls:
        clone.append(i)

    return clone

#4
def max_num(ls):
    a=[]
    for i in ls:
        if i.isnumeric():
            a.append(int(i))
    return max(a)

#5
def two_last(ls):
    a=[]
    for i in ls:
        if len(i)>=2 and i[0]==i[-1]:
            a.append(i)
    return len(a)

#6
def common(ls):
    n=0

    a=[]
    m=int(input("How many elements in the second list :"))
    for i in range(m):
        k=input("Element" +str (i) +": ")
        a.append(k)

    for i in a:
        if i in ls:
            n=n+1
    if n>0:
        return True
    else:
        return False


#7
def del_el(ls):

    del_ls=[]

    z=int(input("How many elements to delete :"))
    for i in range(z):
        k=int(input("Element" +str (i) +": "))
        del_ls.append(k)
    
    del_ls.sort(reverse=True)
    if del_ls[0]>(len(ls)-1):
        return "List not big enough"
    else:
        for i in del_ls:
            del ls[i]
        return ls

#8 
def shuf_list(ls):
    random.shuffle(ls)
    return ls

def main():
    #print (nodupe(ls))
    #print (if_empty(ls))
    #print (clone(ls))
    #print (max_num(ls))
    #print (two_last(ls))
    #print (common(ls))
    print (del_el(ls))
    #print (shuf_list(ls))
print (ls)
main()
