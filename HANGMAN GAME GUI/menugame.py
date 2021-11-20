
from tkinter import *   
from tkinter import messagebox


import os
import subprocess
top = Tk()  
  
top.geometry("700x600")
top.title("HANGMAN GAME")
top.config(bg = '#E7FFFF')
bg = PhotoImage(file = "menubg.gif")
label1 = Label( top, image = bg)
label1.place(x = 0, y = 0)
  
def fun():  
    #messagebox.showinfo("Hello", "Red Button clicked")
    subprocess.call("abc.py", shell=True)

def viewuser():
    subprocess.call("user.py", shell=True)
    
l1=Label(top,text="Welcome To the HANGMAN Game !!!!!",fg = "Yellow",bg = "dark green",
         font = "Helvetica 16 bold italic").place(relx=0.5,rely=0.1,anchor='center')
#l2=Label(top,text="Choose PLAY to play game" , fg = "red",font = "Times").place(relx=0.5,rely=0.2,anchor='center')


#l3=Label(top,text="Choose Exit to close window", fg = "red",font = "Times").place(relx=0.5,rely=0.55,anchor='center')




img = PhotoImage(file="play.gif")


b1 = Button(top,text = "PLAY ",command = fun ,
            activeforeground = "red",activebackground = "orange")


b1.config(image=img)
b1.place(x=210,y=150)


  
img2=PhotoImage(file="exitr.gif")
b2 = Button(top, text = "EXIT",command =top.destroy
            ,activeforeground = "blue",activebackground = "pink")
b2.config(image=img2)
b2.place(x=210,y=270)
img3=PhotoImage(file="score.gif")
b3=Button(top,text="view scores " ,command=viewuser,activeforeground = "red",activebackground = "orange")
b3.config(image=img3)
b3.place(x=210,y=385)

  
 
 
  

  
top.mainloop()  
