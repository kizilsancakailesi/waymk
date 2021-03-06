"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from helpers.bot_utils import BOT_NAME, USERNAME
from config import SUPPORT_GROUP, UPDATES_CHANNEL
from translations import START_TEXT, HELP_TEXT, ABOUT_TEXT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("β HOW TO USE ME β", callback_data="help"),
            ],
            [
                InlineKeyboardButton("π’ CHANNEL", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("REΔ°S π", url=f"https://t.mw/kizilsancaksahibi"),
            ],
            [
                InlineKeyboardButton("π€ ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE π", callback_data="close"),
            ],
            [
               InlineKeyboardButton("β ADD ME TO YOUR GROUP β", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply_text(f"**{BOT_NAME} is Alive !** β¨")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("π BACK", callback_data="start"),
                InlineKeyboardButton ("SUPPORT π¬", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("π BACK", callback_data="start"),
                InlineKeyboardButton ("SUPPORT π¬", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("β HOW TO USE ME β", callback_data="help"),
            ],
            [
                InlineKeyboardButton("π’ CHANNEL", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("Reis π", url=f"https://t.me/kizilsancaksahibi"),
            ],
            [
                InlineKeyboardButton("π€ ABOUT", callback_data="about"),
                InlineKeyboardButton("CLOSE π", callback_data="close"),
            ],
            [
               InlineKeyboardButton("β ADD ME TO YOUR GROUP β", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

