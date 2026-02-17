from expense_tracker.tracker import add_expense, total_expenses

def test_total():
    add_expense("Test", 10)
    assert total_expenses() >= 10
