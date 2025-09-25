actual_cost = float(input("Please Enter the actuall product price: "))
sale_amount = float(input("Please Enter the sale amount: "))
if (Sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}". format(amount))
else: 
    print("No Profit!!!")