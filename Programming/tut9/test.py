def change_pos(l):
    if len(l)%2!=0:
        change_pos(l[0:len(l)-1])


    k=l
    for i in range(0,len(l),2):
        l[i],l[i+1]=k[i+1],k[i]
    return l



l=[0,1,2,3,4,5]
print(change_pos(l))
