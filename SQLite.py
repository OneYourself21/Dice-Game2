import sqlite3

connnection = sqlite3.connect("Information.db")
cursor = connnection.cursor()
cursor.execute("""CREATE TABLE login_info(
               Username VARCHAR(255) PRIMARY KEY,
               Password VARCHAR(255) 
               )""")
cursor.execute("""
    INSERT INTO login_info VALUES
        ("OneYourself21","Ez"),
        ('OneYourself22',"Jk")
    """)
cursor.execute("""CREATE TABLE top_scores(
               Username VARCHAR(255),
               Password VARCHAR(255),
               Score INTEGER
               )""")
connnection.commit()
