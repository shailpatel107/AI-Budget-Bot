from telegram import Update
from telegram.ext import ContextTypes

async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Credit command received.")
