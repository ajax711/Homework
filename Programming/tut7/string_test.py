import string_check as a

sent=str(input("enter a string"))
forbid=str(input("enter forbidden letter"))
print(a.avoid(forbid,sent))
print(a.uses_only(sent,forbid))

