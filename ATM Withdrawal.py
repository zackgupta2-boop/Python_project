''' ATM Withdrawal '''

balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw % 100 != 0:
    print("Withdrawal amount must be multiple of 100")

elif withdraw > balance:
    print("Insufficient balance")

elif balance - withdraw < 500:
    print("Minimum balance of ₹500 should remain")

else:
    balance = balance - withdraw
    print("Remaining balance = ₹", balance)
