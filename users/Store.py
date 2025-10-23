class Store:
    def __init__(self,type,price,quantity):
        self.type = type
        self.price = price
        self.quantity = quantity


class Store_baza:
    def __init__(self,title,id):
        self.title = title
        self.id = id
        self.data = []


    def add(self,s):
        self.data.append(s)

    def view_store(self):
        count = 0
        for item in self.data:
            count += 1
            if isinstance(item, Store):
                print(f'{count}: Type: {item.type} - Price: ${item.price} - Quantity: {item.quantity} kg ')

    def add_item_store(self):
        type = input("Enter a type: ")
        price = input("Enter a price: ")
        quantity = input("Enter quantity of product: ")
        a = Store(type,price,quantity)
        self.data.append(a)

    def delete_item_store(self):
        kod = int(input("which item you want to delete "))
        count = 0
        for item in self.data:
            count += 1
            if isinstance(item,Store):
                if kod == count:
                    self.data.remove(item)
                    print(f'Type: {item.type} - Deleted Successfully!')

    def change_item_store(self):
        kod = input("Which item need to change: ")
        for item in self.data:
            if isinstance(item,Store) and item.type == kod:
                kod1 = input("What we need to change: ")
                if kod1 == "type":
                    new_type = input("Enter a new type: ")
                    item.type = new_type
                    print(f'Type:{item.type} - Updated')
                elif kod1 == 'price':
                    new_price = input("Enter a new price: ")
                    item.price = new_price
                    print(f'Type: {item.type} Price: {item.price} - Updated')
                elif kod1 == 'quantity':
                    new_quantity = input("Enter a new quantity: ")
                    item.quantity = new_quantity
                    print(f'Type: {item.type} Price: {item.price} Quantity: {item.quantity} - Updated')
            else:
                break






    # def korzinka(self,s):





#
# baza.view_store()
# baza.add_item_store()
# baza.delete_item_store()
# baza.view_store()
#












