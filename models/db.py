from tkinter import messagebox
import psycopg2
from env import ENV

USERNAME = ENV().get('.env', 'DB_USER')
PASSWORD = ENV().get('.env', 'DB_Pass')


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
            conn = psycopg2.connect(
                user=USERNAME, password=PASSWORD, port="5433", database="form_tkinter")
            cur = conn.cursor()

            cur.execute(f"INSERT INTO userform (NAME,PHONE,EMAIL,PASSWORD) \
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
            conn = psycopg2.connect(
                user=USERNAME, password=PASSWORD, port="5433", database="form_tkinter")
            cur = conn.cursor()

            cursor = cur.execute(
                f"SELECT NAME,ID FROM userform WHERE EMAIL = '{email}' AND PASSWORD = '{password}'")
            print("--->> ")
            # print(self.name)
            cursor = cur.fetchone()
            print(cursor)
            if cursor is None:
                return False
            else:
                self.name = cursor[0]
                self.ID = cursor[1]
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
            conn = psycopg2.connect(
                user=USERNAME, password=PASSWORD, port="5433", database="form_tkinter")
            cur = conn.cursor()

            cur.execute(f"UPDATE userform SET NAME = '{name}' WHERE ID = {id}")
            conn.commit()
            conn.close()
            self.show_error('Success', 'Name updated successfully')
        except Exception as e:
            print(e)
            self.show_error('Error', 'Some error occured')
            conn.rollback()
            conn.close()


def create_table():
    try:
        conn = psycopg2.connect(
            user=USERNAME, password=PASSWORD, port="5433", database="form_tkinter")
        cur = conn.cursor()
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS userform (ID SERIAL PRIMARY KEY,NAME TEXT,PHONE INTEGER,EMAIL TEXT,PASSWORD TEXT); ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        messagebox.showerror('Error', 'Some error occured')
