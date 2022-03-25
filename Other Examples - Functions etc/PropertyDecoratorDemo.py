class House:

   def __init__(self, price, color):
      self._price = price
      self._color = color

   def get_price(self):
      return self._price

   def set_price(self, x):
      self._price = x

H1 = House(30000,"red")
#print(H1.price) #note - remove protected or private modifier to show that this works
#print(H1.color)
H1.set_price(40000)
#print(H1.get_price())




class House2:

   def __init__(self, price):
      self._price = price

   @property
   def price(self):
      return self._price

   @price.setter
   def price(self, new_price):
      if new_price > 0 and isinstance(new_price, float):
         self._price = new_price
      else:
         print("Please enter a valid price")

   @price.deleter
   def price(self):
      del self._price

H2=House2(50000)

print(H2.price)