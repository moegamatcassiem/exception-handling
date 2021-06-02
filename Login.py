from tkinter import *

root = Tk()

root.geometry("450x400")
root.title("Login Info")

result = StringVar()
tick_btn = StringVar()

Label(root, text="Login Info").place(x=200, y=20)

Label(root, text="Username: ").place(x=10, y=70)
user_ent = Entry(root)
user_ent.place(x=120, y=70)
user_ent.focus()
Label(root, text="Password: ").place(x=10, y=130)
pass_ent = Entry(root, show="\u2022")
pass_ent.place(x=120, y=130)
res_lab = Label(root, text="", textvariable=result)
res_lab.place(x=150, y=200)


def log_in():
    usernames = ["Uthmaan", "Cassiem", "Zaid", "Gary", "Aaliyah"]
    passwords = ["uthie", "Cassiem007", "0000", "skrr", "password"]

    found = False

    for x in range(len(usernames)):
        if user_ent.get() == usernames[x] and pass_ent.get() == passwords[x]:
            found = True

    if found:
        result.set("Welcome")
        root.destroy()
        import Deposit
    else:
        result.set("Access Denied!!!")

def clear():
    user_ent.delete(0, END)
    pass_ent.delete(0, END)
    result.set("")

def exit():
    root.destroy()

def toggle_password():
    global pass_ent, tick
    if tick_btn.get():
        pass_ent['show'] = ""
    else:
        pass_ent['show'] = ""

Button(root, text="Login", borderwidth=3, command=log_in).place(x=170, y=180)
Button(root, text="Clear", borderwidth=3, command=clear).place(x=70, y=180)
Button(root, text="Exit", borderwidth=3, command=exit).place(x=270, y=180)
tick = Checkbutton(root, onvalue=True, offvalue=False, textvariable=tick_btn, command=toggle_password)
tick.place(x=300, y=130)

root.mainloop()