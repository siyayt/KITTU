import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

# PyDroid3 में Asyncio के Loop को Fix करें
nest_asyncio.apply()

# अपना बॉट टोकन डालें
BOT_TOKEN = "7741317454:AAHXf8bkM1JZtBBK5Nn02MXtncThtBPOJ-A"

async def delete_edited_message(update: Update, context: CallbackContext):
    """जब कोई यूज़र मैसेज एडिट करेगा, तो उसे डिलीट कर देगा।"""
    if update.edited_message:
        chat_id = update.edited_message.chat_id
        message_id = update.edited_message.message_id
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        print(f"Deleted edited message in chat: {chat_id}")

async def main():
    """बॉट को स्टार्ट करता है और हैंडलर जोड़ता है।"""
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # एडिट किए गए मैसेज को मॉनिटर करने के लिए हैंडलर जोड़ें
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, delete_edited_message))
