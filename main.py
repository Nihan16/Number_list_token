from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext, filters
from config import BOT_TOKEN
from utils import get_next_numbers

user_progress = {}

keyboard = [[
    "📞 Get Number"
]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("👋 স্বাগতম!
আপনি কী করতে চান?", reply_markup=markup)

async def handle_message(update: Update, context: CallbackContext.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if update.message.text == "📞 Get Number":
        if user_id not in user_progress:
            user_progress[user_id] = 0
        start_index = user_progress[user_id]
        numbers = get_next_numbers(start_index, 10)
        if not numbers:
            await update.message.reply_text("❌ দুঃখিত, আর কোনো নাম্বার নেই! অ্যাডমিন numbers.txt আপডেট করুন।")
            return
        user_progress[user_id] += 10
        response = "\n".join(numbers)
        await update.message.reply_text(response)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

if __name__ == "__main__":
    print("Bot running...")
    app.run_polling()
