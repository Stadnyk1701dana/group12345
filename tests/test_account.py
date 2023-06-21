import pytest

from models import Account, AccountType

def test_balance(current_account):
    assert current_account.balance == 0

def test_account_take_money(current_account):
    current_account.balance = 4500
    current_account.withdraw_money(270)
    assert current_account.balance == 4230

def test_account_withdraw_not_enough_money(current_account):
    current_account.credit_allowed = False
    current_account.balance = 350
    current_account.withdraw_money(750)
    assert current_account.balance == 350

def test_account_withdraw_credit_allowed(current_account):
    current_account.credit_allowed = True
    current_account.balance = 500
    current_account.withdraw_money(800)
    assert current_account.balance == -300

def test_account_withdraw_enough_money(current_account):
    current_account.credit_allowed = False
    current_account.balance = 3790
    current_account.withdraw_money(2500)
    assert current_account.balance == 1290

def test_add_deposit_money(current_account):
    current_account.balance = 45000
    current_account.deposit_money(10000)
    assert current_account == 55000

