import csv

class Item:
    
    pay_rate = 0.8 # Class attribute. The pay rate after 20% dicount
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        # Run validation to receive arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        #print(f'An instance created: {name}')

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
         # This a method, The first parameter is object itself
         # We have now access to attributes from self 
         return self.price * self.quantity
    
    def apply_discount(self):
        # Updating the price attribute with old price and multiplied with pay rate
        # Access the pay rate from the class level, if not then use instance level
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        # This method should no be called from instance
        # Here the class reference is passed as parameter
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero

        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

print(Item.is_integer(7.0))

#Item.instantiate_from_csv() # Instantiate a class method
#print(Item.all)

#print(Item.all)
#for instance in Item.all:
#    print(instance.name)



#item1 = Item('Phone',100, 5) # Instance of Class
#item2 = Item('Laptop', 1000, 3)
#item2.has_numpad = False


#print(item1.apply_discount(), item1.price)
#item2.pay_rate = 0.7 # Will find at the instance level here
#print(item2.apply_discount(), item2.price)


#print(Item.__dict__) # All the attributes of the class level
#print(item1.__dict__) # All the attributes at instance level

#print(Item.pay_rate) # Acces the class attribute with class
#print(item1.pay_rate) # Acces the class attribute with class, That were not fpund at instance level, but at the class level

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

# print(item1.name)
# print(item2.name)

