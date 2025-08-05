from telegram import Update
from telegram.ext import ContextTypes

async def handle_text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")
