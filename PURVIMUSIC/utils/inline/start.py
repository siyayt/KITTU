from pyrogram.types import InlineKeyboardButton

import config
from PURVIMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),  
            InlineKeyboardButton(text="˹ ʏᴛ-ᴧᴘɪ ˼", callback_data="bot_info_data"),
        ],
        [
        #    InlineKeyboardButton(text="sσυʀᴄє ᴄσᴅє", url=f"https://github.com/TEAM-ISTKHAR/IstkharMusic.git"),
        InlineKeyboardButton(text=_["S_B_13"], callback_data="abot_cb"),  
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons
    
