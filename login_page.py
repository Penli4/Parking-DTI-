from tkinter import *

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # Login frame
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=550,y=90,width=350,height=460)

        title = Label(login_frame, text="Login System", font=("Elephant", 40, "bold"), bg="white", fg="black")
        title.place(x=0,y=30,relwidth=1)

        user_lbl = Label(login_frame, text="Username", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        user_lbl.place(x=20, y=100)
        txt_username = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC", fg="black",bd=1)
        txt_username.place(x=20, y=140, width=300)

        password_lbl = Label(login_frame, text="Password", font=("Andalus", 20, "bold"), bg="white", fg="#767171")
        password_lbl.place(x=20, y=190)
        txt_password = Entry(login_frame, font=("times new roman", 15), bg="#ECECEC", fg="black",bd=1)
        txt_password.place(x=20, y=240,width=300)

        forget_btn = Button(login_frame, text="Forget Password?", font=("times new roman",13),highlightbackground="white", fg="#00759E",bd=0)
        forget_btn.place(x=20,y=280)

        login_btn = Button(login_frame, text="Login",font=("Arial Rounded MT Bold", 15),bg="#0000FF", activebackground="#0000FF",fg="black",activeforeground="black",width=15, height=2, relief=FLAT, borderwidth=0)
        login_btn.place(x=20, y=350, width=300, height=35)

        rgr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        rgr_frame.place(x=550, y=570, width=350, height=60)
        reg_lbl=Label(rgr_frame, text="Don't have an account?", font=("times new roman",18), bg="white", fg="#767171")
        reg_lbl.place(x=30,y=11)
        su_btn = Button(rgr_frame, text="Sign up", font=("times new roman", 18),highlightbackground="white", fg="#00759E", bd=0)
        su_btn.place(x=208, y=11)

root = Tk()
obj = Login_System(root)
root.mainloop()
