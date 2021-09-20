from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Login and Registration Page')
root.geometry('600x400')
root.iconbitmap('race_car_icon_125926.ico')
root.resizable(False, False)

### Using an image as background###
# resize image
pic = Image.open("background_entry.jpg")
resize_pic = pic.resize((603, 400), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)
label1 = Label(root, image=new_pic)
label1.place(x=-3, y=0)

label2 = Label(root, text="Welcome", font='Ubuntu', fg='purple')
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


# creating database for SIGNUP
def Signin():
    def signUp():
        conn = sqlite3.connect("Login and Registration.db")
        c = conn.cursor()

        c.execute("INSERT INTO addressA VALUES(:Name_label, :Username_label, :Password_label,:Country_label)", {
            'Name_label': Name_entry.get(),
            'Username_label': Username_entry.get(),
            'Password_label': Password_entry.get(),
            'Country_label': Country_entry.get()
        })

        print('SIGN SUCCESSFUL')
        roe = c.fetchall()
        print(roe)

        conn.commit()
        conn.close()

        Name_entry.delete(0, END)
        Username_entry.delete(0, END)
        Password_entry.delete(0, END)
        Country_entry.delete(0, END)

    signwindow = Toplevel()
    signwindow.geometry('650x400')
    signwindow.resizable(False, False)
    signwindow.title('HURRY! SIGNUP')
    signwindow.iconbitmap('CarIcon.png')
    signwindow.configure(bg="Sky Blue")

    Frame1 = Frame(signwindow, bd=10, bg='black', width=600, relief=RIDGE)
    Frame1.place(x=15, y=0)

    Frame1_label = Label(Frame1, font=('Ubuntu', 20, 'bold'), bg='light pink',
                         text='Hurry... SignUp and Enjoy The Adventure', padx=20)
    Frame1_label.grid()

    Entry_frame_details = Frame(signwindow, bd=10, bg='#D1C3BE', width=610, height=290, padx=250, relief=RIDGE)
    Entry_frame_details.place(x=15, y=100)

    # making labels, entries and buttons for signup
    Name_label = Label(Entry_frame_details, text='Name', font='Ubuntu', bg="#D1C3BE").place(x=-220, y=5)

    Name_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Name_entry.place(x=-130, y=1)

    Username_label = Label(Entry_frame_details, text="Username", font='Ubuntu', bg="#D1C3BE").place(
        x=-220, y=50)

    Username_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Username_entry.place(x=-130, y=50)

    Password_label = Label(Entry_frame_details, text="Password", font='Ubuntu', bg="#D1C3BE").place(
        x=-220, y=100)

    Password_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Password_entry.place(x=-130, y=100)

    Country_label = Label(Entry_frame_details, text="Country", font='Ubuntu', bg="#D1C3BE").place(x=-220,
                                                                                                  y=150)

    Country_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Country_entry.place(x=-130, y=150)

    SubmitButton = Button(Entry_frame_details, text="Submit", font='Ubuntu', bg="Light Green", command=signUp).place(
        x=-130,
        y=203)

# Fuction to get into game
def logdata():
    conn = sqlite3.connect("Login and Registration.db")
    c = conn.cursor()

    lnam = Username_entry.get()
    lpass = Password_entry.get()

    c.execute("SELECT * FROM addressA")
    record = c.fetchall()
    print(record)
    user = []
    passw = []

    for records in record:
        user += [records[1]]
        passw += [records[2]]
    print(user)
    print(passw)

    if lnam in user and lpass in passw:
        if user.index(lnam) == passw.index(lpass):
            print("sucess")
            import final


        else:
            messagebox.showinfo("FAILED", "Invalid Username or Password")

    else:
        messagebox.showinfo("FAILED", "Invalid Username or Password")

    Username_entry.delete(0, END)
    Password_entry.delete(0, END)

    conn.commit()
    conn.close()


# making labels, entries and buttons
UsernameL = Label(root, text="Username", font='Ubuntu', bg="Light Green").place(x=170, y=50)
Username_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Username_entry.place(x=270, y=50)
PasswordL = Label(root, text="Password", font='Ubuntu', bg="light green").place(x=170, y=100)
Password_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Password_entry.place(x=270, y=100)

NewPlayer = Label(root, text="If you are a new Player", font='Ubuntu', fg='blue', bg="#C4CFD8", width=70)
NewPlayer.place(x=5, y=270)
login_button = Button(root, text="Login", font='Ubuntu', bg="Light Green",command=logdata).place(x=300, y=170)
signup_button = Button(root, text="Sign Up", font='Ubuntu', bg="Light Green", command=Signin).place(x=300, y=220)

conn.commit()

conn.close()

mainloop()
