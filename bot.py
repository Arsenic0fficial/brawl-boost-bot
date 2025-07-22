import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

TOKEN = os.getenv("TOKEN")  # Token will be set in Railway

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Sync error: {e}")

# Example slash command
@bot.tree.command(name="ping", description="Check bot latency.")
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Latency: {round(bot.latency * 1000)}ms")

bot.run(TOKEN)