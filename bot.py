import discord
from discord import app_commands
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="calc", description="Add/subtract from x, y, z values")
@app_commands.describe(x="Value for x (adds 29)", y="Value for y (subtracts 32)", z="Value for z (adds 52)")
async def calc(interaction: discord.Interaction, x: float, y: float, z: float):
    x_out = x + 29
    y_out = y - 32
    z_out = z + 52
    embed = discord.Embed(title="Calculation Results", color=0x57f287)
    embed.add_field(name=f"x ({x} + 29)", value=str(x_out), inline=False)
    embed.add_field(name=f"y ({y} − 32)", value=str(y_out), inline=False)
    embed.add_field(name=f"z ({z} + 52)", value=str(z_out), inline=False)
    embed.set_footer(text=f"Output → {x_out}, {y_out}, {z_out}")
    await interaction.response.send_message(embed=embed)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

import os
client.run(os.environ['TOKEN'])
