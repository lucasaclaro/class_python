# Os métodos getter e setter são uma forma de proteção para controlar a maneira como os dados são inseridos

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount (self, discount):
        self.price = self.price - (self.price * (discount / 100))

    # Getter
    @property
    def price(self):
        return self._price


    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))
        self._price = value


shirt_yellow = Product('Shirt', 'R$120')
shirt_yellow.discount(15)
print(f"Price: R$ {shirt_yellow.price}.")