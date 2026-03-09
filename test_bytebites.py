import pytest
from models import Customer, MenuItem, Menu, Order


# --- Fixtures ---

@pytest.fixture
def sample_menu():
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 9.99, "Burgers", 4.8))
    menu.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.2))
    menu.add_item(MenuItem("Lemonade", 3.49, "Drinks", 4.5))
    menu.add_item(MenuItem("Chocolate Cake", 5.49, "Desserts", 4.6))
    return menu

@pytest.fixture
def sample_customer():
    return Customer("Mofe")

@pytest.fixture
def sample_order(sample_customer):
    order = Order(sample_customer)
    order.add_item(MenuItem("Spicy Burger", 9.99, "Burgers", 4.8))
    order.add_item(MenuItem("Large Soda", 2.99, "Drinks", 4.2))
    return order


# --- Order Total Tests ---

def test_order_total_with_multiple_items(sample_order):
    """A burger ($9.99) and soda ($2.99) should total $12.98."""
    assert sample_order.compute_total() == pytest.approx(12.98)

def test_order_total_is_zero_when_empty(sample_customer):
    """An order with no items should return a total of $0."""
    order = Order(sample_customer)
    assert order.compute_total() == 0


# --- Menu Filter Tests ---

def test_filter_returns_only_matching_category(sample_menu):
    """Filtering by 'Drinks' should return only drink items."""
    drinks = sample_menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)

def test_filter_is_case_insensitive(sample_menu):
    """Filtering should work regardless of case (e.g. 'drinks' vs 'Drinks')."""
    drinks = sample_menu.filter_by_category("drinks")
    assert len(drinks) == 2

def test_filter_returns_empty_for_unknown_category(sample_menu):
    """Filtering by a category that doesn't exist should return an empty list."""
    result = sample_menu.filter_by_category("Sushi")
    assert result == []


# --- Sorting Tests ---

def test_sort_by_popularity_descending(sample_menu):
    """Most popular item should come first when sorted descending."""
    sorted_items = sample_menu.sort_by_popularity(descending=True)
    assert sorted_items[0].name == "Spicy Burger"  # popularity 4.8

def test_sort_by_price_ascending(sample_menu):
    """Cheapest item should come first when sorted ascending."""
    sorted_items = sample_menu.sort_by_price(descending=False)
    assert sorted_items[0].name == "Large Soda"  # price 2.99


# --- Customer Tests ---

def test_customer_is_real_user(sample_customer):
    """A customer with a name should be verified as a real user."""
    assert sample_customer.is_real_user() is True

def test_customer_with_no_name_is_not_real():
    """A customer with an empty name should not be a real user."""
    c = Customer("")
    assert c.is_real_user() is False

def test_customer_purchase_history(sample_customer, sample_order):
    """Adding an order to history should be stored on the customer."""
    sample_customer.add_to_history(sample_order)
    assert len(sample_customer.purchase_history) == 1