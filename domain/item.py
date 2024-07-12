class Item:
    def __init__(self, id, name, price, category):
        self._id = id
        self._name = name
        self._price = price
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

class Dress(Item):
    def get_details(self):
        return f"Dress - Name: {self.name}, Price: {self.price}, Category: {self.category}"

class Shirt(Item):
    def get_details(self):
        return f"Shirt - Name: {self.name}, Price: {self.price}, Category: {self.category}"
