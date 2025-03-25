from tkinter import *
from tkinter import messagebox
import os
import subprocess
users = {"Diya": "123456"}

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # Login frame
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=550, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Elephant", 40, "bold"), bg="white", fg="black")
        title.place(x=0, y=30, relwidth=1)

        # Username
        user_lbl = Label(login_frame, text="Username", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        user_lbl.place(x=20, y=100)
        self.username = StringVar()
        self.password = StringVar()
        txt_username = Entry(login_frame, textvariable=self.username, font=("times new roman", 15), bg="#ECECEC", fg="black", bd=1)
        txt_username.place(x=20, y=140, width=300)

        # Password
        password_lbl = Label(login_frame, text="Password", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        password_lbl.place(x=20, y=190)
        txt_password = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="#ECECEC", fg="black", bd=1)
        txt_password.place(x=20, y=240, width=300)

        #forgot password
        forget_btn = Button(login_frame, text = "Forgot Password?", font=("times new roman", 13), highlightbackground="white", fg="#00759E", bd=0)
        forget_btn.place(x = 20, y = 280)

        # Login button
        login_btn = Button(login_frame, command=self.login, text="Login", font=("Arial Rounded MT Bold", 15), bg="#0000FF", activebackground="#0000FF", fg="black", activeforeground="black", width=15, height=2, relief=FLAT, borderwidth=0 )
        login_btn.place(x=20, y=350, width=300, height=35)

        # Register frame
        rgr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        rgr_frame.place(x=550, y=570, width=350, height=60)

        reg_lbl = Label(rgr_frame, text="Don't have an account?", font=("times new roman", 18), bg="white", fg="#767171")
        reg_lbl.place(x=30, y=11)

        # Sign Up button
        su_btn = Button(rgr_frame, text="Sign up", command=self.open_signup, font=("times new roman", 18),highlightbackground="white", bg="white", fg="#00759E", bd=0)
        su_btn.place(x=208, y=11)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username not in users or users[username] != password:
            messagebox.showerror("Error", "Invalid Username or Password.\nTry again.")
        else:
            messagebox.showinfo("Success", f"Welcome : {username}")
            self.root.destroy()  # Close login window before opening the next page
            subprocess.Popen(["python", "parking_space.py"])  # Open the parking system

    def open_signup(self):
        self.new_window = Toplevel(self.root)
        self.app = Sign_up(self.new_window)

from tkinter import *
from tkinter import messagebox
import os

users = {"Diya": "123456"}

class Sign_up:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # Sign-Up Frame
        signup_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        signup_frame.place(x=550, y=90, width=350, height=460)

        title = Label(signup_frame, text="Sign Up", font=("Elephant", 40, "bold"), bg="white", fg="black")
        title.place(x=0, y=30, relwidth=1)

        # Username
        user_lbl = Label(signup_frame, text="New Username", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        user_lbl.place(x=20, y=100)
        self.new_username = StringVar()
        self.new_password = StringVar()
        txt_username = Entry(signup_frame, textvariable=self.new_username, font=("times new roman", 15), bg="#ECECEC", fg="black", bd=1)
        txt_username.place(x=20, y=140, width=300)

        # Password
        password_lbl = Label(signup_frame, text="New Password", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        password_lbl.place(x=20, y=190)
        txt_password = Entry(signup_frame, textvariable=self.new_password, show="*", font=("times new roman", 15), bg="#ECECEC", fg="black", bd=1)
        txt_password.place(x=20, y=240, width=300)

        # Register Button
        register_btn = Button(signup_frame, command=self.signup, text="Sign Up", font=("Arial Rounded MT Bold", 15), bg="#0000FF", activebackground="#0000FF", fg="black", activeforeground="black", width=15, height=2, relief=FLAT, borderwidth=0 )
        register_btn.place(x=20, y=300, width=300, height=35)

        # Back to Login
        back_btn = Button(signup_frame, text="Back to Login", command=self.back_to_login,
                          font=("times new roman", 14), bg="white", fg="#00759E", bd=0)
        back_btn.place(x=20, y=370)

    def signup(self):
        username = self.new_username.get()
        password = self.new_password.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[username] = password
            messagebox.showinfo("Success", "Account Created Successfully!")
            self.back_to_login()

    def back_to_login(self):
        self.root.destroy()

root = Tk()
obj = Login_System(root)
root.mainloop()
