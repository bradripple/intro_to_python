class BankAccount():
    # constructor (instance method)
  def __init__(self, kind):
    self.kind = kind
    self.balance = 0
    self.overdraft_fees = 0

    # identifier (instance method)
  def __str__(self):
      return f"This is a {self.kind} account"

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.amount -= amount
    if (self.amount < 0):
      self.overdraft_fees += 20
    return amount

rome_account = BankAccount('checking')
print(rome_account)

print(rome_account.balance)