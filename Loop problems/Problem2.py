# Calculate the sum of even numbers up to the given number n

n = int(input("Enter a number : "))
sum = 0
for i in range (n):
    if i % 2 == 0:
        sum += i 
print(sum)