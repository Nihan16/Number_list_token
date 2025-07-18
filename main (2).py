from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters
from config import BOT_TOKEN
from utils import get_next_numbers, get_next_names

user_progress_numbers = {}
user_progress_names = {}

keyboard = [[
    "📞 Get Number", "🧑 Get Name"
]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("👋 স্বাগতম! আপনি কী করতে চান?", reply_markup=markup)

async def handle_message(update: Update, context: CallbackContext.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if text == "📞 Get Number":
        if user_id not in user_progress_numbers:
            user_progress_numbers[user_id] = 0
        start_index = user_progress_numbers[user_id]
        numbers = get_next_numbers(start_index, 10)
        if not numbers:
            await update.message.reply_text("❌ আর কোনো নাম্বার নেই!")
            return
        user_progress_numbers[user_id] += 10
        await update.message.reply_text("\n".join(numbers))

    elif text == "🧑 Get Name":
        if user_id not in user_progress_names:
            user_progress_names[user_id] = 0
        start_index = user_progress_names[user_id]
        names = get_next_names(start_index, 10)
        if not names:
            await update.message.reply_text("❌ আর কোনো নাম নেই!")
            return
        user_progress_names[user_id] += 10
        await update.message.reply_text("\n".join(names))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

if __name__ == "__main__":
    print("Bot running...")
    app.run_polling()

