def avoid(forbid,sent):
    a=0
    for i in sent:
        if i in forbid:
            a=a+1
    if a>1:
        return False
    else:
        return True

def uses_only(sent,forbid):
    a=0
    for i in sent:
        if i in forbid:
            a=a+1

    if a==len(sent):
        return True
    else:
        return False

def uses_all(sent,forbid):
    a=0
    for i in forbid:
        if i in sent:
            a=a+1
    if a==len(forbid):
        return True
    else:
        return False

def is_alphabetic(sent):
    for i in range(1,len(sent)):
        if sent[i]<sent[i-1]:
            return False

    return True



