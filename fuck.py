#!/usr/bin/env python3

from __future__ import print_function
from discord.utils import get

import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("!도움말")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!도움말"):
        await message.channel.send("```!play [노래 제목/유튜브 링크] / !skip```")
    if message.content.startswith("!ㅎㅇ"):
        await message.channel.send("ㅎㅇ")
    if message.content.startswith("!엄준식"):
        await message.channel.send("'Still Alive'")
    if message.content.startswith("!민재랑 야스"):
        await message.channel.send("섹1스 하고싶다")
    if message.content.startswith("ㄱㄴ"):
        await message.channel.send("민재♡예진")
    if message.content.startswith("!하민재"):
        await message.channel.send("'아 귀찮게 왜 그러는거임?' (안귀찮아 ㅄ) 브2 -하민재")
    if message.content.startswith("!유민우"):
        await message.channel.send("'내가 쟤보단 낫지' 브1 -유민우")
    if message.content.startswith("!하지민"):
        await message.channel.send("'ㅅㅂ 내가 왜 얘네들 데리고 랭겜을 해야하지'골1 -하지민")
    if message.content.startswith("!구민준"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!김도헌"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!유정민"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!이지영"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!김우진"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!배지민"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!원우민"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!송나연"):
        await message.channel.send("```지정된 소개글이 없습니다. FunCoolPP#3073으로 DM하여 수정.```")
    if message.content.startswith("!김현아"):
        await message.channel.send("https://www.twitch.tv/hyunah03")
    if message.content.startswith("!탬탬버린"):
        await message.channel.send("https://www.twitch.tv/2chamcham2")
    if message.content == "!민재랑 연애":
        my_name = discord.utils.get(message.guild.members, name="나는 나다-")
        await message.channel.send("민재♡예진".format(my_name.mention))





acess_token = os.environ["BOT_TOKEN"]
client.run(acess_token)
