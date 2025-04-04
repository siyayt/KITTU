from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_edited_message(filters.group)
async def delete_edited_messages(client, message):
    try:
        if hasattr(message, "edit_date") and message.edit_date and not message.from_user.is_bot:
            await message.delete()

            user_mention = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.mention}</a>"

            keyboard = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("𝖠𝖽𝖽 𝗆𝖾 𝖡𝖺𝖡𝗒", url=f"https://t.me/{client.me.username}?startgroup=true"),
                    InlineKeyboardButton("𝖡𝗈𝗍 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/purvi_support")
                ]
            ])

            await client.send_message(
                chat_id=message.chat.id,
                text=f"**⚠ {user_mention} edited their message, so it has been deleted.**",
                reply_markup=keyboard,
                disable_web_page_preview=True
            )

    except Exception as e:
        print(f"Error: {e}")
