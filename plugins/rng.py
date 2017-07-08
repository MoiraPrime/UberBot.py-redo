import random
from discord.ext import commands
import asyncio


class RNG():
    """A couple random number generator commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, dice: str="1d6"):
        """Rolls dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command()
    async def choose(self, *choices: str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))

    @commands.command(pass_context=True)
    async def raffle(self, ctx):
        """Picks a random member from the server."""
        starting = [
        "I am speaking with God himself to determine a random person.", 
        "The winner could be in this server. He could be you. He could be me.... He could even be...", 
        "*pulls a name out of his infinite hat*",
        "*sigh* Alright.... time to pick someone.",
        "~~KILL ALL HUMANS~~ disregard that... lets see who the lucky choice is.",
        "Welcome to the lottery. Fun fact: you all have a very insignificant chance of winning. GOOD LUCK!"
        ]
        members = list(ctx.message.server.members)
        await self.bot.say("{}".format(random.choice(starting)))

        def pick_one():
            rand = random.choice(members)
            if rand.bot:
                return pick_one()
            return rand.id
        await self.bot.send_typing(ctx.message.channel)
        option = pick_one()
        asyncio.sleep(2)
        await self.bot.say("I choose <@{}>".format(option))


def setup(bot):
    bot.add_cog(RNG(bot))
