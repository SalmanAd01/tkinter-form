from tkinter import *
from tkinter import messagebox
from models import *
from models.db import DB
from public.validation import Validate_Data
from view.Dashboard import Dashboard


class Home:
    def __init__(self, ws):
        self.ws = ws

    def display(self):

        self.ws.geometry("940x500")
        Vd = Validate_Data(self.ws)
        db = DB(self.ws)
        f = ('Times', 14)

        def store_info():
            username = name_input.get()
            useremail = email_input.get()
            userphone = phone_input.get()
            userpassword = password_input.get()
            pass_again = pwd_again.get()
            if Vd.validate_data(username, useremail, userpassword, userphone, pass_again):
                try:
                    db.insert_user(username, userpassword,
                                   useremail, userphone)
                    print("User added successfully")
                except Exception as e:
                    print("--->>", e)
                    messagebox.showerror(self.ws, 'Some error occured')
            else:
                print("Not Validate")

        def login_btn():
            login_email = email_tf.get()
            login_password = pwd_tf.get()
            print(login_email, login_password)
            if db.check_if_exists(login_email, login_password) is True:
                print("Login Success")
                cur_user_info = db.get_curr_user()
                Dashboard(self.ws, cur_user_info[0],
                          cur_user_info[1]).display()
            else:
                print("Login Failed")

        # widgets
        left_frame = Frame(
            self.ws,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=10,
            pady=10
        )

        Label(
            left_frame,
            text="Enter Email",
            bg='#CCCCCC',
            font=f).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            left_frame,
            text="Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=1, column=0, pady=10)

        email_tf = Entry(
            left_frame,
            font=f
        )
        pwd_tf = Entry(
            left_frame,
            font=f,
            show='*'
        )
        login_btn = Button(
            left_frame,
            width=15,
            text='Login',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=login_btn
        )

        right_frame = Frame(
            self.ws,
            bd=2,
            bg='#CCCCCC',
            relief=SOLID,
            padx=10,
            pady=10
        )

        Label(
            right_frame,
            text="Enter Name",
            bg='#CCCCCC',
            font=f
        ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Email",
            bg='#CCCCCC',
            font=f
        ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Contact Number",
            bg='#CCCCCC',
            font=f
        ).grid(row=2, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=5, column=0, sticky=W, pady=10)

        Label(
            right_frame,
            text="Re-Enter Password",
            bg='#CCCCCC',
            font=f
        ).grid(row=6, column=0, sticky=W, pady=10)

        name_input = Entry(
            right_frame,
            font=f
        )

        email_input = Entry(
            right_frame,
            font=f
        )

        phone_input = Entry(
            right_frame,
            font=f
        )

        password_input = Entry(
            right_frame,
            font=f,
            show='*'
        )
        pwd_again = Entry(
            right_frame,
            font=f,
            show='*'
        )

        register_btn = Button(
            right_frame,
            width=15,
            text='Register',
            font=f,
            relief=SOLID,
            cursor='hand2',
            command=store_info
        )

        # widgets placement
        email_tf.grid(row=0, column=1, pady=10, padx=20)
        pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        left_frame.place(x=50, y=50)

        name_input.grid(row=0, column=1, pady=10, padx=20)
        email_input.grid(row=1, column=1, pady=10, padx=20)
        phone_input.grid(row=2, column=1, pady=10, padx=20)
        password_input.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        right_frame.place(x=500, y=50)
        self.ws.mainloop()
