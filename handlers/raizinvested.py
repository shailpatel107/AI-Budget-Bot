from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def raizinvested(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /raizinvested [user] [amount]")
            return
        
        user = args[0]
        amount = float(args[1])
        
        response = supabase.rpc('add_raiz_investment', {'user': user, 'amount': amount}).execute()
        
        if response.error:
            await update.message.reply_text(f"Error adding investment: {response.error.message}")
            return
        
        await update.message.reply_text(f"💸 Added investment of ${amount:.2f} for {user}.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
