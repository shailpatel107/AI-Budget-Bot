<<<<<<< HEAD
from telegram import Update
from telegram.ext import ContextTypes

async def roundup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Roundup command received.")
=======
def roundup(update, context):
    update.message.reply_text("Roundup command triggered")
>>>>>>> 0cad325 (V2 commit)
