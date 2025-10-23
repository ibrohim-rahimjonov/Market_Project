from users.Sellers import *
from users.Store import *
from users.Customers import *
def square(width, height, text):
    print("*" * width)

    text_length = len(text)
    side_padding = (width - text_length - 2) // 2

    for i in range(height - 2):
        if i == (height - 2) // 2:
            print("* " + " " * side_padding + text + " " * (width - text_length - 2 - side_padding) + "*")
        else:
            print("*" + " " * (width - 2) + "*")

    print("*" * width)

class SuperMarket:
    def __init__(self):
        self.store = Store_baza("Store", 1)
        self.sellers = Seller_baza("Sellers", 2)
        self.customers = Baza_customer("Customers", 3)
        self.balance = 0   # supermarket money

    # ---------------- SELLER MENU ----------------
    def seller_menu(self):
        while True:
            square(30,5,"SEller Menu ")
            kod = input("1: View Store\n2: Add Item\n3: Delete Item\n4: Change Item\n"
                        "5: View Balance\n6: Add Customer\n7: View Customers\n8: Delete Customer\n9: View Sellers\n10: Exit\n")
            if kod == "1":
                self.store.view_store()
            elif kod == "2":
                self.store.add_item_store()
            elif kod == "3":
                self.store.delete_item_store()
            elif kod == "4":
                self.store.change_item_store()
            elif kod == "5":
                print(f"Super Market Balance: ${self.balance}")
            elif kod == "6":
                self.customers.add_customer()
            elif kod == "7":
                self.customers.view_customers_()
            elif kod == "8":
                self.customers.delete_customer()
            elif kod == "10":
                break
            elif kod =="9":
                square(30,5,"Sellers")
                self.sellers.view_seller()

    # ---------------- CUSTOMER MENU ----------------
    def customer_menu(self, customer: Customers):
        square(30, 5, "== WELCOME ==")

        while True:
            print(f"\n-*-*-{customer.name} -*-*- Balance: ${customer.balance}")
            kod = input("1: View Store\n2: Add to Basket\n3: Remove from Basket\n4: View Basket\n5: Change Product \n6: Buy\n7: Exit\n")
            if kod == "1":
                self.store.view_store()
            elif kod == "2":
                customer.add_to_basket(self.store)
            elif kod == "3":
                customer.remove_from_basket()
            elif kod == "4":
                customer.view_basket()
            elif kod == '5':
                customer.change_from_basket()
            elif kod == "6":
                customer.buy_items(self.store, self)

            elif kod == "7":
                break

    # ---------------- MAIN MENU ----------------
    def main_menu(self):
        while True:
            square(30,5,"=== Super Market ===")
            kod = input("1: Customer Login\n2: Manager\n3: Exit\n")
            if kod == "1":
                self.customers.view_customers()
                num = int(input("Enter a costumer ID: "))
                customer = None
                for item in market.customers.data:
                    if item.id1 == num:
                        customer = item
                        break

                if customer:
                     self.customer_menu(customer)

                else:
                        print("Invalid customer!")
            elif kod == "2":
                self.seller_menu()
            elif kod == "3":
                break


# -------------------- Run Program
if __name__ == "__main__":
    market = SuperMarket()

    # seller1 = Seller(12, "Ali", 25, '12121212')
    market.store.add(Store("Apple", 5, 10))
    market.store.add(Store("Banana", 3, 20))
    market.store.add(Store("Peach", 2, 40))
    market.store.add(Store("Water", 1, 15))
    market.sellers.add(Seller(1, "Ali", 25, "9121212"))
    market.sellers.add(Seller(2, "Vali", 30, "9989090"))
    market.sellers.add(Seller(2, "ali", 23, "9989090"))

    market.customers.add_baza(Customers(11,"Ali", 23, "Tashkent", "9121212", 500))
    market.customers.add_baza(Customers(12,"Vali", 30, "Samarkand", "9989090", 250))

    market.main_menu()
