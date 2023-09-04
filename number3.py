num = int(input("Enter a number: "))

totalDigits = 0
smallest = 9
highest = 0

if num == 0:
    totalDigits = 1
    smallest = 0
    highest = 0
elif num < 0:
    num = -num
else:
    while num > 0:
        digit = num % 10
        totalDigits +=1

        if digit < smallest:
            smallest = digit
        if digit > highest:
            highest = digit
        num = num // 10

print("Number of digits in the given number is: ", totalDigits)
print("Smallest number is: ", smallest)
print("Highest number is: ", highest)

# digits = input("Please enter a number: ")
#
# # store digits
# totalDigits = len(digits)
# smallest = min(digits)
# highest = max(digits)
#
# print("Number of digits in the given number is: ", totalDigits)
# print("Smallest number is: ", smallest)
# print("Highest number is: ", highest)


