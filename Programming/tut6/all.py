sent=str(input("Input a string: "))
sent=sent.lower()

"""
l= len(sent)


#length
print ("Length :" + str(l))
#palindrome
a=0
for i in range(0,l):
    if sent[i]==sent[l-i-1]:
        a=a+1
if a==l:
    print ("Palindrome : Yes")

else:
    print ("Palindrome: No")



#reverse
#words=sent.split(' ')
#print (words[::-1])

print ('Reverse :' + sent[::-1])

#vowels
a=0
for i in sent:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        a=a+1
print ('Vowels :' + str(a))

#substring
a=0
subsent=str(input("Input a substring: "))
subl=len(subsent)

for i in range(0,l):
    n=sent[i:i+subl]
    if n==subsent:
        a=a+1
if a!=0:
    print ("Substring : Yes")
else:
    print ("Substring : No")

#common
anosent=str(input("Input second string : "))
anosent=anosent.lower()
anol=len(anosent)
print ("common letters :"),
for i in sent:
    if i in anosent:
        print (i)


#uncommon
print ("Uncommon letters :"),
for i in sent:
     if i not in anosent:
         print (i),
for i in anosent:
    if i not in sent:
        print (i)

"""
#duplicate #problem 
n=0
print ("Duplicate letters : "),
for i in sent:
    a=0
    for j in sent:
        if i==j:
            a=a+1
            if a>1:
                print (i)
                n=n+1

print ("Number of duplicate letters : " + str(n))

#even
print ('Words wih even letters" : ')
words=sent.split(' ')
for i in words:
    if len(i)%2==0:
        print (i)


