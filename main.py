<<<<<<< HEAD
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from handlers.add import add
from handlers.attach import attach
from handlers.edit import edit
from handlers.starting import starting
from handlers.transfer import transfer
from handlers.roundup import roundup
from handlers.summary import summary
from handlers.spent import spent
from handlers.credit import credit
from handlers.raizshare import raizshare
from handlers.raizdividends import raizdividends
from handlers.raizinvested import raizinvested
from handlers.raizwithdraw import raizwithdraw
from handlers.alerts import alerts
from handlers.ruleoverride import ruleoverride
from handlers.reset import reset
from handlers.help_command import help_command as help
from handlers.start import start
from handlers.text_parser import handle_text_command

import os
from dotenv import load_dotenv

load_dotenv()
=======
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.add import add
from handlers.attach import attach
from handlers.edit import edit
from handlers.transfer import transfer
from handlers.roundup import roundup
from handlers.alerts import alerts
from handlers.raiz import raizshare, raizdividends, raizinvested, raizwithdraw
from handlers.reset import ruleoverride, reset
from handlers.help_command import help_command
from handlers.text_parser import handle_text_command
from dotenv import load_dotenv
import os

load_dotenv()

>>>>>>> 0cad325 (V2 commit)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

<<<<<<< HEAD
# Slash commands
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("attach", attach))
app.add_handler(CommandHandler("edit", edit))
app.add_handler(CommandHandler("starting", starting))
app.add_handler(CommandHandler("transfer", transfer))
app.add_handler(CommandHandler("roundup", roundup))
app.add_handler(CommandHandler("summary", summary))
app.add_handler(CommandHandler("spent", spent))
app.add_handler(CommandHandler("credit", credit))
=======
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("attach", attach))
app.add_handler(CommandHandler("edit", edit))
app.add_handler(CommandHandler("transfer", transfer))
app.add_handler(CommandHandler("roundup", roundup))
app.add_handler(CommandHandler("alerts", alerts))
>>>>>>> 0cad325 (V2 commit)
app.add_handler(CommandHandler("raizshare", raizshare))
app.add_handler(CommandHandler("raizdividends", raizdividends))
app.add_handler(CommandHandler("raizinvested", raizinvested))
app.add_handler(CommandHandler("raizwithdraw", raizwithdraw))
<<<<<<< HEAD
app.add_handler(CommandHandler("alerts", alerts))
app.add_handler(CommandHandler("ruleoverride", ruleoverride))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", start))

# Text-based command triggers (no slash)
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_command))

if __name__ == '__main__':
    print("🚀 BudgetBuddy is running...")
    app.run_polling()
=======
app.add_handler(CommandHandler("ruleoverride", ruleoverride))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_command))

print("Bot is running...")
app.run_polling()
>>>>>>> 0cad325 (V2 commit)
