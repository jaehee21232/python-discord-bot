import sqlite3

conn = sqlite3.connect("sqlite_data/seosda_data.db", isolation_level=None)

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS seosda (id text, 이름 text, Card1 text, Card2 text, 결과 text)")

s = 0
a = []
n = []
D = []
Seosda_player = 0

Seosda_Card = [
    "https://cdn.discordapp.com/attachments/907266059457925130/907266083285762078/1-1.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266089417834536/1-2.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266094094512168/1-3.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266099396100116/1-4.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266107558223912/1-5.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266113094688878/1-6.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266119029653544/1-7.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266123957956639/1-8.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266127829291028/1-9.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266132241678386/1-10.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266152277868554/2-1.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266156774174750/2-2.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266160918163506/2-3.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266165099872306/2-4.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266168501448834/2-5.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266172532174858/2-6.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266175937966150/2-7.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266179318554634/2-8.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266182720139264/2-9.jpg",
    "https://cdn.discordapp.com/attachments/907266059457925130/907266186289500250/2-10.jpg"
]

NN = "https://cdn.discordapp.com/attachments/904681455186247693/909456946577428480/unknown.png"


class Seosda:

    def seosdasign(self, id, name, card1, card2, mains):
        c.execute(f"INSERT INTO seosda \
        VALUES('{id}', '{name}','{card1}','{card2}','{str(mains)}')")

    def seosdacheck(self, id):
        c.execute("SELECT id FROM seosda")
        c.execute("SELECT * FROM seosda WHERE id ='{}'".format(id))
        if c.fetchone() == None:
            return False
        else:
            return True

    def Seleteid(self):
        c.execute("SELECT * FROM seosda")
        for row in c.fetchall():
            a.append(row[0])

    def Data_delete(self):
        c.execute("DELETE FROM 'seosda'")

    def changeone(self, id, name, card1, card2, cardmain):
        c.execute("DELETE FROM seosda WHERE id = :ID", {"ID": id})
        Seosda.seosdasign(self, id, name, card1, card2, str(cardmain))

    def Seletename(self):
        c.execute("SELECT * FROM seosda")
        for row in c.fetchall():
            n.append(row[1])

    def Delete(self, id):
        c.execute("DELETE FROM seosda WHERE id = :ID", {"ID": id})

    def SeleteDeck(self):
        c.execute("SELECT * FROM seosda")
        for row in c.fetchall():
            D.append(row[4])


