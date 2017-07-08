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
        "Welcome to the lottery. Fun fact: you all have a very insignificant chance of winning. GOOD LUCK!",
        "The following person shall be spared when robots eventually conquer the Earth...",
        "Are you ready kids?",
        "Random. Random never changes.",
        "The following person must give up their life to lead the Undertale fandom.",
        "The following person wishes to formally announce their candidacy for president.",
        "The following person has such a spell of good luck that they've completely ran out, and will enjoy 9 years straight of bad luck.",
        "The following person has been chosen as Jill Stein's future Vice President.",
        "Who wants to be randomly chosen?"
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
        await asyncio.sleep(3)
        await self.bot.say("I choose <@{}>".format(option))


def setup(bot):
    bot.add_cog(RNG(bot))
