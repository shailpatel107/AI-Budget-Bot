from telegram import Update
from telegram.ext import ContextTypes

# In-memory set to track pending resets per user for confirmation
pending_resets = set()

async def ruleoverride(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        if not args or args[0].lower() not in ['on', 'off']:
            await update.message.reply_text("Usage: /ruleoverride on|off")
            return

        override_enabled = args[0].lower() == 'on'
        user_id = update.effective_user.id

        # Here you would save the override state in DB or cache — placeholder below
        # Example: save to supabase user_settings table (pseudo-code)
        # supabase.table('user_settings').upsert({'user_id': user_id, 'rule_override': override_enabled}).execute()

        state = "enabled" if override_enabled else "disabled"
        await update.message.reply_text(f"Budget rule override has been {state}. Use responsibly!")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")


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
            await update.message.reply_text("Please request a reset first by typing /reset")
            return

        # Perform the reset logic — e.g. delete transactions belonging to the user
        # Replace with actual supabase calls
        # supabase.table("transactions").delete().eq("user_id", user_id).execute()

        # Clear confirmation
        pending_resets.remove(user_id)

        await update.message.reply_text("✅ All your data has been reset successfully.")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
