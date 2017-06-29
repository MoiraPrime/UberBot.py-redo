from discord.ext import commands
import json

description = '''WIP'''
global_config = {}

# this specifies what extensions to load when the bot starts up
startup_extensions = ["plugins.fp_members", "plugins.rng", "plugins.misc"]

bot = commands.Bot(command_prefix='&', description=description)

with open("config.json") as config:
    global_config = json.load(config)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    def format_message(message):
        if message.server is None:
            template = "[Private Message] <{}> {}"
            return template.format(message.author.name, message.content)
        template = "[{}] #{} <{}> {}"
        return template.format(message.server.name, message.channel.name, message.author.name, message.content)

    print( format_message(message) )

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command(pass_context=True)
async def reboot(ctx):
    if ctx.message.author.id != global_config["admin"]["owner"]:
        await bot.say("You do not have permission to do that!")
        return
    await bot.say("Rebooting...")
    await bot.logout()

'''@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)'''

'''@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)'''

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(global_config["token"])