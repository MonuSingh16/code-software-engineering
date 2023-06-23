from item import Item

item1 = Item("MyItem", 750, 2)
item1._name = "Other Item" # Will throw erro
print(item1.name)


# item1.name = "OtherItem" # We should have error when we try to instantiate or change attribute again
# print(item1.read_only_name)
# item1.read_only_name = 'BBB' # Will trhow error


#phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(Phone.all)
#print(Item.all)


#phone2 = Phone("jscPhonev11", 700, 10, 1)

#print(Item.is_integer(7.0))

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

