Assignment: Design and Implement a Restaurant Management System
You are required to design an object-oriented system for managing a restaurant. Your system should include
at least the following classes:
MenuItem: representing an individual menu item with a name, price, and category.
Order: representing a customer's order with a list of items and a method to calculate the total.
Restaurant: representing the restaurant with a menu and a record of placed orders.

UML Sketch:

+-------------+ +-----------+ +---------------+
| MenuItem | | Order | | Restaurant |
+-------------+ +-----------+ +---------------+
| - name | | - items[] | | - menu[] |
| - price | +-----------+ | - orders[] |
| - category | | +add_item()| +---------------+
+-------------+ | +total() | | +add_order() |
+-----------+ | +list_orders()|
+---------------+

Task: Based on the UML, implement the classes in Python using the principles of class definition, constructors,
data members, instance methods, encapsulation, and optionally static methods.
Additionally, create a separate main class or script that will serve as the entry point of your program. This
script should:
1. Instantiate a Restaurant object.
2. Interact with the user through the command line to perform the following:
Add new menu items (prompt the user for name, price, and category).
Display the current menu.
Create a new order (allow the user to select items by name).
Place the order into the restaurant's order list.
List all orders with total amounts.

Structure your code cleanly with comments explaining the logic and how it connects back to the concepts of
object-oriented programming.
Example Run:

Intro_OOP_Python.md 2025-05-09

2 / 11
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 1
Enter item name: Margherita Pizza
Enter item price: 8.5
Enter item category: Pizza
Menu item added successfully.
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 1
Enter item name: Caesar Salad
Enter item price: 6.0
Enter item category: Salad
Menu item added successfully.
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 2
Menu:
1. Margherita Pizza ($8.5) [Pizza]
2. Caesar Salad ($6.0) [Salad]
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 3
Enter item numbers for the order separated by commas (e.g., 1,2): 1,2
Order created and added successfully.

Intro_OOP_Python.md 2025-05-09

3 / 11
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 4
Orders:
Order 1:
- Margherita Pizza ($8.5)
- Caesar Salad ($6.0)
Total: $14.5
Welcome to the Restaurant Management System!
Choose an option:
1. Add menu item
2. View menu
3. Create new order
4. List all orders
5. Exit
> 5
Thank you for using the Restaurant Management System!
