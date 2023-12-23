import _sqlite3  # could be abandoned
class Player:
    def __init__(self, username, password):
        action = Player.input_valid("Login or Sign up?", ["LOGIN", "LOG", "SIGNUP", "SIGN"])

        succeed = True
        while succeed:
            if action == "LOGIN" or action == "LOG":
                pass
            elif action == "SIGNUP" or action == "SIGN":
                pass

        self.username = username
        self.password = password
        self.scores = []

    @staticmethod  # idk man python hurts my mind why cant it be the same as java smh :(
    def input_valid(input_text, allowed):
        while True:
            try:
                temp = (((input(input_text)).upper()).replace("_", "")).replace(" ", "")
                for allows in allowed:
                    if temp == allows:
                        return temp
            finally:
                print("Invalid input please try again. (type either Log In or Sign Up)")



