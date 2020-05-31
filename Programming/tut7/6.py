n=int(input("Length of string"))
sent=str(input("Input a string"))
if len(sent)!=n:
    print("String length incorrect")

if len(sent)!=n:
    print("String length incorrect")

else:
    d=int(input("Enter rotation index"))
    print("Left :" + sent[d:] + sent[:d])
    print('Right:' + sent[n-d:] + sent[:n-d])





