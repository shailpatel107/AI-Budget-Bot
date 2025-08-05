from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.add import add
from handlers.summary import summary

from handlers.attach import attach
from handlers.edit import edit
from handlers.transfer import transfer
from handlers.roundup import roundup
from handlers.alerts import alerts
from handlers.raiz import raizshare, raizdividends, raizinvested, raizwithdraw
from handlers.reset import ruleoverride, reset
from handlers.help_command import help_command
from handlers.text_parser import handle_text_command
from handlers.start import start
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
app = ApplicationBuilder().token(TOKEN).build()

# Slash commands
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("summary", summary))

app.add_handler(CommandHandler("attach", attach))
app.add_handler(CommandHandler("edit", edit))
app.add_handler(CommandHandler("transfer", transfer))
app.add_handler(CommandHandler("roundup", roundup))
app.add_handler(CommandHandler("alerts", alerts))
app.add_handler(CommandHandler("raizshare", raizshare))
app.add_handler(CommandHandler("raizdividends", raizdividends))
app.add_handler(CommandHandler("raizinvested", raizinvested))
app.add_handler(CommandHandler("raizwithdraw", raizwithdraw))
app.add_handler(CommandHandler("ruleoverride", ruleoverride))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

# Text-based commands (no slash)
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text_command))

print("🚀 BudgetBuddy is running...")
app.run_polling()
