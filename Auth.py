import sqlite3

connection = sqlite3.connect("Information.db")
cursor = connection.cursor()

def find(username, password):
    if (cursor.execute("""SELECT Password
                   FROM login_info
                   WHERE Username = """ + username + """, 
                   """)).upper == password.upper:
        return 0

def auth_user():
    while True:
        try:
            username = str(input("What is your username? "))
            password = str(input("What is your username? "))
            if find(username, password) == 0:
                break
        finally:
            print("invalid user validation.")
        return 0