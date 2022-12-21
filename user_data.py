import sqlite3

conn = sqlite3.connect("user.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS UserData \
    (name text, id text, money text)")

a = []
money = []


class User_Data:

    def sign(name, id, money):
        c.execute(f"INSERT INTO UserData \
        VALUES('{name}', '{id}', {money})")

    def check(id):
        c.execute("SELECT id FROM UserData")
        c.execute("SELECT * FROM UserData WHERE id ='{}'".format(id))
        if c.fetchone() == None:
            return False
        else:
            print("찾음")
            return True

    def Selete(id):
        c.execute("SELECT * FROM UserData WHERE id ='{}'".format(id))
        for row in c.fetchall():
            a.append(row[1])

    def change_user(name, id, money):
        c.execute("DELETE FROM UserData WHERE id = :ID", {"ID": id})
        User_Data.sign(name, id, money)

    def Selete_money(id):
        c.execute("SELECT * FROM UserData WHERE id ='{}'".format(id))
        for row in c.fetchall():
            money.append(row[2])
            return row[2]
