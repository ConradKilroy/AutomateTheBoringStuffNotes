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




class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#note: Check out the code in the editor. We've defined a class, Customer, as well as a ReturningCustomer class that inherits 
#from Customer. Note that we don't define the display_cart method in the body of ReturningCustomer, but it will still have access 
#to that method via inheritance. Click Run to see for yourself!




#Inheritance is a tricky concept, so let's go through it step by step.
#Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.

#----------------
#Override Inheritance!
#Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent,
#but to override one or more of them.

class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!


############Calling overrided inheritance functions
#On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've overwritten a method 
#or attribute defined in that class' base class (also called a parent or superclass) that you actually need. 
#Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in super call.

#The syntax looks like this:

class Derived(Base):
  def m(self):
    return super(Derived, self).m()

#Where m() is a method from the base class.



