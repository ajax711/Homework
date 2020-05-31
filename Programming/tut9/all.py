import math
import random

#question 1
def printsquare():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    l1=l[:5]
    l2=l[-5:]
    l1.extend(l2)
    print (l1)
#printsquare()

#input list command
list1 = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    element = input() 
  
    list1.append(element)

list2 = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    element = input() 
  
    list2.append(element)
#question 2
def diff():
	print(set(list1)-set(list2))

#diff()

#question 3
element=input("enter an element")
def listindex():
  try:
   print(list1.index(element))
  except ValueError:
    print("element not in list")
#listindex()

#question 4
def randomele(list1):
  print(random.choice(list1))

#randomele(list1)

#ques5
def rotatelist(list1):
    k=list[1]
    for i in range(0,len(list1),2):
        list1[i]=k[i+1]
        list1[i+1]=k[i]
    print (list1)

rotatelist()
