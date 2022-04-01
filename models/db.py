import sqlite3
from tkinter import messagebox


class DB:
    def __init__(self, ws):
        self.ws = ws

    def show_error(self, type, msg):
        if type == 'Success':
            messagebox.showinfo(self.ws, msg)
        else:
            messagebox.showerror(self.ws, msg)

    def insert_user(self, name, password, email, phone):
        try:
            conn = sqlite3.connect('test.db')
            conn.execute(f"INSERT INTO USER (NAME,PHONE,EMAIL,PASSWORD) \
            VALUES ('{name}',{phone},'{email}','{password}' )")
            self.show_error('Success', 'User added successfully')
            print("User added successfully")
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
            self.show_error('Error', 'Some error occured')
            conn.rollback()
            conn.close()

    def check_if_exists(self, email, password):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.execute(
                f"SELECT NAME,ID FROM USER WHERE EMAIL = '{email}' AND PASSWORD = '{password}'")
            print("--->> ")
            # print(self.name)
            for row in cursor:
                self.name = row[0]
                self.ID = row[1]
                print(self.name)
                return True
            self.show_error('Error', 'Invalid Email or Password')
            return False
        except Exception as e:
            print(e)
            self.show_error('Error', 'Some error occured')
            return False

    def get_curr_user(self):
        return [self.name, self.ID]

    def update_name(self, name, id):
        try:
            conn = sqlite3.connect('test.db')
            conn.execute(f"UPDATE USER SET NAME = '{name}' WHERE ID = {id}")
            conn.commit()
            conn.close()
            self.show_error('Success', 'Name updated successfully')
        except Exception as e:
            print(e)
            self.show_error('Error', 'Some error occured')
            conn.rollback()
            conn.close()


def create_table():
    conn = sqlite3.connect('test.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS USER
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
        PHONE INTEGER,
        EMAIL TEXT,
        PASSWORD TEXT)''')
    conn.commit()
    conn.close()

    # show_error('Error', 'Some error occured')
