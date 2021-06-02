from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("450x400")
root.title("Malaysia trip")

results = IntVar()

ent_lab = Label(root, text="Enter amount: ").place(x=10, y=70)
user_ent = Entry(root)
user_ent.place(x=120, y=70)
user_ent.focus()

def submit():
    if int(user_ent.get()) < 3000:
        raise Exception(messagebox.showinfo("STATUS FEEDBACK", "Please deposit more funds for this excursion"))
    else:
        messagebox.showinfo("STATUS FEEDBACK", "You qualify for the malaysia trip. Congratulations")

def exit():
    root.destroy()

exit_btn = Button(root, text="Exit", borderwidth=3, command=exit).place(x=220, y=120)
deposit_btn = Button(root, text="Deposit", borderwidth=3, command=submit).place(x=120, y=120)

root.mainloop()