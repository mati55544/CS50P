# def main ():
#     print("Amount Due:50")
#     money:int = input("insert your coins-")
#     print(exchange(money))



# def exchange(money:int):
#     balance:int = ""
#     while True:
#         if money <=50:
#             balance = 50 - money
#             print("amount due:",balance)
        

#     x:int = 50
#     if money == x:
#         balance = x - 10
#     else: 
#         balance = "dc"
    

#     return balance

# main()
coins:int = [25, 10, 5]
amount_due:int = 50
total_inserted:int = 0
price = 50
while total_inserted < price:
    coin = int(input(f" Insert a coin:{coins} "))
    if coin in coins:
        total_inserted += coin
        amount_due -= coin
        print(f"Amount due: {amount_due}")
    else:
        print(f"Invalid coin. Please insert a coin in the following denominations: {coins}")

change =  amount_due
print(f"Change owed: {change} ")