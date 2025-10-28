from psycopg2 import connect
import psycopg2

class Data_Connect:
    def __init__(self,dbname,user,password,host='localhost',port = 5432):
        self.connection = psycopg2.connect(
            dbname = dbname,
            user = user,
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.connection.cursor()
        # self.cursor.close()

    def view_users(self):
            query = "SELECT * FROM Users ORDER BY user_id"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)


    def add_user(self,full_name,age,phone,address,fax):
        query = """
        INSERT INTO Users(full_name,age,phone,address,fax)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query,(full_name,age,phone,address,fax))
        self.connection.commit()

    def delete_user(self,user_id):
        query = """ DELETE FROM Users WHERE user_id = %s"""
        self.cursor.execute(query,(user_id,))
        self.connection.commit()
        print(f"User with ID {user_id} deleted successfully.")

    def search_user(self,user_id,phone):
        query = """SELECT * FROM Users WHERE user_id = %s OR phone = %s"""
        self.cursor.execute(query,(user_id,phone))
        self.connection.commit()
        result = self.cursor.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("No user found with that ID or phone.")

    def update_user(self, user_id, full_name=None,age=None,phone=None,address=None,fax=None):
        update = []
        values = []
        if full_name:
            update.append("full_name = %s")
            values.append(full_name)
        if age:
            update.append("age = %s")
            values.append(age)
        if phone:
            update.append("phone = %s")
            values.append(phone)
        if address:
            update.append("address = %s")
            values.append(address)
        if fax:
            update.append("fax = %s")
        if not update:
            print("No fields to update. ")
            return
        query = f"Update Users SET {','.join(update)} WHERE user_id = %s"
        values.append(user_id)

        self.cursor.execute(query, tuple(values))
        self.connection.commit()
        print("User information Updated. ")

class Sms_manager:
    def __init__(self,connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def send_message(self,sender_id,receiver_id,messages_text):
        """Here we add a message and send"""
        query = """
        INSERT INTO messages(sender_id, receiver_id,messages_text)
        VALUES(%s, %s, %s)
        """
        self.cursor.execute(query,(sender_id,receiver_id,messages_text))
        self.connection.commit()




connector  = Data_Connect('call_centre', 'n71', '123')
sms = Sms_manager(connector.connection)
def sms_menu(sms):
    while True:
        print("============ Sms manager ============")
        kod = input("1. Send a Message\n2. View a Message\n3. Delete a Message\n4. Exit ")
        if kod == '1':
            sender = input("Sender ID: ")
            receiver = input("Receiver ID: ")
            text = input("Message text: ")
            sms.send_message(sender, receiver, text)
            print("The message sent Successfully. ")
        if kod == '2':


def manager():
    while True:
        kod = input("1. View all Users\n2. Add a User\n3. Delete a user\n4. Search a user\n5. Update User\n6. Exit  ")
        if kod == '1':
            print('============== USERS ================')
            connector.view_users()
        elif kod == '2':
            print('============== Add User =============')
            full_name = input("Enter a name: ")
            age = input("Enter your age: ")
            phone = input("Enter your phone: ")
            address = input("Enter your address: ")
            fax = input("Enter your fax: ")
            connector.add_user(full_name, age, phone, address, fax)
        elif kod == '3':
            print("============== Delete User ============")
            user_id = input("Enter a user ID to delete: ")
            connector.delete_user(user_id)
        elif kod == '4':
            print("============= SEARCH PHONE ==============")
            kod1 = input("What do you need to search ?  \n1. User ID\n2. Phone")
            if kod1 == '1':
                user_id = input("Enter a User ID:  ")
                connector.search_user(user_id,None)
            elif kod1 == '2':
                phone = input("Enter a phone: ")
                connector.search_user(None, phone)
        elif kod == '5':
            print("============= UPDATE USER ==============")
            user_id = input("Enter the user ID to update: ")
            print("Leave blank any field you don’t want to change.")
            name = input("New full name: ")
            age = input("New age: ")
            phone = input("New phone: ")
            address = input("New address: ")
            fax = input("New fax: ")

            connector.update_user(
                user_id,
                full_name=name or None,
                age=age or None,
                phone=phone or None,
                address=address or None,
                fax=fax or None
            )
        elif kod == '6':
            sms_menu(sms)

        elif kod == '7':
            break

manager()