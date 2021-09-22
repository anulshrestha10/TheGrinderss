from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.title('Login and Registration Page')
root.geometry('600x400')
root.iconbitmap('carr.ico')
root.resizable(False, False)

### Using an image as background###
# resize image
pic = Image.open("background_entry.jpg")
resize_pic = pic.resize((603, 400), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)
label1 = Label(root, image=new_pic)
label1.place(x=-3, y=0)

label2 = Label(root, text="Welcome", font='Cambria 15 italic', fg='purple')
label2.place(x=300, y=10)
# creating database
conn = sqlite3.connect('Login and Registration.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE addressA(
                Name text,
        Username text,
        Password text,
        Country text
)""")

print("Table created successfully")
'''


# creating datbase for SIGNUP
def signUp():
    signwindow = Toplevel()
    signwindow.geometry('750x500')
    signwindow.resizable(False, False)
    signwindow.title('HURRY! SIGNUP')
    signwindow.iconbitmap('carr.ico')
    signwindow.configure(bg="Sky Blue")

    # title
    Frame1 = Frame(signwindow, bd=10, bg='black', width=1000, relief=RIDGE)
    Frame1.place(x=15, y=0)

    Frame1_label = Label(Frame1, font=('Ubuntu', 25, 'bold'), bg='light pink',
                         text='Hurry... SignUp and Enjoy The Adventure', padx=20)
    Frame1_label.grid()

    Entry_frame_details = Frame(signwindow, bd=10, bg='#D1C3BE', width=710, height=350, padx=250, relief=RIDGE)
    Entry_frame_details.place(x=15, y=100)


# making labels, entries and buttons
UsernameL = Label(root, text="Username", font='Cambria 15 italic').place(x=170, y=50)
Username_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Username_entry.place(x=270, y=50)
PasswordL = Label(root, text="Password", font='Cambria 15 italic').place(x=170, y=100)
Password_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Password_entry.place(x=270, y=100)

NewPlayer = Label(root, text="If you are a new Player->", font='Cambria 15 italic', fg='blue', width=70)
NewPlayer.place(x=-20, y=220)
login_button = Button(root, text="Login", font='Cambria 15 italic').place(x=300, y=170)
signup_button = Button(root, text="Sign Up", font='Cambria 15 italic', command=signUp).place(x=300, y=270)

conn.commit()

conn.close()

mainloop()
