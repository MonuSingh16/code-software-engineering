from item import Item

class Phone(Item): # Inheritance from Item

    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0) -> None:
        # Call to super to have to access to all atrributes and methods
        super().__init__(
            name, price, quantity
        )        
        # Run validation to receive arguments
        #assert price >= 0, f"Price {price} is not greater than or equal to zero"
        #assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero"
        
        # Assign to self object
        #self.name = name
        #self.price = price
        #self.quantity = quantity
        self.broken_phones = broken_phones
        #print(f'An instance created: {name}')