import re as Regex
from tkinter import messagebox


class Validate_Data:
    def __init__(self, ws):
        self.ws = ws

    def show_error(self, type, msg):
        if type == 'Success':
            messagebox.showinfo(self.ws, msg)
        else:
            messagebox.showerror(self.ws, msg)

    def validate_data(self, name, email, password, phone, pass_again):
        name_re = r'[a-zA-z]\b'
        email_re = r'[a-zA-Z0-9]+@+[a-zA-Z]+.+[a-zA-Z]\b'
        if len(password) < 8:
            self.show_error('Error', 'Password is not valid')
            return False
        if password != pass_again:
            self.show_error('Error', 'Password is not matched')
            return False
        phone_re = r'^[0-9]{10}$'

        if Regex.search(name_re, name) is None:
            self.show_error('Error', 'Name is not valid')
            return False
        if Regex.search(email_re, email) is None:
            self.show_error('Error', 'Email is not valid')
            return False

        if Regex.search(phone_re, phone) is None:
            self.show_error('Error', 'Phone is not valid')
            return False
        return True
