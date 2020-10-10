import sys
import mysql.connector
import time

#baglanti
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    passwd="db2020db",
    port=3307,
    database="todo",
)

entry=-1

while(entry != 0):
    print("choose process: "
          "\n 1=get users table "
          "\n 2=add user "
          "\n 3=update user password "
          "\n 4=delete user "
          "\n 5=get user by id  "
          "\n 6=get todos table "
          "\n 7=add todo "
          "\n 8=update todo description "
          "\n 9=delete todo "
          "\n 10=get todo by id,"
          " \n 0=cikis" )
    yourChoose = int(input("Please choose process: "))

    mycursor = mydb.cursor()
    if (yourChoose == 1):

        # mevcut tablonun cekilmesi
        mycursor.execute("SELECT  * FROM users")
        todos = mycursor.fetchall()

        # mevcut tablonun gosterilmesi
        print("Users Table: id, name, surname, email, city, birthday, password, visibility ")
        for row in todos:
            print(row)
        print("-----------------------")