import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send("!사진 [ 등급표.png 또는 양식.png ] , !멘션 서버장")
    
    if message.content.startswith("!멘션 서버장"):
        await message.channel.send("<@672664501635776534>님을 불러오는중입니다.")

    if message.content.startswith("!멘션 문기"):
        await message.channel.send("<@339770810040451073>님을 불러오는중입니다.")

    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])
    
    if message.content.startswith("!청소"):
            number = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit=number)
            await message.channel.send(f"{number}개의 메세지 삭제가 완료되었습니다.!")

client.run("ODU5NzU0NDg2NDY0OTA1MjU2.YNxSww.RHhM_eNTqv1VDrZMY5aEpeBENaA")