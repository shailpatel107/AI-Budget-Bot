from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def raizdividends(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 1:
            await update.message.reply_text("Usage: /raizdividends [amount]")
            return
        
        amount = float(args[0])
        response = supabase.rpc('add_raiz_dividends', {'amount': amount}).execute()
        
        if response.error:
            await update.message.reply_text(f"Error adding dividends: {response.error.message}")
            return
        
        await update.message.reply_text(f"💰 Added ${amount:.2f} dividends to Raiz.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
