# -*- coding: utf-8 -*-

from imap_tools import MailBox, Q
from constants import *

import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is login as ({0.user.name}, {0.user.id})'.format(client))
    
@client.event
async def look_for_email_news():
   await client.wait_until_ready()
   while(True):
      mailbox = MailBox(mail_server)
      mailbox.login(mail_address, mail_password, initial_folder = mail_folder)
      for msg in mailbox.fetch(Q(seen=False)):
         if "[🐍PyTricks]" in msg.subject:
            print("A new message was found !")
            txt = msg.text[:msg.text.find("This email is part of the Python")]           
            await client.get_channel(channel_id).send(txt)
      print("time = " + str(datetime.datetime.now()), end = "\r")
      mailbox.logout()
      await asyncio.sleep(time_sleep)

client.loop.create_task(look_for_email_news())                
client.run(token)