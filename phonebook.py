from Tkinter import *
import sqlite3
from Phonebook_007 import *
root = Tk()
root.geometry("1500x1500")
root.configure(background='black')
Label(root, text='Welcome to PHONEBOOK Directory',bg="black",fg ='Green',font="Javanese 27 italic bold").grid(row=0,column=0)
Label(root, text='Project of Python And Database',bg="black",fg ='yellow',font="Javanese 30 bold underline").grid(row=5,column=2)
Label(root, text='Devloped By :- Abhay Garg',fg ='#f4f5e2',font="Javanese 25 italic",bg="black").grid(row=6,column=2)
Label(root, text='Enrollment No :- 181B007 ',fg ='#f4f5e2',font="Javanese 25 italic",bg="black").grid(row=7,column=2)
Label(root, text='Batch :- B1',fg ='#f4f5e2',font="Times 25 italic",bg="black").grid(row=8,column=2)
def change(e=1):
    root.destroy()
    new_window()
root.bind('<Motion>',change)
root.mainloop()

