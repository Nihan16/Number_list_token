import os

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters

from utils import get_next_numbers, get_next_names

user_progress_numbers = {}
user_progress_names = {}

keyboard = [
    ["📞 Get Number", "🧑‍💻 Get Name"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: CallbackContext):
    """Handles the /start command, sends a welcome message and the main keyboard."""
    await update.message.reply_text(
        "👋 স্বাগতম! আপনি কি করতে চান?",
        reply_markup=markup
    )

async def handle_message(update: Update, context: CallbackContext):
    """Handles all text messages from the user."""
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    if text == "📞 Get Number":
        if user_id not in user_progress_numbers:
            user_progress_numbers[user_id] = 0
        
        start_index = user_progress_numbers[user_id]
        numbers = get_next_numbers(start_index, 10) # 10টি নাম্বার আনা হবে

        if not numbers:
            await update.message.reply_text("❌ আর কোনো নাম্বার নেই! অ্যাডমিনকে `numbers.txt` আপডেট করতে বলুন।")
            return
        
        # প্রতিটি নাম্বার আলাদা আলাদা মেসেজে পাঠানো হবে
        for num in numbers:
            await update.message.reply_text(f"`{num}`", parse_mode="Markdown") # Markdown ব্যবহার করে কপি করা সহজ হবে
        
        user_progress_numbers[user_id] += 10 # 10টি নাম্বার এগিয়ে যাওয়া হবে

    elif text == "🧑‍💻 Get Name":
        if user_id not in user_progress_names:
            user_progress_names[user_id] = 0
        
        start_index = user_progress_names[user_id]
        names = get_next_names(start_index, 5) # 5টি নাম আনা হবে

        if not names:
            await update.message.reply_text("❌ আর কোনো নাম নেই! অ্যাডমিনকে `names.txt` আপডেট করতে বলুন।")
            return
        
        # প্রতিটি নাম আলাদা আলাদা মেসেজে পাঠানো হবে
        for name in names:
            await update.message.reply_text(f"`{name}`", parse_mode="Markdown") # Markdown ব্যবহার করে কপি করা সহজ হবে
        
        user_progress_names[user_id] += 5 # 5টি নাম এগিয়ে যাওয়া হবে

def main():
    """Sets up the Telegram bot application and runs it."""
    token = os.getenv("BOT_TOKEN") 
    if not token:
        print("Error: BOT_TOKEN environment variable not set. Please set it in Railway or your local environment.")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("✅ Bot running...")
    application.run_polling()

if __name__ == "__main__":
    main()
