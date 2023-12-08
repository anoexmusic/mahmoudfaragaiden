import asyncio


import asyncio
import aiohttp
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums
import config

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton





import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")



@app.on_message(filters.command(["المطور", "ايدن","مطور البوت"], ""))
async def dev(client: Client, message: Message):
     bot_username = client.me.username
     user = await client.get_chat(OWNER_ID)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"╭⦿ɴᴀᴍᴇ : {message.from_user.mention} \n│᚜⦿  ᴄʜᴀᴛ ɴᴀᴍᴇ : {title}" if message.from_user else f"╰⦿ ᚐᴄʜᴀᴛ : ɴᴀᴍᴇ: {message.chat.title}"
     try:
      await client.send_message(username, f"<b></b>\nحـبي في حـد بينـادي عليك\n{chat_title}\n╰⦿ ᚐᴄʜᴀᴛ ɪᴅ : {message.chat.id}",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     await message.reply_photo(
     photo=photo,
     caption=f"<b></b>\n\n⌔ {name}\n⌔ @{username}\n⌔ {bio}",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass


@app.on_message(filters.left_chat_member)
async def left_bot(c,msg):
    link_gr = "@{msg.chat.username}" if msg.chat.username else "private group"
    if msg.left_chat_member.id == app.id:
        await app.send_message(config.OWNER_ID[0],f"تـم طـرد البـوت مـن جـروب {msg.chat.title} \n الجروب {link_gr}")

async def stcall(client: Client, message: Message): 
      Startt = "تـم بـدأ مـحادثـه صـوتيـه ي قـلبي"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "تـم إغـلاق المـحادثـه الصـوتيـه ي قـلبي"
      await message.reply_text(Enddd)

@app.on_message(filters.video_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"- قـام {message.from_user.mention}\n - بـدعـوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass