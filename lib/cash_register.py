#!/usr/bin/env python3

class CashRegister:
  pass
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, name, price, quantity=1):
    item_cost = price * quantity
    self.total += item_cost
    for _ in range(quantity):
      self.items.append(name)  # Append only the item name
      self.transactions.append({"name": name, "quantity": quantity, "price": price})
        
  def apply_discount(self):
    if self.discount:
      discount_amount = int(self.total * (self.discount / 100))
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if not self.transactions:
      return "There are no transactions to void."
        
    last_transaction = self.transactions.pop()
    for _ in range(last_transaction["quantity"]):
      self.items.pop()
         
    self.total -= last_transaction["price"] * last_transaction["quantity"]

# Example usage:
register = CashRegister(discount=10)
register.add_item("Apple", 1.5, 3)
print(register.total)  # Output: 4.5
register.apply_discount()  # Output: After the discount, the total comes to $4.05
print(register.total)  # Output: 4.05
register.void_last_transaction()
print(register.total)  # Output: 0.45



