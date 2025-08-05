from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def raizwithdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if len(args) < 2:
            await update.message.reply_text("Usage: /raizwithdraw [user] [amount]")
            return
        
        user = args[0]
        amount = float(args[1])
        
        response = supabase.rpc('withdraw_raiz', {'user': user, 'amount': amount}).execute()
        
        if response.error:
            await update.message.reply_text(f"Error withdrawing amount: {response.error.message}")
            return
        
        await update.message.reply_text(f"💵 Withdrawn ${amount:.2f} for {user}.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
