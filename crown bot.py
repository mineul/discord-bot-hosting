import asyncio,discord,os
import random
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import time
from discord.ext import commands
from datetime import datetime
import re
from gtts import gTTS
import playsound
import pyautogui
from googletrans import Translator

client = discord.Client()
token = "ODIwNTgyMDk0NDcyMjE2NTc2.YE3QoQ.eEbmb2Jm4Dq2i-seOuWQ9tUlFto"
game = discord.Game("!도움")

@client.event
async def on_ready():
    print("로그인 됨")

@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith("킹크라운"):
        await message.channel.send("안녕!")

    if message.content.startswith("뽑기 "):
        await message.channel.send(random.choice(str(message.content)[2:].split(",")))

    if message.content.startswith("GG <@"):
        await message.channel.send("미육이 바부!")
    if random.randint(1, 400) == 1:
        await message.channel.send("https://mnsoftware.netlify.app/")

    if random.randint(1, 400) == 1:
        await message.channel.send("https://discord.gg/5vSd6b7szN")


client.run(token)