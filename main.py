from discord.ext import commands
import json

description = '''UberBot is run by UberActivist#1085. It uses discord.py.
The source can be found here: https://github.com/UberActivist/UberBot.py-redo'''

global_config = {} # This dict is changed to the loaded json later...

# this specifies what extensions to load when the bot starts up
startup_extensions = ["plugins.members", "plugins.rng", "plugins.misc"]

bot = commands.Bot(command_prefix='&', description=description)

# this loads the config file, converts the json to a dict, saves it globally, then closes the filestream
with open("config.json") as config:
    global_config = json.load(config)

@bot.event
async def on_ready():
    # Print to console that the bot has successfully logged into Discord.
    template = "Logged in as {} {}"
    name = "{}#{}".format(bot.user.name, bot.user.discriminator)
    template = template.format(name, bot.user.id)
    print("Successfully logged into Discord.")
    print(template)
    print('------')

@bot.event
async def on_message(message):
    # Needed for the commands system to work.
    await bot.process_commands(message)

    def format_message(message):
        """This function takes a message object provided by
        discord.py and outputs the message to the console
        as a form of chat log."""
        # Template for what the chat log will look like
        template = "[{}] #{} <{}> {}"
        # Placeholder for server name.
        server = "Private Message"
        # If there is a message.server,
        if message.server is not None:
            # change server to message.server.name
            server = message.server.name
        # If there is a message.attachments,
        if message.attachments:
            # Gather all the attachments objects...
            for i in message.attachments:
                # ...and append their URL to the end of the template message
                template = template + " " + i["url"]
        # If the message content is empty (it's just an attachment with no text)
        if message.clean_content == "":
            # Change the message.content to inform the chat log of such
            message.clean_content = "((User did not send any text with this message.))"
        # Return the template, pefectly formatted and ready to be printed.
        return template.format(server, message.channel.name, message.author.name, message.clean_content)

    # Print the perfectly formatted message.
    print(format_message(message))

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    # If the message author isn't the owner of the bot
    if ctx.message.author.id != global_config["admin"]["owner"]:
        # Tell them to fuck off
        await bot.say("You do not have permission to do that!")
        return
    # Attempt to load the extension
    try:
        bot.load_extension(extension_name)
    # Gracefully handle the error if my code is shit.
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        print("Failed to load {}".format(extension_name))
        return
    await bot.say("{} loaded.".format(extension_name))
    print("Loaded {}".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    # If the message author isn't the bot owner...
    if ctx.message.author.id != global_config["admin"]["owner"]:
        # Tell them to fuck off
        await bot.say("You do not have permission to do that!")
        return
    # Unload that shit
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))
    print("Unloaded {}".format(extension_name))

@bot.command(pass_context=True)
async def reboot(ctx):
    '''Reboots the bot.'''
    #If the message author isn't the bot owner...
    if ctx.message.author.id != global_config["admin"]["owner"]:
        # Tell them to fuck off
        await bot.say("You do not have permission to do that!")
        return
    await bot.say("Rebooting...")
    print("Rebooting...")
    await bot.logout()

@bot.command()
async def info():
    '''Provides basic identifying information about the bot'''
    await bot.say(description)

'''@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)'''

'''@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)'''

# Loads all the extensions on startup.
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(global_config["token"])