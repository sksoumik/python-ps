class CreditCard:
    def __init__(self, customer, account, bank, acnt, limit):
        self._customer = customer
        self._account = account
        self._bank = bank
        self._acnt = acnt  # account identifier
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit
