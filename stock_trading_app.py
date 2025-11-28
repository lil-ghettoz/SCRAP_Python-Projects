import random


def buying():
    print("Welcome to the Stock Buying Section")
    stock_price = random.randint(100, 500)
    print(f"Current Stock Price: ${stock_price}")
    
    try:
        quantity = int(input("Enter the number of stocks you want to buy: "))
        total_cost = stock_price * quantity
        print(f"You have bought {quantity} stocks for a total of ${total_cost}.")
    except ValueError:
        print("Error, Please Type A Number!")
 
 
    
def selling():
    print("Welcome to the Stock Selling Section")
    stock_price = random.randint(100, 500)
    print(f"Current Stock Price: ${stock_price}")
    
    try:
        quantity = int(input("Enter the number of stocks you want to sell: "))
        total_revenue = stock_price * quantity
        print(f"You have sold {quantity} stocks for a total of ${total_revenue}.")
    except ValueError:
        print("Error, Please Type A Number!")




def main():
    print("Welcome to the Stock Trading App")
    while True:
        print("\n1. Buy Stocks")
        print("2. Sell Stocks")
        print("3. Exit")
        
        choice = input("Please choose an option (1-3): ")
        
        if choice == '1':
            buying()
        elif choice == '2':
            selling()
        elif choice == '3':
            print("Thank you for using the Stock Trading App. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


 
 
 