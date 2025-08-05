from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def spent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if not args:
            await update.message.reply_text("Usage: /spent [category]")
            return

        category_name = args[0]
        user_id = update.effective_user.id

        # Call RPC to get spent amount in category for current month
        response = supabase.rpc('spent_in_category', {'user_id': user_id, 'category_name': category_name}).execute()

        if response.error:
            await update.message.reply_text(f"Error fetching spending: {response.error.message}")
            return

        total_spent = 0.0
        if response.data and len(response.data) > 0:
            total_spent = float(response.data[0].get('total', 0))

        await update.message.reply_text(f"💸 You have spent ${total_spent:.2f} in '{category_name}' this month.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
