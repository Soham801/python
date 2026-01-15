# age = int(input("Enter you age : "))
# day = (input("Enter today's Day:"))

# Movie_ticket = 0


# if age >= 18:
#     Movie_ticket = 12
#     if day == 'Wednesday':
#      Movie_ticket = Movie_ticket - 2
#     print(f"the price of the tickets are ${Movie_ticket} ")
# else:
#     Movie_ticket = 8
#     if day == 'Wednesday':
#      Movie_ticket = Movie_ticket - 2
#     print(f"The prices of Tickets are ${Movie_ticket}  ")


age = int(input("Enter you age : "))
day = (input("Enter today's Day:"))

price = 12 if age >= 18 else 8
if day == 'Wednesday':
    price = price -  2
print(f"The price of the Tickets are ${price}")