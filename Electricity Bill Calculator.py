unit = int(input("enter number: "))

if unit <=100:
    bill = unit * 5
elif unit <= 300:
    bill = unit * 7
elif unit <= 500:
    bill = unit * 10
else:
    bill = unit * 15
print("electricity bill =", bill)