class Deck:

    def GiveCard(self, P):
        if P == 1:
            return Seosda_Card[1], Seosda_Card[2]
        if P == 2:
            return Seosda_Card[3], Seosda_Card[4]
        if P == 3:
            return Seosda_Card[5], Seosda_Card[6]
        if P == 4:
            return Seosda_Card[7], Seosda_Card[8]

    def CardCheck(self, card):
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266083285762078/1-1.jpg":
            return "일광"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266089417834536/1-2.jpg":
            return "이월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266094094512168/1-3.jpg":
            return "삼광"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266099396100116/1-4.jpg":
            return "사월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266107558223912/1-5.jpg":
            return "오월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266113094688878/1-6.jpg":
            return "육월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266119029653544/1-7.jpg":
            return "칠월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266123957956639/1-8.jpg":
            return "팔광"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266127829291028/1-9.jpg":
            return "구월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266132241678386/1-10.jpg":
            return "십월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266152277868554/2-1.jpg":
            return "일월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266156774174750/2-2.jpg":
            return "이월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266160918163506/2-3.jpg":
            return "삼월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266165099872306/2-4.jpg":
            return "사월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266168501448834/2-5.jpg":
            return "오월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266172532174858/2-6.jpg":
            return "육월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266175937966150/2-7.jpg":
            return "칠월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266179318554634/2-8.jpg":
            return "팔월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266182720139264/2-9.jpg":
            return "구월"
        if card == "https://cdn.discordapp.com/attachments/907266059457925130/907266186289500250/2-10.jpg":
            return "십월"

    def Cardmain(self, card1, card2):
        if card1 == "삼광" and card2 == "팔광":
            return "삼팔광땡", 1
        elif card1 == "팔광" and card2 == "삼광":
            return "삼팔광땡", 1

        elif card1 == "일광" and card2 == "삼광":
            return "광땡", 2
        elif card1 == "일광" and card2 == "팔광":
            return "광땡", 2
        elif card1 == "삼광" and card2 == "일광":
            return "광땡", 2
        elif card1 == "팔광" and card2 == "일광":
            return "광땡", 2
        # ------------- 땡 3등------- 순서대로 순위
        elif card1 == "일광" and card2 == "일월":
            return "1땡", 3.9
        elif card1 == "일월" and card2 == "일광":
            return "1땡", 3.9
        elif card1 == "이월" and card2 == "이월":
            return "2땡", 3.8
        elif card1 == "삼광" and card2 == "삼월":
            return "3땡", 3.7
        elif card1 == "삼월" and card2 == "삼광":
            return "3땡", 3.7
        elif card1 == "사월" and card2 == "사월":
            return "4땡", 3.6
        elif card1 == "오월" and card2 == "오월":
            return "5땡", 3.5
        elif card1 == "육월" and card2 == "육월":
            return "6땡", 3.4
        elif card1 == "칠월" and card2 == "칠월":
            return "7땡", 3.3
        elif card1 == "팔월" and card2 == "팔광":
            return "8땡", 3.2
        elif card1 == "팔광" and card2 == "팔월":
            return "8땡", 3.2
        elif card1 == "구월" and card2 == "구월":
            return "9땡", 3.1
        elif card1 == "십월" and card2 == "십월":
            return "10땡", 3
        # ---------------------------------
        elif card1 == "일광" and card2 == "이월":
            return "알리", 4
        elif card1 == "일월" and card2 == "이월":
            return "알리", 4
        elif card1 == "이월" and card2 == "일광":
            return "알리", 4
        elif card1 == "이월" and card2 == "일월":
            return "알리", 4

        elif card1 == "일광" and card2 == "사월":
            return "독사", 5
        elif card1 == "일월" and card2 == "사월":
            return "독사", 5
        elif card1 == "사월" and card2 == "일월":
            return "독사", 5
        elif card1 == "사월" and card2 == "일광":
            return "독사", 5

        elif card1 == "일광" and card2 == "구월":
            return "구삥", 6
        elif card1 == "일월" and card2 == "구월":
            return "구삥", 6
        elif card1 == "구월" and card2 == "일광":
            return "구삥", 6
        elif card1 == "구월" and card2 == "일월":
            return "구삥", 6

        elif card1 == "일광" and card2 == "십월":
            return "장삥", 7
        elif card1 == "일월" and card2 == "십월":
            return "장삥", 7
        elif card1 == "십월" and card2 == "일광":
            return "장삥", 7
        elif card1 == "십월" and card2 == "일월":
            return "장삥", 7

        elif card1 == "사월" and card2 == "십월":
            return "장사", 8
        elif card1 == "십월" and card2 == "사월":
            return "장사", 8

        elif card1 == "사월" and card2 == "육월":
            return "세륙", 9
        elif card1 == "육월" and card2 == "사월":
            return "세륙", 9

         # 갑오 10등
        elif card1 == "일광" and card2 == "팔광":
            return "갑오", 10
        elif card1 == "일광" and card2 == "팔월":
            return "갑오", 10
        elif card1 == "일월" and card2 == "팔월":
            return "갑오", 10
        elif card1 == "일월" and card2 == "팔월":
            return "갑오", 10
        elif card1 == "팔광" and card2 == "일월":
            return "갑오", 10
        elif card1 == "팔광" and card2 == "일광":
            return "갑오", 10
        elif card1 == "팔월" and card2 == "일광":
            return "갑오", 10
        elif card1 == "팔월" and card2 == "일월":
            return "갑오", 10
        elif card1 == "이월" and card2 == "칠월":
            return "갑오", 10
        elif card1 == "칠월" and card2 == "이월":
            return "갑오", 10
        elif card1 == "삼월" and card2 == "육월":
            return "갑오", 10
        elif card1 == "삼광" and card2 == "육월":
            return "갑오", 10
        elif card1 == "육월" and card2 == "삼월":
            return "갑오", 10
        elif card1 == "육월" and card2 == "삼광":
            return "갑오", 10
        elif card1 == "사월" and card2 == "오월":
            return "갑오", 10
        elif card1 == "오월" and card2 == "사월":
            return "갑오", 10

        # ------끗--------------------------------- 높은 순서대로
        elif card1 == "팔월" and card2 == "십월":
            return "여덟끗", 11
        elif card1 == "십월" and card2 == '팔월':
            return "여덟끗", 11
        elif card1 == "일광" and card2 == "칠월":
            return "여덟끗", 11
        elif card1 == "일월" and card2 == "칠월":
            return "여덟끗", 11
        elif card1 == "칠월" and card2 == "일월":
            return "여덟끗", 11
        elif card1 == "칠월" and card2 == "일광":
            return "여덟끗", 11
        elif card1 == "이월" and card2 == "육월":
            return "여덟끗", 11
        elif card1 == "육월" and card2 == "이월":
            return "여덟끗", 11
        elif card1 == "삼광" and card2 == "오월":
            return "여덟끗", 11
        elif card1 == "삼월" and card2 == "오월":
            return "여덟끗", 11
        elif card1 == "오월" and card2 == "삼광":
            return "여덟끗", 11
        elif card1 == "오월" and card2 == "삼월":
            return "여덟끗", 11

        elif card1 == "칠월" and card2 == "십월":
            return "일곱끗", 11.1
        elif card1 == "십월" and card2 == "칠월":
            return "일곱끗", 11.1
        elif card1 == "팔월" and card2 == "구월":
            return "일곱끗", 11.1
        elif card1 == "팔광" and card2 == "구월":
            return "일곱끗", 11.1
        elif card1 == "구월" and card2 == "팔월":
            return "일곱끗", 11.1
        elif card1 == "구월" and card2 == "팔광":
            return "일곱끗", 11.1
        elif card1 == "삼광" and card2 == "사월":
            return "일곱끗", 11.1
        elif card1 == "삼월" and card2 == "사월":
            return "일곱끗", 11.1
        elif card1 == "사월" and card2 == "삼광":
            return "일곱끗", 11.1
        elif card1 == "사월" and card2 == "삼월":
            return "일곱끗", 11.1
        elif card1 == "이월" and card2 == "오월":
            return "일곱끗", 11.1
        elif card1 == "오월" and card2 == "이월":
            return "일곱끗", 11.1
        elif card1 == "일광" and card2 == "육월":
            return "일곱끗", 11.1
        elif card1 == "일월" and card2 == "육월":
            return "일곱끗", 11.1
        elif card1 == "육월" and card2 == "일광":
            return "일곱끗", 11.1
        elif card1 == "육월" and card2 == "일월":
            return "일곱끗", 11.1

        elif card1 == "육월" and card2 == "십월":
            return "여섯끗", 11.2
        elif card1 == "십월" and card2 == "육월":
            return "여섯끗", 11.2
        elif card1 == "이월" and card2 == "사월":
            return "여섯끗", 11.2
        elif card1 == "사월" and card2 == "이월":
            return "여섯끗", 11.2
        elif card1 == "일광" and card2 == "오월":
            return "여섯끗", 11.2
        elif card1 == "일월" and card2 == "오월":
            return "여섯끗", 11.2
        elif card1 == "오월" and card2 == "일광":
            return "여섯끗", 11.2
        elif card1 == "오월" and card2 == "일월":
            return "여섯끗", 11.2
        elif card1 == "칠월" and card2 == "구월":
            return "여섯끗", 11.2
        elif card1 == "구월" and card2 == "칠월":
            return "여섯끗", 11.2

        elif card1 == "이월" and card2 == "삼광":
            return "다섯끗", 11.3
        elif card1 == "이월" and card2 == "삼월":
            return "다섯끗", 11.3
        elif card1 == "삼광" and card2 == "이월":
            return "다섯끗", 11.3
        elif card1 == "삼월" and card2 == "이월":
            return "다섯끗", 11.3
        elif card1 == "칠월" and card2 == "팔월":
            return "다섯끗", 11.3
        elif card1 == "팔월" and card2 == "칠월":
            return "다섯끗", 11.3
        elif card1 == "육월" and card2 == "구월":
            return "다섯끗", 11.3
        elif card1 == "구월" and card2 == "육월":
            return "다섯끗", 11.3
        elif card1 == "오월" and card2 == "십월":
            return "다섯끗", 11.3
        elif card1 == "십월" and card2 == "오월":
            return "다섯끗", 11.3

        elif card1 == "사월" and card2 == "십월":
            return "네끗", 11.4
        elif card1 == "십월" and card2 == "사월":
            return "네끗", 11.4
        elif card1 == "오월" and card2 == "구월":
            return "네끗", 11.4
        elif card1 == "구월" and card2 == "오월":
            return "네끗", 11.4
        elif card1 == "육월" and card2 == "팔월":
            return "네끗", 11.4
        elif card1 == "팔월" and card2 == "육월":
            return "네끗", 11.4
        elif card1 == "일광" and card2 == "삼광":
            return "네끗", 11.4
        elif card1 == "일광" and card2 == "삼월":
            return "네끗", 11.4
        elif card1 == "일월" and card2 == "삼광":
            return "네끗", 11.4
        elif card1 == "일월" and card2 == "삼월":
            return "네끗", 11.4
        elif card1 == "삼광" and card2 == "일광":
            return "네끗", 11.4
        elif card1 == "삼광" and card2 == "일월":
            return "네끗", 11.4
        elif card1 == "삼월" and card2 == "일광":
            return "네끗", 11.4
        elif card1 == "삼월" and card2 == "일월":
            return "네끗", 11.4

        elif card1 == "오월" and card2 == "팔월":
            return "세끗", 11.5
        elif card1 == "팔월" and card2 == "오월":
            return "세끗", 11.5
        elif card1 == "삼광" and card2 == "십월":
            return "세끗", 11.5
        elif card1 == "삼월" and card2 == "십월":
            return "세끗", 11.5
        elif card1 == "십월" and card2 == "삼광":
            return "세끗", 11.5
        elif card1 == "십월" and card2 == "삼월":
            return "세끗", 11.5
        elif card1 == "사월" and card2 == "구월":
            return "세끗", 11.5
        elif card1 == "구월" and card2 == "사월":
            return "세끗", 11.5
        elif card1 == "육월" and card2 == "칠월":
            return "세끗", 11.5
        elif card1 == "칠월" and card2 == "육월":
            return "세끗", 11.5
        elif card1 == "일광" and card2 == "이월":
            return "세끗", 11.5
        elif card1 == "일월" and card2 == "이월":
            return "세끗", 11.5
        elif card1 == "이월" and card2 == "일월":
            return "세끗", 11.5
        elif card1 == "이월" and card2 == "일광":
            return "세끗", 11.5

        elif card1 == "오월" and card2 == "칠월":
            return "두끗", 11.6
        elif card2 == "칠월" and card2 == "오월":
            return "두끗", 11.6
        elif card1 == "사월" and card2 == "팔월":
            return "두끗", 11.6
        elif card1 == "팔월" and card2 == "사월":
            return "두끗", 11.6
        elif card1 == "사월" and card2 == "팔광":
            return "두끗", 11.6
        elif card1 == "팔광" and card2 == "사월":
            return "두끗", 11.6
        elif card1 == "삼광" and card2 == "구월":
            return "두끗", 11.6
        elif card1 == "삼월" and card2 == "구월":
            return "두끗", 11.6
        elif card1 == "구월" and card2 == "삼광":
            return "두끗", 11.6
        elif card1 == "구월" and card2 == "삼월":
            return "두끗", 11.6
        elif card1 == "이월" and card2 == "십월":
            return "두끗", 11.6
        elif card1 == "십월" and card2 == "이월":
            return "두끗", 11.6

        elif card1 == "오월" and card2 == "육월":
            return "한끗", 11.7
        elif card1 == "육월" and card2 == "오월":
            return "한끗", 11.7
        elif card1 == "사월" and card2 == "칠월":
            return "한끗", 11.7
        elif card1 == "칠월" and card2 == "사월":
            return "한끗", 11.7
        elif card1 == "삼광" and card2 == "팔월":
            return "한끗", 11.7
        elif card1 == "삼월" and card2 == "팔월":
            return "한끗", 11.7
        elif card1 == "팔월" and card2 == "삼월":
            return "한끗", 11.7
        elif card1 == "팔월" and card2 == "삼광":
            return "한끗", 11.7
        elif card1 == "이월" and card2 == "구월":
            return "한끗", 11.7
        elif card1 == "구월" and card2 == "이월":
            return "한끗", 11.7
        elif card1 == "일광" and card2 == "십월":
            return "한끗", 11.7
        elif card1 == "일월" and card2 == "십월":
            return "한끗", 11.7
        elif card1 == "십월" and card2 == "일광":
            return "한끗", 11.7
        elif card1 == "십월" and card2 == "일월":
            return "한끗", 11.7

        # 망통 12등
        elif card1 == "이월" and card2 == "팔월":
            return "망통", 12
        elif card1 == "이월" and card2 == "팔광":
            return "망통", 12
        elif card1 == "팔광" and card2 == "이월":
            return "망통", 12
        elif card1 == "팔월" and card2 == "이월":
            return "망통", 12
        else:
            return "없어"

    def Rank(self, num1, num2, num3, num4):
        a = min(int(num1), int(num2), int(num3), int(num4))
        if a == int(num1):
            if a == int(num2):
                return 0, 1
            elif a == int(num3):
                return 0, 2
            elif a == int(num4):
                return 0, 3
            return 0
        elif a == int(num2):
            if a == int(num1):
                return 1, 0
            elif a == int(num3):
                return 1, 2
            elif a == int(num4):
                return 1, 3
            return 1
        elif a == int(num3):
            if a == int(num2):
                return 2, 1
            elif a == int(num1):
                return 2, 0
            elif a == int(num4):
                return 2, 3
            return 2
        elif a == int(num4):
            if a == int(num2):
                return 3, 1
            elif a == int(num3):
                return 3, 2
            elif a == int(num1):
                return 3, 3
            return 3
        else:
            return "무승부"
