import sys
import mysql.connector
import time

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
          "\n 10=get todo by id"
          "\n 10=show the todo list"
          " \n 0=close" )
    yourChoose = int(input("Please choose process: "))

    mycursor = mydb.cursor()
    if (yourChoose == 1):
        mycursor.execute("SELECT  * FROM users")
        users = mycursor.fetchall()

        print("Users Table: id, name, surname, email, city, birthday, password, visibility ")
        for row in users:
            print(row)
        print("-----------------------")

    elif(yourChoose == 2):
        name = str(input("name: "))
        surname = str(input("surname: "))
        email = str(input("email: "))
        city = str(input("city: "))
        birthday = time.strftime(input("birthday: "))
        password = str(input("password: "))

        values = (name, surname, email, city, birthday, password)
        addUserQuery = "INSERT INTO users (name, surname, email, city, birthday, password) VALUES(%s, %s, %s, %s, %s, %s)"

        a = mydb.cursor().execute(addUserQuery, values)
        mydb.commit()

        if a != enumerate:
            print("User is added successfully")
            mycursor.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1")
            lastUserId = mycursor.fetchone()
            print(int(lastUserId[0]), " last user id")
        else:
            print("Error")
        print("-----------------------")

    elif (yourChoose == 3):
        mycursor = mydb.cursor()
        id = int(input("which do you update of the user id: "))

        password = str(input("password: "))
        updateUserQuery = "UPDATE users SET password = {} WHERE id = {} ".format(password, id)
        values = (password)
        mycursor.execute(updateUserQuery, values)
        mydb.commit()
        print("-----------------------")

    elif(yourChoose == 4 ):
        mycursor = mydb.cursor()
        id = int(input("which do you delete of the user(please entry user id): "))

        changeVisibilityQuery = "UPDATE users SET visibility=0 WHERE id = {} ".format(id)
        mycursor.execute(changeVisibilityQuery, id)
        mydb.commit()
        print("-----------------------")

    elif (yourChoose == 5):
        id = int(input("Select user id: "))
        selectUserQuery = "SELECT * FROM users WHERE id = {} ".format(id)
        values = (id)
        mycursor.execute(selectUserQuery, id)

        myresult = mycursor.fetchall()
        for getUser in myresult:
            print("Selected User VALUES: ", getUser)
        print("-----------------------")


    elif(yourChoose == 6):
        mycursor.execute("SELECT  * FROM todos")
        todos = mycursor.fetchall()

        print("Todos table: ")
        for row in  todos:
            print(row)
        print("Total Todo Count: ", mycursor.rowcount)
        print("-----------------------")

    elif (yourChoose == 7):
        userId = int(input("user id: "))
        name = str(input("todo name: "))
        description = str(input("todo description: "))
        time = time.strftime(input("todo time: "))

        newTodoValues = (userId, name, description, time)
        addTodoQuery = "INSERT INTO todos (userId, name, description, time) VALUES(%s, %s, %s, %s)"

        a = mydb.cursor().execute(addTodoQuery, newTodoValues)
        mydb.commit()

        if a != enumerate:
            print("Success")
        else:
            print("Error")
        print("-----------------------")

    elif(yourChoose == 8):
        mycursor = mydb.cursor()
        id = int(input("which do you update of the todo id: "))

        description = str(input("description: "))
        updateTodoDescriptionQuery = "UPDATE todos SET description = {} WHERE id = {} ".format(description, id)
        values = (description)
        mycursor.execute(updateTodoDescriptionQuery, values)
        mydb.commit()

        print("-----------------------")

    elif(yourChoose == 9 ):
        mycursor = mydb.cursor()
        id = int(input("which do you delete of the todo(please entry todo id): "))

        deleteTodoQuery = "UPDATE todos SET visibility=0 WHERE id = {} ".format(id)
        mycursor.execute(deleteTodoQuery, id)
        mydb.commit()

        print("-----------------------")

    elif(yourChoose == 10):
        id = int(input("Select todo id: "))
        selectUserQuery = "SELECT * FROM todos WHERE id = {} ".format(id)
        values = (id)
        mycursor.execute(selectUserQuery, id)

        myresult = mycursor.fetchall()
        for getTodo in myresult:
            print("Selected Todo VALUES: ", getTodo)
        print("-----------------------")

    elif(yourChoose == 11):
        mycursor = mydb.cursor()

        mycursor.execute(
            "SELECT users.id AS 'user id', users.name, users.surname, users.visibility, todos.name AS 'todo name', todos.description, todos.time  FROM users INNER JOIN todos ON users.id = todos.userID")
        todos = mycursor.fetchall()

        for row in todos:
            print(row)
        print(" Total todo count is:  " , mycursor.rowcount)


    elif(yourChoose == 0):
        sys.exit()