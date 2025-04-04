from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PURVIMUSIC import app

from pyrogram import Client, filters
import asyncio

@app.on_edited_message(filters.group)
async def delete_edited_message(client, message):
    try:
        await asyncio.sleep(2)
        await message.delete()

        await message.reply(
            f"Hey {message.from_user.mention}, you edited a message, so it has been deleted."
        )

    except Exception as e:
        print(f"Error: {e}")
