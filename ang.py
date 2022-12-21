import sqlite3,random,math

jutime = 180
hansei_bank = None
jaeheedang = None
conn = sqlite3.connect("jusig_data.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS jusig_data \
    (종목 text, 금액 text)")
c.execute("CREATE TABLE IF NOT EXISTS 주식매수량 \
    (아이디 text, 이름 text, 한세은행 text)")


class Jusig:

    def Selete_money(id, juname):
        if juname == "한세은행":
            c.execute("SELECT * FROM 주식매수량 WHERE 아이디 ='{}'".format(id))
            for row in c.fetchall():
                return row[2]

    def jucheck(id):
        c.execute("SELECT 아이디 FROM 주식매수량")
        c.execute("SELECT * FROM 주식매수량 WHERE 아이디 ='{}'".format(id))
        if c.fetchone() == None:
            return False
        else:
            return True

    def jusigsign(name, money):
        c.execute(f"INSERT INTO jusig_data \
        VALUES('{name}', '{money}')")

    def upjusign(id, name, juname, ju1):
        c.execute("DELETE FROM 주식매수량 WHERE 아이디 = :ID",{"ID":id})
        Jusig.maesosign(id, name, juname, ju1)

    def maesosign(id, name, juname, ju1):
        if juname == "한세은행":
            c.execute(f"INSERT INTO 주식매수량 \
                VALUES('{id}', '{name}','{ju1}')")

    def Seletejusig(name):
        c.execute("SELECT * FROM jusig_data WHERE 종목 = :ID",{"ID":name})
        for row in c.fetchall():
            return row[1]

    def updatejusig(name, money):
        c.execute("DELETE FROM jusig_data WHERE 종목 = :ID",{"ID":name})
        Jusig.jusigsign(name, money)

    def jusigone():
        pl = random.choice(["+", "-"])
        zosik = random.randrange(1, 99)
        한세은행 = None
        if pl == "+":
            한세은행돈 =  int(Jusig.Seletejusig("한세은행")) + zosik
            한세은행 = "{}　한세은행　　{}(🔺{})".format(
                pl, 한세은행돈, str(zosik).rjust(8)
            )
            Jusig.updatejusig("한세은행", 한세은행돈)
            return 한세은행

        if pl == "-":
            한세은행돈 = int(Jusig.Seletejusig("한세은행")) - zosik
            한세은행 = "{}　한세은행　　{}(🔻{})".format(
                pl, 한세은행돈, str(zosik).rjust(8)
            )
            Jusig.updatejusig("한세은행", 한세은행돈)
            return 한세은행
    
    def jusigtwo():
        pl = random.choice(["+", "-"])
        zosik = random.randrange(1, 49)
        재희재당 = None
        if pl == "+":
            재희재당돈 =  int(Jusig.Seletejusig("재희재당")) + zosik
            재희재당 = "{}　재희재당　　{}(🔺 {})".format(
                pl, 재희재당돈, (zosik)
            )
            Jusig.updatejusig("재희재당", 재희재당돈)
            return 재희재당

        if pl == "-":
            재희재당돈 = int(Jusig.Seletejusig("재희재당")) - zosik
            재희재당 = "{}　재희재당　　{}(🔻 {})".format(
                pl, 재희재당돈, (zosik)
            )
            Jusig.updatejusig("재희재당", 재희재당돈)
            return 재희재당
        

    
    def jurestart():
        Jusig.jusigsign("한세은행", 1000)
        Jusig.jusigsign("재희재당", 500)

