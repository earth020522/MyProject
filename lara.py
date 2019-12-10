import asyncio
import discord

app=discord.Client()

token="NjUzODQ2OTU4NDA1OTc2MDY0.Xe886A.CZcXwB0EzEuikCyQWDd-wOnfm4U"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==============")
    game = discord.Game("Learning")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.content=="!command":
        channel = message.channel
        await channel.send('Hi')

app.run(token)