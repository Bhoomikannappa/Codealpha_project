STOCK_PRICES = {
    "NTPC": 319,
    "WIPRO": 260,
    "APL": 139,
    "ITC": 402
}

print("=" * 50)
print("PORTFOLIO MANAGEMENT SYSTEM")
print("=" * 50)
print()

while True:
    # Get user input
    print("_" * 40)
    stock_name = input("Enter Stock Symbol (e.g., APL, ITC): ").strip().upper()
    
    if stock_name == "EXIT" or stock_name == "QUIT":
        print("\nThank you for using Portfolio Management System!")
        break
    
    quantity = int(input("Enter Number of Shares: "))
    
    # Process investment
    if stock_name in STOCK_PRICES:
        price_per_share = STOCK_PRICES[stock_name]
        total_investment = price_per_share * quantity
        
        # Display investment summary
        print("\n" + "-" * 50)
        print("INVESTMENT SUMMARY")
        print("-" * 50)
        print(f"Stock: {stock_name}")
        print(f"Price per Share: Rs.{price_per_share}")
        print(f"Quantity: {quantity} shares")
        print(f"Total Investment: Rs.{total_investment}")
        print("-" * 50)
        
        # Save to portfolio file with UTF-8 encoding
        try:
            with open("portfolio.txt", "a", encoding="utf-8") as portfolio_file:
                portfolio_file.write(f"{stock_name} | {quantity} shares | Rs.{total_investment}\n")
            
            print("✓ Investment recorded in portfolio.txt")
            
        except Exception as e:
            print(f"⚠️  Error saving to file: {e}")
        
    else:
        print(f"\n⚠️  Stock '{stock_name}' not found in database.")
        print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    
    # Ask if user wants to continue
    print("\n" + "_" * 40)
    print("What would you like to do next?")
    print("1. Add another stock")
    print("2. View available stocks")
    print("3. Exit program")
    
    choice = input("Enter choice (1/2/3 or type 'exit'): ").strip().lower()
    
    if choice == "2":
        print("\nAvailable Stocks:")
        print("-" * 30)
        for stock, price in STOCK_PRICES.items():
            print(f"{stock}: Rs.{price}")
        print("-" * 30)
        continue
    elif choice == "3" or choice == "exit":
        print("\nThank you for using Portfolio Management System!")
        break
    elif choice != "1":
        print("\nContinuing with next stock entry...")
        continue

print("\n" + "=" * 50)
print("Program ended. Check 'portfolio.txt' for your investment records.")
print("=" * 50)