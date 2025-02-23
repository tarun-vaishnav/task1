number = int(input("Enter a number"))
i=0
temp = number

while temp>0:
    i+=1
    temp//=10

sum = 0
temp=number

while temp>0:
    rem = temp%10
    j=i
    mult =1
    while j>0:
        mult = mult*rem
        j-=1
    sum+=mult
    temp//=10

if sum == number:
    print("True")
else:
    print("False")