sent=str(input("Input a string: "))

"""#1
k=int(input('Enter a length'))
print("The words with length more than " + str(k) + " are :")
words=sent.split(' ')
for i in words:
    if len(i)>k:
        print (i)

#2
i=int(input('Enter a index :'))
str1=sent[:i]+sent[i+1:]
print ('New string after removing character ' + str(i) + " is : " + str1)

#3 
words=sent.split(" ")
newsent=""
print ('-'.join(words)) 

#4 
a=0
for i in sent:
    if i in ['0','1']:
        a=a+1
if a==len(sent):
    print("String is binary")
else:
    print ("Not binary")

"""
#5
#Converting string in list 
charlist=list(sent)
for i in range(len(charlist)):
    if charlist[i]==',':
        charlist[i]='.'
    elif charlist[i]=='.':
        charlist[i]=','
    
newsent=""
print(newsent.join(charlist))

