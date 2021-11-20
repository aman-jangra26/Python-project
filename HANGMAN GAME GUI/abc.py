import mysql.connector
cnx = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "root",
                                     db ="hangman")
cursor = cnx.cursor()
import hangman as h

x=h.score

if(x==0):
   None
else:
   import between as b
   
      
