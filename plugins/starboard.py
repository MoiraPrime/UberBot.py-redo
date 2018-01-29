from discord.ext import commands
import discord
import asyncio

restricted = ["246758392411062272", "150752714362585088", "284903283770785792", "406279148932431872", "397963636464943105", "405135937912438804"]

class starboard():
    """Firepowered Server starboard plugin."""
    def __init__(self, bot):
        self.bot = bot

    async def on_reaction_add(self, reaction, member):
        if reaction.message.server.id != "149707514521321473":
            return
        if reaction.message.channel.id in restricted:
            return
        for i in reaction.message.reactions:
            if i.name == "x" and i.me:
                return
        if reaction.message.author.id == member.id:
            async self.bot.add_reaction(reaction.message, "❌")
            return

        if reaction.count > 5 or reaction.count < 5:
            return

        embed=discord.Embed(color=0xff8000, description=reaction.message.content)
        embed.set_author(name=reaction.message.author.name,, icon_url=reaction.message.author.avatar_url)
        if len(reaction.message.attachments) > 0:
            embed.set_image(url=reaction.message.attachments[0].url)
        date = reaction.message.timestamp.date
        time = reaction.message.timestamp.time
        embed.set_footer(text="{}/{}/{} at {}:{} in <#{}>.".format(date.month, date.day, date.year, time.hour, time.minute, reaction.message.channel.id))
        await await client.send_message(client.get_channel('405135937912438804'), embed=embed)


def setup(bot):
    bot.add_cog(starboard(bot))
