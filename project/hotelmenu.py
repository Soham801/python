# Menu of the restaurent

Menu = {
    'Pasta': 80,
    'Pizza':110,
    'Momos':60,
    'Biryani':250,
    'Cold Coffee': 90
}

print( "|| WELCOME TO PYTHON RESTRO || ")

print("We Serve -")

print ("Pizza:110\nPasta:80\nMomos:60\nBiryani:250\nCold Coffee:90")


Order_Total = 0

item_1 = input ("What would you like to have :")

if item_1 in Menu:
    Order_Total += Menu[item_1]
    print(f"You have Ordered {item_1}, Payable Amount is : ", Order_Total)
else:
    print("Add a item from the Menu")

another_item = input("Would you like to Order anything more? (YES / NO)")

if another_item == "YES":
    item_2 = input("What would you like to Have :")
    if item_2 in Menu:
     Order_Total += Menu[item_2]
    print(f"You have Ordered {item_2}")
    print (f"The total Payable amount after Ordering {item_1} and {item_2} is : " , Order_Total)

print("Thank You For Visiting US")

