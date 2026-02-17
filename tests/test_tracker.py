from expense_tracker.tracker import add_expense, total_expenses

def test_total():
    add_expense("Test", 10)
    assert total_expenses() >= 10
from expense_tracker.tracker import list_expenses

def test_list_returns_list():
    assert isinstance(list_expenses(), list)
# Stores expense records
# Adds new expense
# Returns total amount
