import math
import random
import sqlite3


class User:
    def __init__(self, userid, username):
        self.id = userid
        self.name = username
        self.money = 10000
        self.stock = {}

    def buy(self, stock, amount):
        if stock.name in self.stock:
            self.stock[stock.name] += amount
        else:
            self.stock[stock.name] = amount

        self.money -= stock.currentprice * amount

    def sell(self, stock, amount):
        if stock.name in self.stock:
            self.stock[stock.name] -= amount
            self.money += stock.currentprice * amount
