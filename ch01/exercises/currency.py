rate = input("Enter Current Exchange Rate For Euro To Dollar:")
rate = float(rate)
print("You have entered:", rate)
amount = input("Enter Amount To Exchange:")
amount = float(amount)
print("You have entered:", amount)
total = amount*rate
result  = total - 3.00
print("result:",result)