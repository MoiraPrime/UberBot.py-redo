import random
import discord
from discord.ext import commands

class misc():
    """Commands that don't fit into any other category"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def csi(self):
        """Generates a random 'techy' sounding jargon sentence based on the poor writing found on CSI: Cyber"""
        start = ['The first thing we need to do is ','To fix your problem, we have to ','The hackers are getting in! Quickly, ','To get in to the government database we\'re going to ','Quickly! We have to ','We can get rid of the virus, don\'t worry. First we have to ']
        verb = ['reroute','splice','compile','reprocess','log','port','decrypt','encrypt','recode','refactor','import','export','modify','uninstall','install','upload','download','open','decode','push','recompile','decompile','write a GUI to track','trace','troubleshoot']
        noun = [' the VGA cable',' the USB',' the browser',' the interface',' the Internet',' the IP address',' the source code',' the hard drive',' the RAM',' the CPU',' the motherboard',' the monitor',' the shortcut',' the LAN',' the Wi-Fi',' the CAT5',' the Bluetooth',' the program',' the encryption',' the compiler',' the IDE',' Linux',' Microsoft Word',' the Google',' the traceroute',' the stack',' C++',' Java',' JavaScript',' C',' C#',' Python',' the programming language',' the SATA cable',' the subnet mask',' the Ethernet',' the Ethernet adapter',' the GPU',' the keyboard',' Internet Explorer',' Ubuntu',' the command prompt',' the command line',' HTTPS',' FTP',' SSH',' Visual Basic']
        preposition = [' through',' into',' with',' on']

        def pickOne (list):
            return random.choice(list)

        def doList ():
            template = "{}{}{}{}{}."
            return template.format(pickOne(start), pickOne(verb), pickOne(noun), pickOne(preposition), pickOne(noun))
        await self.bot.say(doList())

    @commands.command(pass_context=True)
    async def raffle(self, ctx):
        members = ctx.message.server.members
        def choose_one():
            rand = random.choice(members)
            return rand
        self.bot.say("I choose <@{}>".format(choose_one().id))



def setup(bot):
    bot.add_cog(misc(bot))