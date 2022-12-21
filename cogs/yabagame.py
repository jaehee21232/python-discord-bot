import discord
from discord.ext import commands


class smallgame(commands.Cog):
    def __init__(self, app):
        self.app = app

    @commands.command(name="야바위")
    async def test(self, ctx):
        embed = discord.Embed(
            title="야바위게임", description="⚾  🏀  ⚽\n\n  고르세요!", color=0x62c1cc)
        msg = await ctx.channel.send(embed=embed)
        mmm = await msg.add_reaction("⚾")
        await msg.add_reaction("🏀")
        await msg.add_reaction("⚽")


def setup(app):
    app.add_cog(smallgame(app))
    print("앙 smallgame.py 준비완료!")
