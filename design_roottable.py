from tkinter import *
import sqlite3

root=Tk()
root.title('Login and Registration Page')
root.geometry('600x400')
root.iconbitmap('carr.ico')
#creating database
conn= sqlite3.connect('Login and Registration.db')

c= conn.cursor()

'''
c.execute("""CREATE TABLE addressA(
                Name text,
        Username text,
        Password text,
        Country text
)""")

print("Table created successfully")
'''
UsernameL = Label(root, text="Username", font='Cambria 15 italic').place(x=170, y=50)
Username_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Username_entry.place(x=270, y=50)
PasswordL = Label(root, text="Password", font='Cambria 15 italic').place(x=170, y=100)
Password_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Password_entry.place(x=270, y=100)

NewPlayer = Label(root, text="If you are a new Player->", font='Cambria 15 italic', fg='blue', width=70)
NewPlayer.place(x=-20, y=220)
login_button = Button(root, text="Login", font='Cambria 15 italic').place(x=300, y=170)
signup_button = Button(root, text="Sign Up", font='Cambria 15 italic').place(x=300, y=270)


conn.commit()

conn.close()


mainloop()


