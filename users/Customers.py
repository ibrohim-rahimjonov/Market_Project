from users.Store import Store, Store_baza


class Customers:
    def __init__(self,id1, name, age, address, phone,balance):
        self.id1 = id1
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.balance = balance
        self.basket = []   # basket for products
        self.type = "Customer"

    def view_basket(self):
        if not self.basket:
            print("Basket is empty")
        else:
            for idx, item in enumerate(self.basket, start=1):
                print(f"{idx}: {item.type} - ${item.price}")

    def add_to_basket(self, store):
        store.view_store()
        kod = int(input("Which item to add to basket (number): "))
        if 1 <= kod <= len(store.data):
            product = store.data[kod - 1]
            if product.quantity > 0:
                soni = int(input("How much kg do you want? - "))
                if soni <= product.quantity:
                    a = Store(product.type,product.price, soni)
                    self.basket.append(a)

                    print(f"\n=== {product.type} {product.quantity} added to basket ===")
                else:
                    print("\n=== Out of stock! ===")
            else:
                print("Out of stock!")

    def remove_from_basket(self):
        self.view_basket()
        kod = int(input("Which item to remove: "))
        if 1 <= kod <= len(self.basket):
            removed = self.basket.pop(kod - 1)

            print(f"{removed.type} removed from basket")

    def change_from_basket(self):
        self.view_basket()
        kod = input("Which product need to change ? ")
        for item in self.basket:
            if isinstance(item, Store) and item.type == kod :
                new_kg = int(input("How much kg you need? " ))
                item.quantity = new_kg
                print("=== The product has Changed ===")





    def buy_items(self, store, market):
        total = sum(item.price for item in self.basket)
        if total > self.balance:
            print("Not enough money!")
            return
        for j in self.basket:
            for item in store.data:
                if j.type == item.type:
                    item.quantity -= j.quantity


        self.balance -= total
        market.balance += total

        for item in self.basket:
            item.quantity -= 1
        self.basket.clear()
        print("===  Purchase successful  ===")



class Baza_customer:
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.data = []

    def add_baza(self, s):
        self.data.append(s)

    def add_customer(self):
        id1 = int(input("Enter an Id: "))
        name = input("Enter a name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        phone = input("Enter phone number: ")
        balance = input("Enter a balance: ")
        a = Customers(id1,name, age, address, phone, balance)
        self.data.append(a)

    def view_customers(self):
        count = 0
        for item in self.data:
            count += 1
            if isinstance(item, Customers):
                print(f'{count}:ID:** Name - {item.name} Age - {item.age} Address - {item.address} Phone - {item.phone} Balance - {item.balance}')

    def view_customers_(self):
        count = 0
        for item in self.data:
            count += 1
            if isinstance(item, Customers):
                print(f'{count}:ID:{item.id1} Name - {item.name} Age - {item.age} Address - {item.address} Phone - {item.phone} Balance - {item.balance}')

