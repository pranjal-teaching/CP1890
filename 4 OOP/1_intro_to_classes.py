# Describes the idea/concept of a house
from address import Address

class House:
    """
    # ATTRIBUTES
    data items: address(str), #_of_rooms(int), price(float), is_for_sale(bool)
    # METHODS
    behaviour: open_garage_door(), mow_lawn(), clean_up()
    """
    def __init__(self, street_address:Address, rooms_count, house_price:float, is_for_sale):
        assert isinstance(street_address, Address), "must be of type Address"
        self.address = street_address
        self.rooms = rooms_count
        self.price = house_price
        self.for_sale = is_for_sale

    def open_garage_door(self):
        print('opening garage door', self.address)



work_address = Address(street="1 PPD",
                       city="St. John's",
                       province='NL',
                       postal_code="A1A 1A1")

my_house = House(street_address=work_address, rooms_count=10, house_price=300000, is_for_sale=True)
# my_shed = House(street_address='2 PPD', rooms_count=0, house_price=20000, is_for_sale=False)

print(my_house.price)
# print(my_shed.price)

my_house.open_garage_door()
# my_shed.open_garage_door()