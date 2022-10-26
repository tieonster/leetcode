class Product:
  all = []

  def __init__(self, name: str, price: float, quantity: int, discount=0):
    # Run validations to the received arguments
    assert price >= 0, "Price " + str(price) + " is not greater than or equal to zero!"
    assert quantity >= 0, "Quantity " + str(quantity) + " is not greater than or equal to zero!"

    # Assign to self object
    self.name = name
    self.price = price
    self.quantity = quantity
    self.discountedPrice = round((100-discount)/100)*price

    # Actions to execute
    Product.all.append(self) # Appending Product to list everytime a particular instance is instantiated

  def calculate_price(self):
    return self.discountedPrice * self.quantity

  # Reformat the Product.all string
  def __repr__(self):
    return f"Product('{self.name}', {self.price}, {self.quantity}, {self.discountedPrice})"

def calculate_total_price():
  total_price = 0
  for product in Product.all:
    subtotal = product.calculate_price()
    total_price += subtotal
  return total_price

def cancel_order(name):
  index_to_delete = 0
  for index, product in enumerate (Product.all):
    if product.name == name:
      index_to_delete = index
      break
  del Product.all[index_to_delete]
  print (Product.all)

def print_receipt():
  for product in Product.all:
    if product.price == product.discountedPrice:
      print("Item name: " + product.name + " , QTY: " + str(product.quantity) + " , Price: $" + str(product.price) + " , Subtotal: $" + str(product.quantity*product.discountedPrice))

    else:
      print("Item name: " + product.name + " , QTY: " + str(product.quantity) + " , Original Price: $" + str(product.price) + " , Discount: " + str(round((product.price-product.discountedPrice)/product.price * 100)) + "%, Discounted Price: $" + str(product.discountedPrice) + " , Subtotal: $" + str(product.quantity*product.discountedPrice))
  
  print("Grand Total: $" + str(calculate_total_price()))

def discount_product(name, discount):
  for product in Product.all:
    if product.name == name:
      product.discountedPrice = ((100-discount)/100) * product.price
  print_receipt()