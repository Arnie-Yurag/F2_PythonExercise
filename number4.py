n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print(f"Sum of numbers from {n} = {total}")