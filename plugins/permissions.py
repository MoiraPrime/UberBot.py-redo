import discord
from discord.ext import commands
import permcommons

class permissions():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def myaccess(self):
        pass

def setup(bot):
    bot.add_cog(permissions(bot))
