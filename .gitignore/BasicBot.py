# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
import random
from discord.ext.commands import Bot
from discord.ext import commands
import platform
random.seed()

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="$", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	return await client.change_presence(game=discord.Game(name='Inpirational Quotes')) #This is buggy, let us know if it doesn't work.


# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
@client.command(pass_context=True)
async def inspire(ctx):
        imgNum = str(random.randrange(1, 9998))
        folderNum = random.randrange(1,81)
        folderNum = str(format(folderNum, '03d'))
        imgLink = "http://generated.inspirobot.me/" + folderNum + "/aXm" +  imgNum + "xjU.jpg"
        folderLink = "http://generated.inspirobot.me/" + folderNum
        await client.say(imgLink)
        await client.send_file(ctx.message.channel, imgLink)
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('NDYwNzM3MDA1MTgyMTI0MDMy.DhJM3g.tYnnsZzz_DEJSaSc9E4zotPAScs')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
