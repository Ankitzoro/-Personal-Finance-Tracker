import json
from datetime import datetime

# File to store transactions
FILE_NAME = "transactions.json"

# Load existing transactions from file
def load_transactions():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save transactions to file
def save_transactions(transactions):
    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)

# Add a new transaction
def add_transaction(amount, category, transaction_type):
    transactions = load_transactions()
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "category": category,
        "type": transaction_type,
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print(f"✅ Transaction Added: {transaction}")

# Generate financial summary
def generate_summary():
    transactions = load_transactions()
    summary = {"Income": 0, "Expenses": 0, "Categories": {}}
    for transaction in transactions:
        amount = transaction["amount"]
        category = transaction["category"]
        t_type = transaction["type"]
        if t_type == "Income":
            summary["Income"] += amount
        else:
            summary["Expenses"] += amount
            summary["Categories"][category] = summary["Categories"].get(category, 0) + amount
    print("\n📊 Financial Summary:")
    print(f"Total Income: Rs.{summary['Income']}")
    print(f"Total Expenses: Rs.{summary['Expenses']}")
    print("Expenses by Category:")
    for category, expense in summary["Categories"].items():
        print(f" - {category}: Rs.{expense}")

# Filter expenses by category
def filter_expenses_by_category(category):
    transactions = load_transactions()
    total = sum(
        t["amount"] for t in transactions if t["type"] == "Expense" and t["category"] == category
    )
    return f"Total expenditure on {category}: Rs.{total}"

# Budget limits
budget_limits = {"Food": 5000, "Transport": 3000}

# Check budget
def check_budget(category, amount):
    if category in budget_limits:
        total_spent = sum(
            t["amount"] for t in load_transactions() if t["type"] == "Expense" and t["category"] == category
        )
        if total_spent + amount > budget_limits[category]:
            return f"⚠ Alert! Spending limit exceeded for {category}."
    return "✅ Transaction within budget."

# Valid categories
valid_categories = ["Food", "Rent", "Transport", "Shopping", "Utilities"]

# Validate category
def validate_category(category):
    try:
        if category not in valid_categories:
            raise ValueError("🚫 Invalid category. Please choose from the predefined list.")
        return "✅ Valid category."
    except ValueError as e:
        return str(e)

# User data
users_data = {}

# Add user
def add_user(user_id, name):
    users_data[user_id] = {"name": name, "transactions": []}
    print(f"✅ User {name} added successfully!")

# Example Test Cases
add_transaction(50000, "Salary", "Income")  # Adding Income
add_transaction(2000, "Food", "Expense")  # Adding Expense
add_transaction(1000, "Transport", "Expense")  # Adding Expense
generate_summary()
print(filter_expenses_by_category("Food"))
print(filter_expenses_by_category("Transport"))
print(check_budget("Food", 4000))
print(check_budget("Transport", 2000))
print(validate_category("Food"))
print(validate_category("Entertainment"))
add_user("U001", "Alice")
print(users_data)
