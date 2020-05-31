import string_check as a

sent=str(input("Enter a sentence :"))
words=sent.split(" ")
while len(words)!=8:
    sent=str(input("Enter a sentence :"))
    words=sent.split(" ")

print (a.avoid(words[0],words[1]))
print (a.uses_only(words[4],words[5]))
print (a.uses_all(words[2],words[3]))
print (a.is_alphabetic(words[6]))
