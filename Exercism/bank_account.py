'''
Simulate a bank account supporting opening/closing, withdrawals, and deposits
of money. Watch out for concurrent transactions!
A bank account can be accessed in multiple ways. Clients can make
deposits and withdrawals using the internet, mobile phones, etc. Shops
can charge against the account.
Create an account that can be accessed from multiple threads/processes
(terminology depends on your programming language).
It should be possible to close an account; operations against a closed
account must fail.
'''
from threading import RLock

class BankAccount(object):
    _lock = RLock()

    def __init__(self):
        BankAccount._balance = 0
        
    def open(self):
        BankAccount._open = True

    def deposit(self, amount):
        if amount >= 0:
            if BankAccount._open:
                with self._lock:
                    self._balance += amount
            elif not BankAccount._open:
                raise ValueError(f'Operation failed.')
        else:
            raise ValueError(f'cannot deposit negative amount.')
        
    def withdraw(self, amount):
        if amount >= 0:
            if BankAccount._open:
                if amount <= self._balance:
                    with self._lock:
                        self._balance -= amount
                else:
                    raise ValueError(f'cannot withdraw more than deposited.')
            elif not BankAccount._open:
                raise ValueError(f'Operation failed.')
        else:
            raise ValueError(f'cannot withdraw negative amount.')

    def get_balance(self):
        if BankAccount._open:
            with self._lock:
                return self._balance
        if not BankAccount._open:
            raise ValueError(f'Operation failed.')

    def close(self):
        BankAccount._open = False


