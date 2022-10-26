import pytest
from main import Product
from main import calculate_total_price
from main import cancel_order
from main import print_receipt
from main import discount_product

# Scanning individual items
product1 = Product("Apple", 4.0, 2)
product2 = Product("Milk", 9.41, 1)
product3 = Product("Egg", 5.25, 1)
product4 = Product("Cola", 12.10, 2)
product5 = Product("Cola Zero", 11.15, 1)


def test_calculate_total_price():
  assert calculate_total_price() == 58.01

def test_cancel_order():
  assert cancel_order("Milk")

def test_print_receipt():
  assert print_receipt()

def test_discount_product():
  assert discount_product("Apple", 10)
