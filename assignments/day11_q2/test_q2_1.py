import pytest

# ✅ Application Logic (End-to-End Flow)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance


# ✅ Functional Tests (End-to-End Behavior)

def test_end_to_end_deposit_withdraw():
    acc = BankAccount(100)

    acc.deposit(50)
    acc.withdraw(30)

    assert acc.balance == 130
    


def test_invalid_deposit():
    acc = BankAccount()

    with pytest.raises(ValueError):
        acc.deposit(-10)


def test_over_withdraw():
    acc = BankAccount(50)

    with pytest.raises(ValueError):
        acc.withdraw(100)
