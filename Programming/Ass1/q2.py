def sal_calc(salary):
    if 1<= salary <= 4000:
        return salary+(0.1*salary)+(0.5*salary)
    elif 4001 <= salary <= 8000:
        return salary+(0.2*salary)+(0.5*salary)
    elif 8001 <= salary <=  12000:
        return salary+(0.25*salary)+(0.7*salary)
    elif salary >= 12000:
        return salary+(0.3*salary)+(0.8*salary)
    else:
        return "Invalid Salary"

try:
    salary = float(input("Enter your salary :"))
    print("Gross Salary = " + str(sal_calc(salary)))

except:                             #If any errors arise in the try block, it will print Invalid Salary
    print ("Invalid salary")        #instead of the error. Used it to rule out string as an input.



