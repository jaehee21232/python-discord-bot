import math
import random
import sqlite3

maxuptime = 180

conn = sqlite3.connect("sqlite_data/stock_data.db", isolation_level=None)

c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stock_data (종목 text, 금액 text)")
c.execute("CREATE TABLE IF NOT EXISTS 주식매수량 (아이디 text, 이름 text, 한세은행 text)")


class Stock:
    def __init__(self, name, price=0):
        self.name = name
        self.msg = ""

        if price == 0:
            self.currentprice = random.randrange(100, 1000)
        else:
            self.currentprice = price

    def __str__(self):
        return self.msg

    def updatestock(self):
        chagerate = random.randint(0, 200)
        if chagerate >= 100:
            self.currentprice -= chagerate
            self.msg = f"{self.name} 주당 현재가 {self.currentprice}(🔻변동가 {abs(chagerate)})\n"
        else:
            self.currentprice += chagerate
            self.msg = f"{self.name} 주당 현재가 {self.currentprice}(🔺 변동가 {abs(chagerate)})\n"
