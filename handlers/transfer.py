
from telegram import Update
from telegram.ext import ContextTypes

async def transfer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Transfer command received.")

def transfer(update, context):
    update.message.reply_text("Transfer command triggered")

