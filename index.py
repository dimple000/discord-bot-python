import discord
import asyncio
import datetime
import os

client = discord.Client()

gaming = '지켜보는중'

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game(gaming)
    await client.change_presence(status=discord.Status.online, activity=game)       
    
@client.event
async def on_message(message):
    if message.content.startswith('!청소'):
        try:
            # 메시지 관리 권한 있을시 사용가능
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', colour=discord.Colour.green()))
                await asyncio.sleep(2)
                await message.delete()
            else:
                message = await message.channel.send(embed=discord.Embed(title='🔑 명령어 사용권한이 없습니다. ')),
        except:
            pass

    
@client.event
async def on_message_delete(message):
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    min = datetime.datetime.now().minute
    bot_logs = '815515949318275112'
    embed = discord.Embed(title='메시지 삭제됨', colour=discord.Colour.orange())
    embed.add_field(name='유저', value=f'<@{message.author.id}>({message.author})')
    embed.add_field(name='채널', value=f'<#{message.channel.id}>')
    embed.add_field(name='내용', value=message.content, inline=False)
    embed.add_field(name='날짜', value=f"{y}-{m}-{d} {h}:{min}", inline=False)
    embed.set_footer(text=f"유저 ID:{message.author.id} • 메시지 ID: {message.id}")
    await client.get_channel(int(bot_logs)).send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
