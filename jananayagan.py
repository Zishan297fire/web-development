actual_cost = float(input("Please enter the actual product price:"))
sale_amount = float(input("Please enter the sales price:"))
if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No profit!!!")
