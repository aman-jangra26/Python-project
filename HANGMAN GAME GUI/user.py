import mysql.connector
from tkinter import *
from  tkinter import ttk
top = Tk()
top.geometry("300x250")
top.title("HANGMAN GAME")
top.config(bg = '#E7FFFF')
game_frame = Frame(top)
game_frame.pack()
my_game = ttk.Treeview(game_frame)

my_game['columns'] = ('username', 'score')


my_game.column("#0", width=0,  stretch=NO)
my_game.column("username",anchor=CENTER, width=80)
my_game.column("score",anchor=CENTER,width=80)
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("username",text="username",anchor=CENTER)
my_game.heading("score",text="score",anchor=CENTER)




#username = StringVar()

#Label(top, text="Username * ").place(x=20,y=40)
    #Username textbox
#Entry(top, textvariable=username).place(x=90,y=42)

cnx = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "root",
                                     db ="hangman")
cursor = cnx.cursor()       
    

cursor.execute("select  * from score")
my_game.tag_configure("evenrow",background='pink',foreground='brown')
myresult = cursor.fetchall()
for x in myresult:
    my_game.insert(parent='',index='end',values=x,tags="evenrow")






my_game.pack()
b2 = Button(top, text = "EXIT",command =top.destroy
            ,activeforeground = "blue",activebackground = "pink").pack()

    
top.mainloop()
                              
cnx.close()
