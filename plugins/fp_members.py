import discord
from discord.ext import commands

class fpmembers():
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        if member.server.id != "149707514521321473":
            return
        template = "Everyone welcome <@{}> to the FirePowered Discord server! This brings our total number of members to {}."
        template = template.format(member.id, member.server.member_count)
        await self.bot.send_message(self.bot.get_channel("158357071815901184"), template)

    async def on_member_remove(self, member):
        if member.server.id != "149707514521321473":
            return
        template = "Aww! It looks like {} is no longer a member of our server. This brings our total number of members to {}."
        template = template.format(member.name, member.server.member_count)
        await self.bot.send_message(self.bot.get_channel("158357071815901184"), template)

    @commands.command(pass_context=True)
    async def members(self, ctx):
        if ctx.message.channel.is_private:
            return
        template = "There are {} members in this server.".format(ctx.message.author.server.member_count)
        await self.bot.say(template)

    @commands.command(pass_context=True)
    async def joinedat(self, ctx, member: discord.Member = None):
        if ctx.message.channel.is_private:
            return
        if member is None:
            member = ctx.message.author
        template = "{0} joined at {0.joined_at}".format(member)
        await self.bot.say(template)




def setup(bot):
    bot.add_cog(fpmembers(bot))