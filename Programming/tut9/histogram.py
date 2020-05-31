def hist():
    d = dict()
    for k in string:
        d[k] = d.get(k, 0) + 1
    return d

string='hippopotamus'
print (hist())



