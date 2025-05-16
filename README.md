# 🍽️ Restaurant Management System (OOP in Python)

This project is a simple **object-oriented restaurant management system** implemented in Python. It demonstrates the use of classes, encapsulation, instance methods, and object interactions to simulate basic operations in a restaurant setting.

---

## 📌 Features

* Add new menu items (name, price, category)
* Display current menu
* Create and place customer orders
* View all placed orders with total cost

---

## 🧱 Class Design (UML Overview)

```plaintext
+-------------+   +------------+    +---------------+
| MenuItem    |   |   Order    |    |   Restaurant  |
+-------------+   +------------+    +---------------+
| - name      |   | - items[]  |    | - menu[]      |
| - price     |   +------------+    | - orders[]    |
| - category  |   | +add_item()|    +---------------+
+-------------+   | +total()   |    | +add_order()  |
                  +------------+    | +list_orders()|
                                    +---------------+
```

---

## 🧠 Object-Oriented Concepts Used

* **Classes & Objects**
* **Constructors (`__init__`)**
* **Instance Methods**
* **Encapsulation**
* **Lists as Aggregates**
* (Optional) **Static/Class Methods**

---

## 🗂️ Class Breakdown

### `MenuItem`

Represents a single item on the menu.

* Attributes: `name`, `price`, `category`
* Methods: Getters/Setters if needed

### `Order`

Represents a customer's order.

* Attributes: List of `MenuItem` objects
* Methods: `add_item()`, `total()`

### `Restaurant`

Represents the restaurant and handles operations.

* Attributes: `menu` (list of `MenuItem`s), `orders` (list of `Order`s)
* Methods: `add_order()`, `list_orders()`, etc.

---

## 🖥️ Example CLI Interaction

```
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

> 1
Enter item name: Caesar Salad
Enter item price: 6.0
Enter item category: Salad
Menu item added successfully.

> 2
Menu:
1. Margherita Pizza ($8.5) [Pizza]
2. Caesar Salad ($6.0) [Salad]

> 3
Enter item numbers for the order separated by commas (e.g., 1,2): 1,2
Order created and added successfully.

> 4
Orders:
Order 1:
- Margherita Pizza ($8.5)
- Caesar Salad ($6.0)
Total: $14.5

> 5
Thank you for using the Restaurant Management System!
```

---

## 🛠️ Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/restaurant-management-system.git
   cd restaurant-management-system
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

---

## 📚 Educational Purpose

This project is ideal for **beginners learning Object-Oriented Programming in Python**. It connects theory with practical use, helping users grasp real-world class interactions and program structure.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
