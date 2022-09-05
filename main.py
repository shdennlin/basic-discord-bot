import os

import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", bot=True, intents=intents)
load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")


@bot.event
async def on_ready():
    print(f"The {bot.user.name} is ready")


@bot.command()
@commands.has_permissions(send_messages=True)
async def echo(ctx, *, msg):
    await ctx.send(msg)


async def cronjob(ctx, channel_id, msg, sleep_time):
    while True:
        await bot.get_channel(channel_id).send(msg)
        # await channel.edit(name=f'Member Count: {ctx.guild.member_count}')
        await asyncio.sleep(sleep_time)


@bot.command()
@commands.has_permissions(send_messages=True)
async def broadcast(ctx, channel: discord.TextChannel, msg, sleep_time: int):
    task = bot.loop.create_task(cronjob(ctx, channel.id, msg, sleep_time),
                                name=f"channel:#{channel.name} msg:{msg} sleep_time:{sleep_time}s")


@bot.command()
@commands.has_permissions(send_messages=True)
async def get_broadcast(ctx):
    msg = ""
    for task in asyncio.all_tasks():
        id = task.get_coro().__str__()
        if "cronjob" in id:
            id = id.split()[-1]
            id = id[:-1]
            msg += f"id:{id} {task.get_name()}" + "\n"
    await ctx.send(msg)


@bot.command()
@commands.has_permissions(send_messages=True)
async def cancel_broadcast(ctx, task_id: str):
    for task in asyncio.all_tasks():
        id = task.get_coro().__str__()
        if "cronjob" in id:
            id = id.split()[-1]
            id = id[:-1]
            if id == task_id:
                task.cancel()
                await ctx.send(f"Task {task_id} has been canceled")
                return
    await ctx.send(f"Task {task_id} not found")


@bot.command()
@commands.has_permissions(send_messages=True)
async def cancel_all_broadcast(ctx):
    for task in asyncio.all_tasks():
        id = task.get_coro().__str__()
        if "cronjob" in id:
            task.cancel()
    await ctx.send(f"All tasks have been canceled")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating a new channel: {channel_name}")
        await guild.create_text_channel(channel_name)
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="channel:", value=f"""
The channel **{channel_name}** has been created.
""", inline=True)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="channel:", value=f"""
The channel **{channel_name}** already exists.
""", inline=True)
        await ctx.reply(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason"):
    try:
        await user.kick(reason=reason)
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="kicked:", value=f"""
The user **{user}** has been kicked from the server.
Reason = **{reason}**
""", inline=True)
        await ctx.reply(embed=embed)
    except Exception as e:
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="kicked:", value=f"Error", inline=True)
        await ctx.reply(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason"):
    try:
        await user.ban(reason=reason)
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="banned:", value=f"""
The user **{user}** has been banned from the server.
Reason = **{reason}**
""", inline=True)
        await ctx.reply(embed=embed)
    except Exception as e:
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="banned:", value=f"Error", inline=True)
        await ctx.reply(embed=embed)

bot.run(token)
