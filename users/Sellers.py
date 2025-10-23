class Seller:
    def __init__(self, id1, name, age, phone):
        self.id1 = id1
        self.name = name
        self.age = age
        self.phone = phone

    def info(self):
        return f'ID:{self.id1} Name: {self.name} Age: {self.age} Phone: {self.phone}'


class  Seller_baza:
    def __init__(self,title,id):
        self.title = title
        self.id = id
        self.data = []
        self.managers = []


    def add(self,s):
        self.data.append(s)

    def add_seller(self):
        id1 = input("Enter an ID: ")
        name = input("Enter a name: ")
        age  = input("Enter your age: ")
        phone = input("Enter a phone: ")
        a = Seller(id1, name, age, phone)


        self.data.append(a)


    def view_seller(self):
        if not self.data:
            print("There is no Seller.")
        else:
            for item in self.data:
              print(f'ID:{item.id1} Name: {item.name} Age: {item.age} Phone: {item.phone}')


    def delete_seller(self):
        delete = input("Enter a customer's name: ")
        for item in self.data:
            if isinstance(item, Seller) and item.name == delete:
                print(f'ID: {item.id1} Name: {item.name} Age: {item.age} Phone: {item.phone}')
                self.data.remove(item)
                print(f'{item.name} = Deleted Successfully ! ')

    def change_info(self):
        kod = int(input("Enter your ID: "))
        for item in self.data:
            if isinstance(item, Seller) and item.id1 == kod :
                info = input("What do you want to change: \nId / Name / Age / Phone : ")
                if info == "id":
                    new_id = input("Enter a new ID: ")
                    item.id1 = new_id
                    print("===== The ID updated =====")
                    break
                if info == "name":
                    new_name = input("Enter a new Name: ")
                    item.name = new_name
                    print("===== The Name updated =====")
                    break
                elif info == "age":
                    new_age = input('Enter a new Age: ')
                    item.age = new_age
                    print("===== The Age updated =====")
                    break
                elif info == "phone":
                    new_phone = input("Enter a new phone: ")
                    item.phone = new_phone
                    print("===== The Phone updated =====")
                    break
        else:
                print("Enter a valid ID !!! ")




a = Seller_baza("awd",12)
seller = Seller(12,"Ali",25,'12121212')
seller1 = Seller(12,"Ali",25,'12121212')
seller2 = Seller(12,"Ali",25,'12121212')
seller3 = Seller(12,"Ali",25,'12121212')
# a = [seller,seller1,seller2,seller3]

a.add(seller1)
a.data.append(seller1)
a.add(seller2)
a.add(seller3)

# a.view_seller()
# Seller_baza.add_seller(seller1)












