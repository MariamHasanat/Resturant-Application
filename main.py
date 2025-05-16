if __name__ == "__main__":
    from MenuItem import MenuItem
    from Order import Order
    from Restaurant import Restaurant
    
    choice = input("\nWelcome to the Restaurant Management System!\nChoose an option:\n1. Add menu item\n2. View menu\n3. Create new order\n4. List all orders\n5. Exit\n")
    # Create an instance of Restaurant
    restaurant = Restaurant()
    
    while choice != '5':
        if choice == '1':
            name = input("Enter the name of the menu item: ")
            price = float(input("Enter the price of the menu item: "))
            category = input("Enter the category of the menu item: ")

            # Create an instance of MenuItem
            item = MenuItem(name, price, category)
            restaurant.set_menu_item(item)
            print("\nMenu item added successfully!")

        elif choice == '2':
            # Check if there are any menu items
            if not restaurant.get_menu_items():
                print("No menu items available.")

            else:
                print("\nMenu:")
                for index, item in enumerate(restaurant.get_menu_items(), start=1):
                    print(f"{index}. {item.get_name()} (${item.get_price()}) [{item.get_category()}]")

        elif choice == '3':
            # Check if there are any menu items
            if not restaurant.get_menu_items():
                print("No menu items available. Please add items first.")
            else:
                order_input = input("\nEnter item numbers for the order separated by commas (e.g., 1,2):")
                item_numbers = [int(num.strip()) for num in order_input.split(",") if num.strip().isdigit()]
                if not item_numbers:
                    print("Invalid input. Please enter valid item numbers.")
                else: 
                    # Create a new order
                    new_order = Order()
                    for item_number in item_numbers:
                        # Check if the item number is valid
                        # Assuming Restaurant.menu is a list of all menu items
                        if 1 <= item_number <= len(restaurant.get_menu_items()):
                            new_order.add_item(restaurant.get_menu_items()[item_number - 1])
                            
                        else:
                            print(f"Item number {item_number} is not valid.")

                    restaurant.set_order(new_order)
                    print("New order created successfully!")

        elif choice == '4':
            # Check if there are any orders
            if not restaurant.get_orders():
                print("No orders available.")
            else:
                for order in restaurant.get_orders():
                    print(f"\nOrder {restaurant.get_orders().index(order) + 1}:")
                    for item in order.get_items():
                        if isinstance(item, MenuItem):
                            print(f"- {item.get_name()} (${item.get_price()}) [{item.get_category()}]")
                    print(f"Total: ${order.total()}")
        else:
            print("\nInvalid choice. Please try again.")
        
        
        choice = input("\nWelcome to the Restaurant Management System!\nChoose an option:\n1. Add menu item\n2. View menu\n3. Create new order\n4. List all orders\n5. Exit\n")
