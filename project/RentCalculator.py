## Inputs we need from the user
# Total rent of the living
# Total charge of Ordered food
# Electricity Units spend
# Chagre per Unit
# Total number of people Living


Total_Rent = int(input (" Enter the total of your house/flat rent : "))
Food_ordered = int(input(" Enter the amount of Total food ordered : "))
Electricity_Units = int (input (" Enter the Electricity Units spend : "))
charge_unit = int(input (" Enter the total charge per unit : ")) 
Total_people = int (input( " Enter the total number of people living : "))

Electricity_bill = Electricity_Units * charge_unit

Total_Rent_share = (Total_Rent + Food_ordered + Electricity_bill) // Total_people

print (f" The amount of Rs {Total_Rent_share} Should be paid by Each person living.")  