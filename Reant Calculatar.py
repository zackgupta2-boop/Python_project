rent = int(input("Enter your home/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spent = int(input("Enter the total of electricity spent = "))
charge_per_unit = int(input("Enter the charge per unit of electricity = "))
persons = int(input("Enter the number of persons in the house/flat = "))

total_bill = electricity_spent * charge_per_unit

output = (rent + food + total_bill) // persons
print("The amount to be paid by each person is = ", output)
