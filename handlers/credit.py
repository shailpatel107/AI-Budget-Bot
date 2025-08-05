from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        
        # Call the stored procedure or RPC that calculates credit usage for the user
        response = supabase.rpc('get_credit_usage', {'user_id': user_id}).execute()
        
        if response.error:
            await update.message.reply_text(f"Error fetching credit usage: {response.error.message}")
            return
        
        data = response.data
        if not data or len(data) == 0:
            await update.message.reply_text("No credit card usage found for this month.")
            return
        
        # Assuming RPC returns a list of transactions or a total
        # If it returns total, just show that, else aggregate here
        total_used = 0.0
        if isinstance(data, list):
            for tx in data:
                total_used += float(tx.get('amount', 0))
        else:
            total_used = float(data)
        
        await update.message.reply_text(f"💳 Total credit card usage this month: ${total_used:.2f}")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")