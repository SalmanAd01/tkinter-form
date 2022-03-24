from tkinter import *
# import ImageTk
from PIL import ImageTk, Image
from tkinter import messagebox


class Dashboard:
    def __init__(self, ws, name):
        self.ws = ws
        self.name = name

    def display(self):
        try:
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

            show_name = Label(new_window, text=f"{self.name}", font=f)
            show_name.place(x=300, y=400)

            new_window.mainloop()
        except Exception as e:
            print("--->>", e)
            messagebox.showerror(self.ws, 'Some error occured')
