import ang
import random
import json
import discord
import user_data
import seosda_data
from ang import Jusig
from discord.ext import tasks
from datetime import datetime
from seosda_data import Deck, Seosda

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# 오늘 날짜
today = datetime.now()

# 디스코드 봇의 고유 토큰
TOKEN = config['discord_bot_token']
app = discord.Client(intents=intents)

hansei_bank_money = 1000


@app.event
async def on_ready():
    ang.hansei_bank = Jusig.jusigone()
    ang.jaeheedang = Jusig.jusigtwo()
    chcange_status.start()
    print("ready")


@tasks.loop(seconds=1)
async def chcange_status():
    ang.jutime -= 1
    if int(ang.jutime) == 0:
        Jusig.jusigone()
        Jusig.jusigtwo()
        ang.jutime = 180
        print("3분이 되어서 주식을 새로고침합니다.")


@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("!앙"):
        num = []
        Seosda.Seleteid()
        Seosda.Seletename()
        for p in seosda_data.a:
            author = await app.fetch_user(int(p))
            a1 = Deck.GiveCard(1)
            player1 = discord.Embed(
                title="첫번째 패", description="", color=0x62c1cc)
            player1.set_thumbnail(url=a1[0])
            await author.send(embed=player1)
            Seosda.changeone(p, seosda_data.n[0], Deck.CardCheck(a1[0]), Deck.CardCheck(
                a1[1]), Deck.Cardmain(Deck.CardCheck(a1[0]), Deck.CardCheck(a1[1]))[0])
            num.append(Deck.Cardmain(Deck.CardCheck(
                a1[0]), Deck.CardCheck(a1[1]))[1])
            user_data.User_Data.Selete_money(int(seosda_data.a[0]))
            p1 = int(user_data.money[0])
            user_data.User_Data.change_user(
                seosda_data.n[0], int(seosda_data.a[0]), p1-500)
            a2 = Deck.GiveCard(2)
            player1 = discord.Embed(
                title="첫번째 패", description="", color=0x62c1cc)
            player1.set_thumbnail(url=a2[0])
            await author.send(embed=player1)
            Seosda.changeone(p, seosda_data.n[1], Deck.CardCheck(a2[0]), Deck.CardCheck(
                a2[1]), Deck.Cardmain(Deck.CardCheck(a2[0]), Deck.CardCheck(a2[1]))[0])
            num.append(Deck.Cardmain(Deck.CardCheck(
                a2[0]), Deck.CardCheck(a2[1]))[1])
            user_data.User_Data.Selete_money(int(seosda_data.a[1]))
            p1 = int(user_data.money[1])
            user_data.User_Data.change_user(
                seosda_data.n[1], int(seosda_data.a[1]), p1-500)

    if message.content.startswith('!주식 시장'):
        embed = discord.Embed(title="", description="{}\n{}".format(
            ang.hansei_bank, ang.jaeheedang))
        embed.set_footer(text="갱신까지 남은시간 {}초".format(ang.jutime))
        await message.channel.send(embed=embed)

    if message.content.startswith("!매수"):
        if user_data.User_Data.check(message.author.id) == False:
            jusigmsg = message.content[4:]
            종목 = str(jusigmsg.split(" ")[0])
            수량 = jusigmsg.split(" ")[1]
            print(ang.hansei_bank_money)
            try:
                if int(수량) == int(수량):
                    수량 = int(수량)
            except:
                await message.channel.send("매수할 개수는 정수여야 합니다.")
            else:
                juju = Jusig.jucheck(message.author.id)
                if int(user_data.User_Data.Selete_money(message.author.id)) >= (int(ang.hansei_bank_money) * int(수량)):
                    if juju == True:
                        if 종목 == "한세은행":
                            print("한세은행")
                            Jusig.upjusign(message.author.id, message.author.name, 종목, (int(
                                Jusig.Selete_money(message.author.id, "한세은행"))+수량))
                            await message.channel.send("{}님 {}을 {}주 만큼 매수하셨습니다.".format(message.author.name, 종목, 수량))
                            user_data.User_Data.change_user(message.author.name, message.author.id, (int(
                                user_data.User_Data.Selete_money(message.author.id)) - (int(Jusig.Seletejusig("한세은행")) * int(수량))))
                        if 종목 == "재희재당":
                            print("재희재당")
                            Jusig.upjusign(message.author.id, message.author.name, 종목, (int(
                                Jusig.Selete_money(message.author.id, "재희재당"))+수량))
                            await message.channel.send("{}님 {}을 {}주 만큼 매수하셨습니다.".format(message.author.name, 종목, 수량))
                            user_data.User_Data.change_user(message.author.name, message.author.id, (int(
                                user_data.User_Data.Selete_money(message.author.id)) - (int(Jusig.Seletejusig("재희재당")) * int(수량))))
                    if juju == False:
                        if 종목 == "한세은행":
                            Jusig.maesosign(message.author.id,
                                            message.author.name, 종목, 수량)
                            await message.channel.send("{}님 {}을 {}주 만큼 매수하셨습니다.".format(message.author.name, 종목, 수량))
                        if 종목 == "재희재당":
                            Jusig.maesosign(message.author.id,
                                            message.author.name, 종목, 수량)
                            await message.channel.send("{}님 {}을 {}주 만큼 매수하셨습니다.".format(message.author.name, 종목, 수량))
                else:
                    await message.channel.send("{}님 돈이 부족합니다".format(message.author.name))
        else:
            await message.channel.send("회원가입후 이용해주세요.")  # 회원가입을 안했으면 실행이 안됨

    if message.content.startswith("!프로필"):  # !프로필이라고 칠 경우
        if user_data.User_Data.check(message.author.id) == False:  # 회원가입을 했을 경우
            # 제목은 프로필 부가설명은 친사람의 이름
            embed = discord.Embed(
                title="프로필", description=message.author.name, color=0x62c1cc)
            embed.add_field(name="돈", value=user_data.User_Data.Selete_money(
                message.author.id), inline=True)  # 두번째 설명에 "돈"과 돈을 출력해줌
            # 밑에 만든사람과 오늘날짜
            embed.set_footer(text=f"by 나.천.사 | {today.date().isoformat()}")
            msg = await message.channel.send(embed=embed)
            user_data.money = []
        else:
            await message.channel.send("회원가입후 이용해주세요.")  # 회원가입을 안했으면 실행이 안됨

    if message.content.startswith('!섯다'):
        if seosda_data.s == 0:
            Seosda.Data_delete()
            embed = discord.Embed(
                title="섯다", description="참가하실분은 아래 ✋를 눌러주세요\n 4명이 모이면 시작합니다", color=0x62c1cc)
            msg = await message.channel.send(embed=embed, delete_after=100)
            await msg.add_reaction("✋")
            seosda_data.Seosda_player = 0
            seosda_data.a = []
            random.shuffle(seosda_data.Seosda_Card)
            seosda_data.s += 1
        else:
            await message.channel.send("게임이 진행 중입니다.")

    if message.content.startswith("!회원가입"):
        print(message.author.name)
        print(message.author.id)
        if user_data.User_Data.check(message.author.id) == False:
            await message.channel.send("이미 가입한 사용자입니다")
        # 이미 가입했으면 "이미 가입한 사용자입니다" 출력 가입 안했으면 회원가입 시킴
        if user_data.User_Data.check(message.author.id) == True:
            user_data.User_Data.sign(
                message.author.name, message.author.id, 10000)
            await message.channel.send("회원가입 완료!")

    @app.event
    async def on_reaction_add(reaction, user):
        if user.bot == 1:  # 봇이면 패스
            return None
        if str(reaction.emoji) == "✋":
            if user_data.User_Data.check(user.id) == False:
                user_data.User_Data.Selete_money(user.id)
                if int(user_data.money[0]) > 2000:
                    user_data.money = []
                    if Seosda.seosdacheck(user.id) == True:
                        print(user.name, "은 참가한 상태")
                    if Seosda.seosdacheck(user.id) == False:
                        Seosda.seosdasign(user.id, user.name, 0, 0, 0)
                        seosda_data.Seosda_player += 1
                        if seosda_data.Seosda_player == 4:
                            await message.channel.purge(limit=int(1))
                            await message.channel.send("플레이어가 모두 모여서 게임을 시작합니다.")
                            print("플레이어가 모두 모여서 섯다를 시작합니다.")
                            Seosda.Seleteid()
                            embed = discord.Embed(
                                title="게임룰", description="", color=0x62c1cc)
                            embed.set_image(
                                url="https://hangame-images.toastoven.net/hangame/renewal_2011/gostop/guide/gssudda/img_guide1_3.jpg",)
                            await message.channel.send(embed=embed)
                            play_p = 0
                            num = []
                            Seosda.Seleteid()
                            Seosda.Seletename()
                            for p in seosda_data.a:
                                play_p += 1
                                author = await app.fetch_user(int(p))
                                if play_p == 1:
                                    a1 = Deck.GiveCard(1)
                                    player1 = discord.Embed(
                                        title="첫번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=a1[0])
                                    await author.send(embed=player1)
                                    Seosda.changeone(p, seosda_data.n[0], Deck.CardCheck(a1[0]), Deck.CardCheck(
                                        a1[1]), Deck.Cardmain(Deck.CardCheck(a1[0]), Deck.CardCheck(a1[1]))[0])
                                    num.append(Deck.Cardmain(Deck.CardCheck(
                                        a1[0]), Deck.CardCheck(a1[1]))[1])
                                    user_data.User_Data.Selete_money(
                                        int(seosda_data.a[0]))
                                    p1 = int(user_data.money[0])
                                    user_data.User_Data.change_user(
                                        seosda_data.n[0], int(seosda_data.a[0]), p1-500)
                                if play_p == 2:
                                    a2 = Deck.GiveCard(2)
                                    player1 = discord.Embed(
                                        title="첫번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=a2[0])
                                    await author.send(embed=player1)
                                    Seosda.changeone(p, seosda_data.n[1], Deck.CardCheck(a2[0]), Deck.CardCheck(
                                        a2[1]), Deck.Cardmain(Deck.CardCheck(a2[0]), Deck.CardCheck(a2[1]))[0])
                                    num.append(Deck.Cardmain(Deck.CardCheck(
                                        a2[0]), Deck.CardCheck(a2[1]))[1])
                                    user_data.User_Data.Selete_money(
                                        int(seosda_data.a[1]))
                                    p1 = int(user_data.money[1])
                                    user_data.User_Data.change_user(
                                        seosda_data.n[1], int(seosda_data.a[1]), p1-500)
                                if play_p == 3:
                                    a3 = Deck.GiveCard(3)
                                    player1 = discord.Embed(
                                        title="첫번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=a2[0])
                                    await author.send(embed=player1)
                                    Seosda.changeone(p, seosda_data.n[2], Deck.CardCheck(a3[0]), Deck.CardCheck(
                                        a3[1]), Deck.Cardmain(Deck.CardCheck(a3[0]), Deck.CardCheck(a3[1]))[0])
                                    user_data.User_Data.Selete_money(
                                        int(seosda_data.a[2]))
                                    p3 = int(user_data.money[2])
                                    num.append(Deck.Cardmain(Deck.CardCheck(
                                        a3[0]), Deck.CardCheck(a3[1]))[1])
                                    user_data.User_Data.change_user(
                                        seosda_data.n[2], int(seosda_data.a[2]), p3-500)
                                    play_p += 1
                                if play_p == 4:
                                    a4 = Deck.GiveCard(4)
                                    player1 = discord.Embed(
                                        title="첫번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=a4[0])
                                    await author.send(embed=player1)
                                    Seosda.changeone(p, seosda_data.n[3], Deck.CardCheck(a4[0]), Deck.CardCheck(
                                        a4[1]), Deck.Cardmain(Deck.CardCheck(a4[0]), Deck.CardCheck(a4[1]))[0])
                                    user_data.User_Data.Selete_money(
                                        int(seosda_data.a[3]))
                                    p4 = int(user_data.money[3])
                                    num.append(Deck.Cardmain(Deck.CardCheck(
                                        a4[0]), Deck.CardCheck(a4[1]))[1])
                                    user_data.User_Data.change_user(
                                        seosda_data.n[3], int(seosda_data.a[3]), p4-500)
                            bet = discord.Embed(
                                title="베팅  기본500  최대 10만", description="콜: 앞 사람이 베팅한 금액만큼 레이스 머니를 받습니다.\n\n 다이: 죽습니다.\n\n 하프: 최대 배팅액의 1/2를 베팅합니다.\n\n ", color=0x62c1cc)
                            ab = 2000
                            P_bet = 500
                            await message.channel.send(embed=bet)
                            Seosda.Seletename()
                            for p in range(0, 4):
                                bet = discord.Embed(title=" {}님 베팅해주세요.\n\n 현재 총 베팅액: {}".format(
                                    seosda_data.n[p], ab), description="ex) 콜", color=0x62c1cc)
                                await message.channel.send(embed=bet)

                                def check(m):
                                    return (m.content == "하프" or m.content == "다이" or m.content == "콜") and m.author.id == int(seosda_data.a[p])
                                msg = await app.wait_for('message', check=check)
                                user_rsp = str(msg.content)
                                if msg.author.id == int(seosda_data.a[p]):
                                    if user_rsp == "하프":
                                        await message.channel.send('하프')
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > 50000:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-50000)
                                            ab += 50000
                                            P_bet = 50000
                                        else:
                                            await message.channel.send("돈이 부족합니다. 다시 베팅해주세요.")

                                            def check(m):
                                                return m.channel == message.channel and m.author.id == int(seosda_data.a[p])
                                            H_msg = await app.wait_for('message', check=check)
                                            H_M = str(H_msg.content)
                                            if H_M == "다이":
                                                embed = discord.Embed(title="{}님이 죽을때 까지 섯다입니다.".format(
                                                    seosda_data.n[p]), description="", color=0x62c1cc)
                                                await message.channel.send(embed=embed)
                                                user_data.User_Data.Selete_money(
                                                    int(seosda_data.a[p]))
                                                mm = int(user_data.money[p])
                                                if mm > P_bet:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                                    ab += 500
                                                    P_bet = 500
                                                else:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                                    ab += mm
                                                    P_bet = mm
                                            elif H_M == "콜":
                                                user_data.User_Data.Selete_money(
                                                    int(seosda_data.a[p]))
                                                mm = int(user_data.money[p])
                                                print(
                                                    "현재 베팅액: {}".format(P_bet))
                                                if mm > P_bet:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                                    ab += 500
                                                else:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                                    ab += mm
                                    elif user_rsp == "다이":
                                        embed = discord.Embed(title="{}님이 죽을때 까지 섯다입니다.".format(
                                            seosda_data.n[p]), description="", color=0x62c1cc)
                                        await message.channel.send(embed=embed)
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > P_bet:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                            ab += 500
                                            P_bet = 500
                                        else:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                            ab += mm
                                            P_bet = mm
                                    elif user_rsp == "콜":
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > P_bet:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                            ab += 500
                            embed = discord.Embed(title="총 배팅액: {}".format(
                                ab), description="", color=0x62c1cc)
                            await message.channel.send(embed=embed)
                            embed = discord.Embed(
                                title="섯다", description="두번째 카드를 오픈합니다.", color=0x62c1cc)
                            await message.channel.send(embed=embed)
                            play_p = 0
                            for p in seosda_data.a:
                                play_p += 1
                                author = await app.fetch_user(int(p))
                                await author.send(embed=embed)
                                if play_p == 1:
                                    C = Deck.GiveCard(1)
                                    player1 = discord.Embed(
                                        title="두번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=C[1])
                                    await author.send(embed=player1)
                                if play_p == 2:
                                    C = Deck.GiveCard(2)
                                    player1 = discord.Embed(
                                        title="두번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=C[1])
                                    await author.send(embed=player1)
                                if play_p == 3:
                                    C = Deck.GiveCard(3)
                                    player1 = discord.Embed(
                                        title="두번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=C[1])
                                    await author.send(embed=player1)
                                if play_p == 4:
                                    C = Deck.GiveCard(4)
                                    player1 = discord.Embed(
                                        title="두번째 패", description="", color=0x62c1cc)
                                    player1.set_thumbnail(url=C[1])
                                    await author.send(embed=player1)
                            for p in range(seosda_data.Seosda_player):
                                bet = discord.Embed(title="{}님 베팅해주세요.\n\n 총 베팅액: {}".format(
                                    seosda_data.n[p], ab), description="ex) 콜", color=0x62c1cc)
                                await message.channel.send(embed=bet)

                                def check(m):
                                    return (m.content == "하프" or m.content == "다이" or m.content == "콜") and m.author.id == int(seosda_data.a[p])
                                msg = await app.wait_for('message', check=check)
                                user_rsp = str(msg.content)
                                if msg.author.id == int(seosda_data.a[p]):
                                    if user_rsp == "하프":
                                        await message.channel.send('하프')
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > 50000:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-50000)
                                            ab += 50000
                                            P_bet = 50000
                                        else:
                                            await message.channel.send("돈이 부족합니다. 다시 베팅해주세요.")

                                            def check(m):
                                                return m.channel == message.channel and m.author.id == int(seosda_data.a[p])
                                            H_msg = await app.wait_for('message', check=check)
                                            H_M = str(H_msg.content)
                                            if H_M == "다이":
                                                embed = discord.Embed(title="{}님이 죽을때 까지 섯다입니다.".format(
                                                    seosda_data.n[p]), description="", color=0x62c1cc)
                                                await message.channel.send(embed=embed)
                                                user_data.User_Data.Selete_money(
                                                    int(seosda_data.a[p]))
                                                mm = int(user_data.money[p])
                                                if mm > P_bet:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                                    ab += 500
                                                    P_bet = 500
                                                else:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                                    ab += mm
                                                    P_bet = mm
                                            elif H_M == "콜":
                                                user_data.User_Data.Selete_money(
                                                    int(seosda_data.a[p]))
                                                mm = int(user_data.money[p])
                                                print(
                                                    "현재 베팅액: {}".format(P_bet))
                                                if mm > P_bet:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                                    ab += 500
                                                else:
                                                    user_data.User_Data.change_user(
                                                        seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                                    ab += mm
                                    elif user_rsp == "다이":
                                        embed = discord.Embed(title="{}님이 죽을때 까지 섯다입니다.".format(
                                            seosda_data.n[p]), description="", color=0x62c1cc)
                                        await message.channel.send(embed=embed)
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > P_bet:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                            ab += 500
                                            P_bet = 500
                                        else:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-mm)
                                            ab += mm
                                            P_bet = mm
                                    elif user_rsp == "콜":
                                        user_data.User_Data.Selete_money(
                                            int(seosda_data.a[p]))
                                        mm = int(user_data.money[p])
                                        if mm > P_bet:
                                            user_data.User_Data.change_user(
                                                seosda_data.n[p], int(seosda_data.a[p]), mm-P_bet)
                                            ab += 500
                            beta = discord.Embed(title="총 배팅액: {}".format(
                                ab), description="", color=0x62c1cc)
                            await message.channel.send(embed=beta)
                            Seosda.SeleteDeck()
                            if Deck.Rank(num[0], num[1], num[2], num[3]) == "무승부":
                                winner = "무승부"
                            else:
                                winner = seosda_data.n[Deck.Rank(
                                    num[0], num[1], num[2], num[3])]
                            embed = discord.Embed(title=" 결과", description="\n{}님: ({})\n\n {}님: ({})\n\n {}님: ({})\n\n {}님: ({})".format(
                                seosda_data.n[0], seosda_data.D[0], seosda_data.n[1], seosda_data.D[
                                    1], seosda_data.n[2], seosda_data.D[2], seosda_data.n[3], seosda_data.D[3]
                            ), color=0x62c1cc)
                            await message.channel.send(embed=embed)
                            await message.channel.send("{}".format(winner))
                else:
                    await message.channel.send("{}님 돈이 부족합니다.".format(user.name))
            else:
                await message.channel.send("{}님 회원가입후 이용해주세요.".format(user.name))

        if str(reaction.emoji) == "⚽":
            await message.delete()
            await message.channel.purge(limit=int(1))
            mnm = random.choice([1, 2, 3])
            if mnm == 1:
                embed = discord.Embed(title="성공", color=0x62c1cc)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="실패", color=0x62c1cc)
                await message.channel.send(embed=embed)

app.run(TOKEN)
