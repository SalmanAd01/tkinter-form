from tkinter import *
# import ImageTk
from PIL import ImageTk, Image
from tkinter import messagebox
from models.db import DB


class Dashboard:
    def __init__(self, ws, name, id):
        self.ws = ws
        self.name = name
        self.id = id

    def display(self):
        try:
            self.ws.withdraw()
            new_window = Toplevel()
            new_window.geometry("940x500")
            new_window.title("Dashboard")
            f = ('Times', 14)
            frame = Frame(new_window)
            frame.pack()
            frame.place(anchor='center', x=400, y=200)

            img = ImageTk.PhotoImage(Image.open(
                "C:/Users/salman/OneDrive/Desktop/Form/assets/values-1.png"))

            label = Label(frame, image=img)
            label.pack()

            # Add Label To Show The Name
            name_label = Label(new_window, text="Name : ", font=f)
            name_label.place(x=200, y=400)

            show_name_entry = Entry(new_window, width=20, font=f)
            show_name_entry.insert(0, self.name)
            show_name_entry.place(x=300, y=400)
            print("--->> ", self.id)
            db = DB(new_window)
            chnage_name_btn = Button(new_window, text="Change Name", font=f,
                                     command=lambda: db.update_name(show_name_entry.get(), self.id))
            chnage_name_btn.place(x=350, y=450)
            new_window.mainloop()
        except Exception as e:
            print("--->>", e)
            messagebox.showerror(self.ws, 'Some error occured')
