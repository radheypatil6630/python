import tkinter as tk 
from tkinter import messagebox

def new_W ():
    root.withdraw
    
    win_dow = tk.Toplevel(root)
    win_dow.geometry("300x300")
    l = tk.Label(win_dow,text="welcome to new window").pack()
    
    b = tk.Button(win_dow,text="back" ,command=lambda: logout(win_dow)).pack()
    
def logout(win_dow):
    win_dow.destroy()
    
    root.deiconify()
    
    
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username =="admin" and password == "12345":
        messagebox.showinfo("login correct","login")
        new_W()
    else:
        messagebox.showerror("failed","login failed")
        

root = tk.Tk()

entry_username = tk.Entry(root)
entry_username.pack()
entry_password = tk.Entry(root)
entry_password.pack()


lb = tk.Button(root,text="login",command=login).pack()


root.geometry("400x400")
root.mainloop()


