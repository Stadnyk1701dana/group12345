from models import AccountType

import pytest
from faker import Faker

from models import Account, AccountType

@pytest.fixture(scope='session')
def new_current_account():
    current_account = Account(
        balance = 1000,
        account_type= 0
    )
    yield current_account
    del current_account

@pytest.fixture(scope='session')
def new_deposit_account():
    deposit_account = Account(
        balance = 10000,
        account_type= 1
    )
    yield deposit_account
    del deposit_account