def fibolist(n):
    list1.append(1)
    list1.append(1)
    for i in range(1,n-1):
        list1.append(list1[i]+list1[i-1])

n = int(input("Enter length of list: "))
list1=[]
fibolist(n)
print(list1)