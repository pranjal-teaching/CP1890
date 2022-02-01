class Address:
    def __init__(self, street:str, city, province, postal_code, country="Canada"):
        self.street = street
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.country = country

    # example method
    def to_string(self):
        return f'{self.street} {self.city}, ' \
               f'{self.province}, {self.postal_code} {self.country}'


# Create work address object
work_address = Address(street="1 PPD",
                       city="St. John's",
                       province='NL',
                       postal_code="A1A 1A1")

# my home address
home_address = Address(street="101 random st",
                       city="St. John's",
                       province='NL',
                       postal_code="A1A 1A1",
                       country='India')

print(work_address.to_string())
