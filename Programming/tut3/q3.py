def fizz_buzz(i):
    if i%3==0:
        if i%5==0:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif i%5==0:
        return "Buzz"
    else:
        return i
try: 
    i = int(input())
    if i>0:
        print(fizz_buzz(i))
    if i<0:
        print("Invalid input")
except:
    print("Invalid input")


    
