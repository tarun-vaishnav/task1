str1 = input("Enter String: ").replace(" ","").lower()
if str1 == str1[::-1]:
    print("Palindrome True")
else:
    print("Not a Palindrome")