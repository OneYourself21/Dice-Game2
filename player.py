import sqlite3
import gc

import string

db = sqlite3.connect("Information.db")
cursor = db.cursor()

class Player:
    def __init__(self):

        action = Player.input_valid("Login or Sign up?", ["LOGIN", "LOG", "SIGNUP", "SIGN"])

        succeed = True
        while succeed:
            try:
                if action == "LOGIN" or action == "LOG":
                    self.username = input("What is your username? ")
                    for player in Player.instance_list():
                        if player.username == self.username:
                            raise ValueError("Username has already been taken")
                    if Player.cleaner(self.username)== "SIGNUP" or Player.cleaner(self.username) == "SIGN":
                        action = self.username
                        raise ValueError("Switching to Sign up.")
                    if cursor("""FROM Information
                                 SELECT Attempts_Left
                                 WHERE Username == """ + self.username) == 0:
                        raise ValueError("Username has been locked out")
                    temp_pass = cursor("""FROM Information
                                          SELECT Password
                                          WHERE Username == """ + self.username)
                    while not cursor("""FROM Information
                                        SELECT Attempts_Left
                                        WHERE Username == """ + self.username) == 0:
                        self.password = str(input("What is the password for this account? "))
                        if temp_pass == self.password:
                            succeed = True
                            print("Login Successful")
                            cursor("""UPDATE Information
                                      SET Attempts_Left =""" + str(5) +
                                     "WHERE Username == " + self.username)
                            db.commit()

                            break
                        elif temp_pass != self.password:
                            print("Password Failed")
                            cursor("""UPDATE Information
                                      SET Attempts_Left =""" + str((cursor("""FROM Information
                                                                              SELECT Attempts_Left
                                                                              WHERE Username == """ + self.username) - 1)) +
                                     "WHERE Username == " + self.username)
                            db.commit()


                elif action == "SIGNUP" or action == "SIGN":
                    self.username = input("What is your username? ")
                    for player in cursor("""FROM Information
                                            SELECT Username"""):
                        if player.username == self.username:
                            raise ValueError("Username has already been taken")
                    is_secure = False
                    while not is_secure:
                        self.password = input("Create a password must be secure (any spaces entered will be interpreted as a password however any spaces at the end will be removed). ")
                        if self.password.isupper() or self.password.islower():
                            print("Use a mix of upper and lower case character to create a secure password.")
                        elif not any(char.isdigit() for char in self.password):
                            print("Use digits to make the password harder to guess.")
                        elif not any(char == any(char for char in string.punctuation) for char in string.punctuation):
                            print("use Special characters.")
                        elif len(self.password) < 8: #idm if no regular characters tbh cus that's hard to guess too lol
                            print("use a longer password.")
                        else:
                            cursor("""INSERT INTO Information (Username, Password, Attempts_Left)
                                      VALUES (""" + self.username + """,""" + self.password + """, """ + 5 + """ )""")
                            is_secure = True
                            succeed = True

            except ValueError as error_msg:
                print(error_msg)
        self.scores = []



    @staticmethod  # idk man python hurts my mind why cant it be the same as java smh :(
    def input_valid(input_text, allowed):
        while True:
            try:
                temp = Player.cleaner(input(input_text))
                for allows in allowed:
                    if temp == allows:
                        return temp
            finally:
                print("Invalid input please try again. (type either Log In or Sign Up)")

    @staticmethod
    def instance_list():
        temp_list = []
        for obj in gc.get_objects():
            if isinstance(obj, Player):
                temp_list.append(obj)
        return temp_list

    @staticmethod
    def cleaner(temp):
        return (((input(temp)).upper()).replace("_", "")).replace(" ", "")

    @staticmethod
    def find(username, password):
        if (cursor.execute("""SELECT Password
                       FROM login_info
                       WHERE Username = """ + username + """, 
                       """)).upper == password.upper:
            return 0