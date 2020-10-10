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

    elif(yourChoose == 2):
        # get last user id
        mycursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
        lastUserId = mycursor.fetchone()
        print(int(lastUserId[0]), " last user id")

        print("New User is creating")

        lastID = lastUserId[0]
        print("new user id: ", lastID + 1)

        id = lastID + 1
        name = str(input("name: "))
        surname = str(input("surname: "))
        email = str(input("email: "))
        city = str(input("city: "))
        birthday = time.strftime(input("birthday: "))
        password = str(input("password: "))
        visibility = 1

        values = (id, name, surname, email, city, birthday, password, visibility )
        addUserQuery = "Insert into users values(%s, %s, %s, %s, %s, %s, %s, %s)"

        x = mydb.cursor()
        a = x.execute(addUserQuery, values)
        mydb.commit()

        if a != enumerate:
            print("User is added successfully")
        else:
            print("Error")

        print("-----------------------")

    elif (yourChoose == 3):
        # user update
        mycursor = mydb.cursor()
        id = int(input("which do you update of the user id: "))

        password = str(input("password: "))
        updateUserQuery = "UPDATE users SET password = {} WHERE id = {} ".format(password, id)
        values = (password)
        mycursor.execute(updateUserQuery, values)
        mydb.commit()
        print("-----------------------")