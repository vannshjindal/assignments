# Coffee machine with running inventory and error handling

water = 100
milk = 100
coffee = 50

try:
    user = input("Enter your name dear: ")

    while True:
        print(f"\nHello {user}! ☕ Here's our menu:")
        print("1. Cappuccino - ₹70 (10L Water, 10L Milk, 3g Coffee)")
        print("2. Mocha      - ₹80 (15L Water, 7L Milk, 7g Coffee)")
        print("3. Latte      - ₹30 (5L Water, 15L Milk, 10g Coffee)")
        print("0. Exit")

        choice = input("\nEnter your choice (1/2/3 or 0 to exit): ").strip()

        if choice == "1":
            if water >= 10 and milk >= 10 and coffee >= 3:
                water -= 10
                milk -= 10
                coffee -= 3
                print(f"\nHere is your ☕ Cappuccino, {user}! Your total is ₹70.")
            else:
                print("\n❌ Sorry, not enough ingredients for Cappuccino.")

        elif choice == "2":
            if water >= 15 and milk >= 7 and coffee >= 7:
                water -= 15
                milk -= 7
                coffee -= 7
                print(f"\nHere is your ☕ Mocha, {user}! Your total is ₹80.")
            else:
                print("\n❌ Sorry, not enough ingredients for Mocha.")

        elif choice == "3":
            if water >= 5 and milk >= 15 and coffee >= 10:
                water -= 5
                milk -= 15
                coffee -= 10
                print(f"\nHere is your ☕ Latte, {user}! Your total is ₹30.")
            else:
                print("\n❌ Sorry, not enough ingredients for Latte.")

        elif choice == "0":
            print(f"\nGoodbye {user}! Come again soon ☕")
            break

        else:
            print("\n❌ Invalid choice. Please choose 1, 2, 3 or 0.")

        # Show remaining inventory after every choice
        print(f"\n📦 Remaining inventory:\nWater: {water}L\nMilk: {milk}L\nCoffee: {coffee}g")

except Exception as e:
    print("\n⚠️ Oops! Something went wrong:", str(e))
