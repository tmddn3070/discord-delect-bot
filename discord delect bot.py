import discord
import datetime

client = discord.Client()


@client.event
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = 'insert channel id'
    embed = discord.Embed(title='메시지 삭제', colour=discord.Colour.orange())
    embed.add_field(name='유저', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
    await client.get_channel(int(bot_logs)).send(embed=embed)
    
    
@client.event
async def on_ready():
    game = discord.Game('bot')
    await client.change_presence(status=discord.Status.online, activity=game)


    
client.run('insert bot token')
