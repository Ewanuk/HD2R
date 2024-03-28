# bot.py
import os
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
HELLO_WORLD = os.getenv('HELLO_WORLD')

client = commands.Bot(command_prefix='!')

strategems = [
    "Tesla Tower",
    "Mortar Sentry",
    "EMS Mortar Sentry",
    "Machine Gun Sentry",
    "Gatling Sentry",
    "Anti-Personnel Minefield",
    "MD-I4 Incendiary Mines",
    "Shield Generator Relay",
    "HMG Emplacement",
    "Autocannon Sentry",
    "Rocket Sentry",

    "Orbital Precision Strike",
    "Orbital Airbust Strike",
    "Orbital 120MM HE Barrage",
    "Orbital 380MM HE Barrage",
    "Orbital Walking Barrage",
    "Orbital Laser",
    "Orbital Railcannon Strike",
    "Orbital Gatling Barrage",
    "Orbital Gas Strike",
    "Orbital EMS Strike",
    "Orbital Smoke Strike",

    "Eagle Strafing Run",
    "Eagle Airstrike",
    "Eagle Cluster Bomb",
    "Eagle Napalm Strike",
    "Eagle Smoke Strike",
    "Eagle 110MM Rocket Pods",
    "Eagle 500kg Bomb",

    "Guard Dog (Laser)",
    "Guard Dog (Machine Gun)",
    "Jump Pack",
    "Supply Pack",
    "Shield Generator Pack",
    "Ballistic Shield Backpack",

    "Autocannon",
    "Expendable Anti-tank",
    "Flamethrower",
    "Laser Cannon",
    "Stalwart",
    "Machine Gun",
    "Arc Thrower",
    "Grenade Launcher",
    "Anti-Materiel Rifle",
    "Railgun",
    "Recoilless Rifle",
    "SPEAR Launcher",
    "Quasar Cannon",
    "Heavy Machine Gun",

    "Patriot Exosuit",
]

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')

@client.command()
async def roll(ctx):
    results = '\n'.join(random.sample(strategems, 4))
    response = 'your strategems are:\n' + results
    await ctx.send(response)

client.run(TOKEN)