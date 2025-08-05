from telegram import Update
from telegram.ext import ContextTypes
from supabase_client import supabase

# Keep track of users who requested reset but haven't confirmed yet
pending_resets = set()

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    try:
        args = context.args
        if not args or args[0].lower() != "confirm":
            pending_resets.add(user_id)
            await update.message.reply_text(
                "⚠️ You are about to reset all your data. "
                "If you are sure, please confirm by typing /reset confirm"
            )
            return

        if user_id not in pending_resets:
            await update.message.reply_text(
                "Please request a reset first by typing /reset"
            )
            return

        # Perform the reset: delete all user transactions and reset accounts/budgets if applicable
        # Example: deleting all user transactions
        resp = supabase.table("transactions").delete().eq("user_id", user_id).execute()
        if resp.error:
            await update.message.reply_text(f"Error resetting data: {resp.error.message}")
            return

        # Clear pending reset flag
        pending_resets.remove(user_id)

        await update.message.reply_text("✅ All your data has been reset successfully.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")
