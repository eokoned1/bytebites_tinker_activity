# ByteBites Backend Models
# Four core classes:
# 1. Customer   - stores name and purchase history
# 2. MenuItem   - stores name, price, category, and popularity rating
# 3. Menu       - holds all MenuItems, supports filtering and sorting
# 4. Order      - groups selected items and computes total cost


class Customer:
    """Represents a ByteBites app user."""

    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []  # list of past Order objects

    def add_to_history(self, order):
        """Record a completed order in the customer's purchase history."""
        self.purchase_history.append(order)

    def is_real_user(self):
        """Return True if the customer has a name."""
        return bool(self.name)

    def __repr__(self):
        return f"Customer(name={self.name!r}, orders={len(self.purchase_history)})"


class MenuItem:
    """Represents a single food or drink item on the ByteBites menu."""

    def __init__(self, name: str, price: float, category: str, popularity: float):
        self.name = name
        self.price = price          # e.g. 8.99
        self.category = category    # e.g. "Burgers", "Drinks", "Desserts"
        self.popularity = popularity  # rating out of 5.0

    def __repr__(self):
        return (
            f"MenuItem(name={self.name!r}, price={self.price}, "
            f"category={self.category!r}, popularity={self.popularity})"
        )


class Menu:
    """Holds all available MenuItems and supports filtering and sorting."""

    def __init__(self):
        self.items = []  # list of MenuItem objects

    def add_item(self, item: MenuItem):
        """Add a MenuItem to the menu."""
        self.items.append(item)

    def filter_by_category(self, category: str):
        """Return a list of MenuItems that match the given category."""
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self, descending: bool = True):
        """Return items sorted by popularity rating."""
        return sorted(self.items, key=lambda item: item.popularity, reverse=descending)

    def sort_by_price(self, descending: bool = False):
        """Return items sorted by price."""
        return sorted(self.items, key=lambda item: item.price, reverse=descending)

    def __repr__(self):
        return f"Menu(items={len(self.items)})"


class Order:
    """Represents a single transaction grouping selected items."""

    def __init__(self, customer: Customer):
        self.customer = customer
        self.items = []  # list of MenuItem objects

    def add_item(self, item: MenuItem):
        """Add a MenuItem to the order."""
        self.items.append(item)

    def compute_total(self):
        """Return the total cost of all items in the order."""
        return sum(item.price for item in self.items)

    def __repr__(self):
        return (
            f"Order(customer={self.customer.name!r}, "
            f"items={len(self.items)}, total={self.compute_total():.2f})"
        )


# --- Manual check ---
if __name__ == "__main__":
    # Build a menu
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 9.99, "Burgers", 4.8))
    menu.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.2))
    menu.add_item(MenuItem("Chocolate Cake", 5.49, "Desserts", 4.6))
    menu.add_item(MenuItem("Lemonade", 3.49, "Drinks", 4.5))

    # Filter by category
    print("Drinks:", menu.filter_by_category("Drinks"))

    # Sort by popularity
    print("By popularity:", menu.sort_by_popularity())

    # Create a customer and place an order
    customer = Customer("Mofe")
    order = Order(customer)
    order.add_item(MenuItem("Spicy Burger", 9.99, "Burgers", 4.8))
    order.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.2))

    print("Order total:", order.compute_total())
    print(order)

    customer.add_to_history(order)
    print(customer)