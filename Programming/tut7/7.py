def pattern(x,str1,str2):
  for i in range(1,x+1):
    print(str1,end="")
    print(str2*i, end="")
n=int(input("Length"))
str1=str(input("Str1"))
str2=str(input("Str2"))
pattern(n,str1,str2)
