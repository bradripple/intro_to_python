class BankAccount:
  def __init__(self, balance):
    self.balance = balance
    self.interest = .02

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if (amount > 0):
        self.balance -= amount
        return amount
    else:
        return False
    
  def accumulate_interest(self):
      self.balance = self.balance + self.balance * self.interest
      return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance):


