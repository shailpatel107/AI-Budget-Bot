from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import get_monthly_spent

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        response = get_monthly_spent(user_id)
        if response.error:
            await update.message.reply_text(f"Error fetching summary: {response.error.message}")
            return
        
        data = response.data
        if not data:
            await update.message.reply_text("No transactions found this month.")
            return

        message = "📊 Your Spending Summary (this month):\n\n"
        for item in data:
            message += f"{item['category']}: ${float(item['total_spent']):.2f}\n"

        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
