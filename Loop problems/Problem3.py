# Print the Multiplication Table for a given number up to 10 , but skip the 5th Iteration

n = 11
x = int (input("Enter a number for Multiplication Table : "))
for i in range(1,n):
    if i == 5:
        continue
    print (f"{x} X {i} = {x*i}")
    