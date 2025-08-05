<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes

async def attach(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Attach command received.")
=======
def attach(update, context):
    update.message.reply_text("Attach command triggered")
>>>>>>> 0cad325 (V2 commit)
