#Name:Quenaysia Hunter
#Program Name: Stock Profit Calculator
#Description: This program calculates the total cost of buying stocks, the profit from selling stocks,
#and displays the results with appropriate labels.


# Define stock name
stock_name= 'Tech Innovations Inc.'
#Define stock price and shares to buy
price_per_stock= 61.37
shares_to_buy= 725

#Calculate total cost of buying stocks
total_cost= price_per_stock * shares_to_buy

#Define administrative fee for buying
admin_fee_buy= 8.49

#Calculate total cost including administrative fee
total_cost_with_fee= total_cost + admin_fee_buy

#Define commission rate for buying
commission_rate_buy= 0.025 #2.5%
commission_fee_buy= total_cost + commission_rate_buy

#Calculate total cost including commission fee
final_cost_buy= total_cost_with_fee + commission_fee_buy

#Output results for buying stocks
print(f'Stock Name: {stock_name}')
print(f'Price per Stock: ${price_per_stock}')
print(f'Shares to Buy: {shares_to_buy}')
print(f'Total Cost (without fees): ${total_cost}')
print(f'Administrative Fee: ${admin_fee_buy}')
print(f'Commission Fee: ${commission_fee_buy}')
print(f'Final Cost (with fees): ${final_cost_buy}')


# Define new stock price and shares to sell
new_price_per_stock = 84.38
shares_to_sell= 450

#Calculate total revenue from selling stocks
total_revenue = new_price_per_stock * shares_to_sell

#Define administrative fee for selling
admin_fee_sell= 10.99

#Calculate total revenue including administrative fee
total_cost_with_fee= total_revenue - admin_fee_sell

#Define commission rate for selling
commission_rate_sell = 0.0285 # 2.85%
commission_fee_sell = total_revenue * commission_rate_sell

#Calculate final revenue after commission
final_revenue = total_cost_with_fee - commission_fee_sell

#Calculate net profit or loss
net_profit_or_loss = final_revenue - final_cost_buy

#Output results for selling stocks
print(f"nNew Price Per Stock: ${new_price_per_stock}")
print(f"Shares to Sell: {shares_to_sell}")
print(f"Total Revenue (without fees): ${total_revenue}")
print(f"Administrative Fee for Selling: ${admin_fee_sell}")
print(f"Commission Fee for Selling: ${commission_fee_sell}")
print(f"Final Revenue (after fees): ${final_revenue}")
print(f"Net Profit or Loss: ${net_profit_or_loss}")
















