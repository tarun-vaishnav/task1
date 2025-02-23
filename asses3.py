def fact(number):
    if number==0 or number==1:
        return 1
    else:
        return number*fact(number-1)

number = int(input("Enter number"))
factorial = fact(number)
print("Factorial is: ",factorial)