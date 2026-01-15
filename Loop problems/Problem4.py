# Reverse a String using loop

input_Str = input("Enter a String to be reversed : ")

reversed_str = ""
for char in input_Str:
    reversed_str = char + reversed_str
print(reversed_str)