import discord
from discord.ext import commands
import random
import config

ketobotlogo="""
 _  __    _        ____        _   
| |/ /___| |_ ___ | __ )  ___ | |_ 
| . // _ \ __/ _ \|  _ \ / _ \| __|
| . \ __/ ||  (_) | |_) | (_) | |_ 
|_|\_\___|\__\___/|____/ \___/ \__|
"""
print(ketobotlogo)

bot = commands.Bot(command_prefix=config.prefix)
bot.remove_command("help")
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=";help | Keylogging Keto"))
    print('------')
    print('Ready!')
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print('------')
    print('Connected to:')
    for server in bot.guilds:
        print(' ')
        print(server.name)
        print(server.id)
    print('------')
    print('© Toilet Cat Technologies')
    print('------')
 
try:
    async def self_check(ctx):
        if 637090083144728576 == ctx.message.author.id:
            return True
        else:
            return False
    # A secondary check to ensure nobody but the owner can run these commands.
    # @commands.check(self_check)
    import quotes
    @bot.command(pass_context=True)
    async def quote(ctx):
        messages = quotes.keto
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} requested a quote in {ctx.guild.name}!")
    # Keto Quotes
 
    @bot.command()
    async def help(ctx):
        embed=discord.Embed(title="Keto Bot", url="https://toilet.cat/", description="Quoting Keto since 2019.")
        embed.set_thumbnail(url="https://raw.githubusercontent.com/xstecky/Keto-Bot/master/ketoflake.png")
        embed.add_field(name="Send one of Keto's finest quotes.", value=";quote", inline=False)
        embed.add_field(name="Ask the magic 8-Ball a question.", value=";m8b [question]", inline=False)
        embed.add_field(name="Links the Keto Bot repository.", value=";github", inline=False)
        embed.add_field(name="Make Keto say something. (Owner only)", value=";say [text]", inline=False)
        embed.add_field(name="Change the game status. (Owner only)", value=";changegame [text]", inline=False)
        embed.set_footer(text="© Toilet Cat Technologies") 
        await ctx.send(embed=embed)
        print (f"{ctx.message.author.name} requested the help embed in {ctx.guild.name}!")
    # Help Embed

    @bot.command(pass_context=True)
    async def m8b(ctx):
        messages = ["Yes.", "No.", "Ask Gordo.", "Absolutely.", "Fuck no."]
        await ctx.send(random.choice(messages))
        print (f"{ctx.message.author.name} used the magic 8-Ball in {ctx.guild.name}! ({ctx.message.content})")
    # 8-Ball

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def say(ctx, *, text):
        await ctx.send(text)
        print (f"{ctx.message.author.name} used the say command in {ctx.guild.name}! ({ctx.message.content})")
    # Say

    @bot.command(pass_context=True)
    async def github(ctx):
        await ctx.send('https://github.com/xstecky/Keto-Bot')
        print (f"{ctx.message.author.name} requested the GitHub URL in {ctx.guild.name}!")
    # GitHub

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def changegame(ctx, *, text):
        await bot.change_presence(activity=discord.Game(name=(text)))
        await ctx.send('done :zany_face:')
        print (f"{ctx.message.author.name} changed Keto's status in {ctx.guild.name}! ({ctx.message.content})")
    # Change Game

except:
    pass
import config
bot.run(config.token, bot=True)
