from tkinter import *
import sqlite3

root=Tk()
root.title('Login and Registration Page')
#creating database
conn= sqlite3.connect('Login and Registration.db')

c= conn.cursor()

c.execute("""CREATE TABLE addressA(
                Name text,
        Username text,
        Password text,
        Country text
)""")

print("Table created successfully")


conn.commit()

conn.close()


mainloop()


