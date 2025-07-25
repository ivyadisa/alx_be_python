purchase_amout = float(input("Enter the purchase amount: "))

if purchase_amout >= 1000:
    discount = 0.1
elif purchase_amout >= 500:
    discount = 0.05
else:
    discount = 0

final_price = purchase_amout * (1 - discount)
print("Final price after discount: $" + str(final_price))