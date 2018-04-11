#Lesson source
#https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes/exercises/its-not-all-animals-and-fruits

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

#Create an instance of ShoppingCart called my_cart.
#Initialize it with any values you like, then use the add_item method to add an item to your cart.

my_cart = ShoppingCart("Ravin")

my_cart.add_item("Bananas", 3.5)

print my_cart.items_in_cart
