# bot_module.py

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode
from PURVIMUSIC import app

async def delete_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """जब कोई यूज़र मैसेज एडिट करेगा, तो उसे डिलीट कर देगा और notify करेगा।"""
    if update.edited_message:
        chat_id = update.edited_message.chat_id
        message_id = update.edited_message.message_id
        user = update.edited_message.from_user

        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
            print(f"Deleted edited message in chat: {chat_id}")
            
            mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"{mention} edited a message, I detected it and deleted it.",
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            print(f"Error deleting edited message: {e}")

def setup_bot(token: str) -> Application:
    """बॉट को सेटअप करता है, लेकिन रन नहीं करता।"""
    app = Application.builder().token(token).build()

    # एडिट किए गए मैसेज को मॉनिटर करने के लिए हैंडलर जोड़ें
    app.add_handler(MessageHandler(filters.ALL & filters.UpdateType.EDITED_MESSAGE, delete_edited_message))

    return app
