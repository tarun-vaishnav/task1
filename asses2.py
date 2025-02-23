def checker(number):
    if number%2==0:
        return True
    else:
        return False

number = int(input("Enter a number:"))
check = checker(number)
if check == True:
    print("Even")
else:
    print("Odd")