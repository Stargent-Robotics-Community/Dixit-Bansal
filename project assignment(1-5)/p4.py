i1 = int(input("Enter 1st integer:"))
i2 = int(input("Enter 2nd integer:"))
i3 = int(input("Enter 3rd integer:"))
i4 = int(input("Enter 4th integer:"))
i5 = int(input("Enter 5th integer:"))


integers = [i1, i2, i3, i4, i5]
i = 0
sum=0
while i<5:
    sum=sum+integers[i]
    i=i+1
print(sum) 


