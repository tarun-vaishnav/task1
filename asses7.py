year = int(input("Enter Year(1001-9999): "))

if ((year%4==0 and year%400==0 ) or year%100==0):
    print("True")
else:
    print("False")