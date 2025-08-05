from telegram import Update
from telegram.ext import ContextTypes

async def spent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Spent command received.")
