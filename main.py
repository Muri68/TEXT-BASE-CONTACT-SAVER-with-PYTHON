import sqlite3
import time
import sys

def main_menu():
    print("Welcome to my Contact Saver")
    menu = ("""
    1 - Creaate New User
    2 - Login to system
    3 - Exit system\n""")

    userchoice = input(menu)

    if userchoice == "1":
        newUser()

    elif userchoice == "2":
        login()

    elif userchoice == "3":
        print("Goodbye")
        sys.exit()

    else:
        print("Command nor recognised: ")

def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("Test.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("\nWelcome " +i[2])
            #return("exit")
            break

        else:
            print("Username and password not recognised")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

def newUser():
    found = 0
    while found ==0:
        username = input("Please enter a username: ")
        with sqlite3.connect("Test.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print("Username Taken,Please try again")
        else:
            found = 1

    firstname = input("Enter your first name: ")
    lastname = input("Enter your lastname: ")
    password = input("Please enter your password: ")
    password = input("Please reenter password: ")
    while password !=password:
        print("Your password didn't match, please try again")
        password = input("Please enter your password: ")
        password = input("Please reenter password: ")
    insertData = '''INSERT INTO user(username,firstname,lastname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username),(firstname),(lastname),(password)])
    db.commit()

def  add_contact():
    found = 0
    while found ==0:
        phonenumber = input("Please enter a Phone Number: ")
        with sqlite3.connect("Contact.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE phonenumber = ?")
        cursor.execute(findUser,[(phonenumber)])

        if cursor.fetchall():
            print("Phone Number already stored,Please try again")
        else:
            found = 1

    fullname = input("Enter Fullname: ")
    phonenumber = input("Enter Phone Number: ")
    email = input("Please enter Email Address: ")
   
    insertData = '''INSERT INTO user(fullname,phonenumber,email)
    VALUES(?,?,?)'''
    cursor.execute(insertData,[(fullname),(phonenumber),(email)])
    db.commit()
    print("\nContact Successfully Save\n")

def search_contact():
    while True:
        fullname = input("Please enter Fullname you want to Searche for: ")
        with sqlite3.connect("Contact.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE fullname = ?")
        cursor.execute(find_user,[(fullname)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("\nFullname: " +i[1] + "\nPhone Number: " +i[2] + "\nEmail Address: " +i[3])
            #return("exit")
            break

        else:
            print("Contact not found")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

def list_contacts():
    
    with sqlite3.connect("Contact.db") as db:
        cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL,
    phonenumber VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL);
    ''')

    #cursor.execute("""
    #INSERT INTO user(fullname,phonenumber,email)
    #VALUES("Isyaku Murtala","08064732356","muriisyaku68@gmail.com")
    #""")

    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for row in rows:
        print("\nFullname: " + str(row[1]) + "\nPhone Number: " + str(row[2]) + "\nEmail Address: "+ str(row[3]))
    #print(cursor.fetchall())

    db.commit()


def menu():
    while True:
        print("Welcome to my Contact Saver")
        menu = ("""
        1 - Add New Contact
        2 - Show All Contacts
        3 - Search Contact
        4 - Exit system\n""")

        userchoice = input(menu)

        if userchoice == "1":
             add_contact()

        elif userchoice == "2":
            list_contacts()

        elif userchoice == "3":
            search_contact()
            

        elif userchoice == "4":
            print("Goodbye")
            sys.exit()

        else:
            print("Command nor recognised, Please try again: ")

main_menu()
main_menu()
menu()

