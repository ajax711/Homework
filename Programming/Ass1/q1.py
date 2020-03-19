import datetime

def check_if_month_is_valid(month):
    if str(month).isdigit():
        if int(month)<=12:
            return True
    else:
        return False

def check_if_day_is_valid(day):
    if str(day).isdigit():
        if int(day)<=31:
            return True
    else:
        return False


day, month = int(input("Date : ")), int(input("Month : "))
if ((check_if_day_is_valid(day)) == False) or ((check_if_month_is_valid(month)) ==
False):
    print ("Invalid values")

else:
    dayofweek = datetime.date(2020, month, day).strftime("%A")
    print(dayofweek)
