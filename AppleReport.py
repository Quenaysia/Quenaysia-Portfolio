#Quenaysia Hunter
#Apple Profits
#This program calculates the profit from apple sales based o user input for the number of
#apples sent, the number of apples left, and computes spoilage, original cost, and profit at
#different sale prices.

#grocery store name and apple quantities
grocery_store_name=input("The Local Market:")
original_apples_sent=int(input("600:"))
apples_left_to_sell=int(input("100:"))

#calculate the number of apples sold
apples_sold= original_apples_sent - apples_left_to_sell

# calculate the spoilage, the spoilage is 4% of the original apples sent
spoilage_percentage= 0.04
spoilage= original_apples_sent * spoilage_percentage

#calculate the original cost
cost_per_apple= 0.079
original_cost= original_apples_sent + cost_per_apple * cost_per_apple

#calculate profit if apples are sold for $1.29 each
selling_price_regular= 1.29
profit_regular= selling_price_regular * apples_sold - original_cost

#calculate profit if apples are sold for the sale price of $1.09
selling_price_sale= 1.09
profit_sale= selling_price_sale * apples_sold - original_cost

#Display all results
print(f"\nGrocery store: {grocery_store_name}")
print(f"Original Number of apples Sent: {original_apples_sent}")
print(f"Number of Apples Left to Sell:{apples_left_to_sell}")
print(f"Number of Apples Sold:{apples_sold}")
print(f"Total Spoilage (4%): {spoilage:.2f}")
print(f"Original Cost of Apples:${original_cost:.2f}")
print(f"Profit if Sold for $1.29 Each:${profit_regular:.2f}")
print(f"Profit if Sold for $1.09 Each:${profit_sale:.2f}")










