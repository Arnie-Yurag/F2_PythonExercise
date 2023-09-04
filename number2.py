n1 = int(input("1st integer: "))
n2 = int(input("2nd integer: "))
n3 = int(input("3rd integer: "))

# can use max function
if n1 > n2:
    maxN = n1
elif n3 > n2:
    maxN = n3
else:
    maxN = n2


print("The maximum number is: ", maxN)
