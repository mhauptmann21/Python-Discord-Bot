import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Set up logging
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

secret_role = "Premium Member"

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}!")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if ("shit")  in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please watch your language!")

    if ("fuck")  in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please watch your language!")

    if ("bitch")  in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, please watch your language!")

    if ("python_bot")  in message.content.lower():
        await message.channel.send(f"{message.author.mention}, do you need any help?")

    await bot.process_commands(message)

# /hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

# /assign
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention}, you have been assigned the {secret_role} role!")
    else:
        await ctx.send("Role not found. Please contact an administrator.")

# /remove
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention}, the {secret_role} role has been removed from you.")
    else:
        await ctx.send("Role not found. Please contact an administrator.")

# /dm
@bot.command()
async def dm(ctx, *, message):
    await ctx.author.send(f"You said {message}")
    await ctx.send(f"{ctx.author.mention}, I have sent you a DM with your message!")

# /reply
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message!")

# /poll
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

# /secret
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send(f"{ctx.author.mention}, welcome to the club!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"{ctx.author.mention}, you do not have the required role to access this command.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
