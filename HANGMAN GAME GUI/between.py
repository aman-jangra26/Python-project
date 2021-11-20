import random
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import subprocess
cnx = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "root",
                                     db ="hangman")
cursor = cnx.cursor()

    

top = Tk()
top.geometry("350x300")
top.title("HANGMAN GAME")
top.config(bg = '#E7FFFF')
bg = PhotoImage(file = "bgxD.gif")
label1 = Label( top, image = bg)
label1.place(x = 0, y = 0)

def ok():
    name=user_name.get()
    score2=score_val.get()
    
    if(len(name)==0):
        messagebox.showinfo("info", "enter user name")
    else:
        
        jmd=str(name)
        jmd2=int(score2)
        qry="INSERT INTO score(username,score) VALUES(%s,%s)"
        cursor.execute(qry,(jmd,jmd2,))
       
        cnx.commit()
        
                    


        
    
    
user_name = StringVar()
score_val=IntVar()
Label(top, text="Enter your user name",fg = "blue",bg = "pink",
         font = "Helvetica 12 bold italic").place(relx=0.35,rely=0.1)
Label(top, text="Enter your score",fg = "blue",bg = "pink",
         font = "Helvetica 12 bold italic").place(relx=0.35,rely=0.4)
#Username textbox
Entry(top, textvariable=user_name,font = ('courier', 15, 'bold')).place(relx=0.19,rely=0.2)
Entry(top, textvariable=score_val,font = ('courier', 15, 'bold')
      ).place(relx=0.19,rely=0.5)
img=PhotoImage(file="ok.gif")
b1=Button(top,text="ok",command=ok,activeforeground = "red",
       activebackground = "orange")
b1.config(image=img)
b1.place(relx=0.35
         ,rely=0.7)

top.mainloop()


    
        
