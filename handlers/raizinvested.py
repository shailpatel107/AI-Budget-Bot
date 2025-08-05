from telegram import Update
from telegram.ext import ContextTypes

async def raizinvested(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Raizinvested command received.")
