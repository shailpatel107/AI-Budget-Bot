from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

async def raizshare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.effective_user.id
        response = supabase.rpc('get_raiz_share', {'user_id': user_id}).execute()
        
        if response.error:
            await update.message.reply_text(f"Error fetching Raiz share: {response.error.message}")
            return
        
        share = response.data.get('share', 0)
        await update.message.reply_text(f"📈 Your Raiz investment share: {share:.2f}%")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
