# ---------------- Creating Product Class --------------------- #

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
    self.discountedPrice = ((100-discount)/100)*price

    # Actions to execute
    Product.all.append(self) # Appending Product to list everytime a particular instance is instantiated

  def calculate_total_price(self):
    return self.discountedPrice * self.quantity

  # Reformat the Product.all string
  def __repr__(self):
    return f"Product('{self.name}', {self.price}, {self.quantity})"

# --------------------------------------------------------------- #


# Scanning individual items
product1 = Product("Apple", 4.0, 2)
product2 = Product("Milk", 9.41, 1)
product3 = Product("Egg", 5.25, 1)
product4 = Product("Cola", 12.10, 2)
product5 = Product("Cola Zero", 11.15, 1)

# Saving items to an array
allProducts = Product.all
print(allProducts)




# --------------  Function 1: Calculate total price  --------- #
def calculate_total_price():
  total_price = 0
  for product in allProducts:
    subtotal = product.calculate_total_price()
    total_price += subtotal
  return total_price

# calculate_total_price()



# ---------------  Function 2: Cancel Product COMPLETELY from the order ------------ #
def cancel_order(name):
  index_to_delete = 0
  for index, product in enumerate (allProducts):
    if product.name == name:
      index_to_delete = index
      break
  del allProducts[index_to_delete]

# cancel_order("Milk")



# Function 2b: Increment Quantity of Product
def increase_quantity(name, increment):
  for product in allProducts:
    if product.name == name:
      product.quantity += increment
      break

# increase_quantity("Apple", 2)



# Function 2c: Decrement Quantity of Product
def decrease_quantity(name, decrement):
  for product in allProducts:
    if product.name == name:
      if product.quantity > decrement:
          product.quantity -= decrement
      else: # In case decrement count is more than the quantity of the product
          print("Cannot decrement to less than 0. Use the function cancel_order if you want to remove the order instead")

# decrease_quantity("Apple", 3)



# ------------ Function 3: Calculate Itemized Receipt Listing Product Name, Quantity, Price, Subtotal and Grand Total ----------- #
def print_receipt():
  for product in allProducts:
    if product.price == product.discountedPrice:
      print("Item name: " + product.name + " , QTY: " + str(product.quantity) + " , Price: $" + str(product.price) + " , Subtotal: $" + str(product.quantity*product.discountedPrice))

    else:
      print("Item name: " + product.name + " , QTY: " + str(product.quantity) + " , Original Price: $" + str(product.price) + " , Discount: " + str(round((product.price-product.discountedPrice)/product.price * 100)) + "%, Discounted Price: $" + str(product.discountedPrice) + " , Subtotal: $" + str(product.quantity*product.discountedPrice))
  
  print("Grand Total: $" + str(calculate_total_price()))
print_receipt()


# ------------- Function 4: Discount Products --------------- #
def discount_product(name, discount):
  for product in allProducts:
    if product.name == name:
      product.discountedPrice = ((100-discount)/100) * product.price

discount_product("Apple", 10)
print_receipt()


