import discord
import asyncio
import bot_plugin

bot = discord.Client()


@bot.event
async def on_ready():
    print("Logged in.")
