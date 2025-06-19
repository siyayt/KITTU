from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    ABUTTON = [
    [
        InlineKeyboardButton("˹ sυᴘᴘσʀᴛ ˼", url="https://t.me/+PaEtaAu9DI9mYzc9"),
        InlineKeyboardButton("˹ υᴘᴅᴧᴛєs ˼", url="https://t.me/ARISHFA_UPDATE")
    ],
    [
        InlineKeyboardButton("˹ ʟᴧηɢᴜᴧɢє ˼", callback_data="LG"),
        InlineKeyboardButton("˹ ʙᴧᴄᴋ ˼", callback_data=f"settingsback_helper")
    ]
    ]
