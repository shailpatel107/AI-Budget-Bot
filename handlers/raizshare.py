from telegram import Update
from telegram.ext import ContextTypes

async def raizshare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Raizshare command received.")
