from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, NUMBERS_FILE, NAMES_FILE
import os

# 📤 Send Numbers
async def send_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not os.path.exists(NUMBERS_FILE):
        await update.message.reply_text("📁 numbers.txt ফাইল পাওয়া যায়নি!")
        return

    with open(NUMBERS_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        await update.message.reply_text("⚠️ কোনো নাম্বার নেই ফাইলে!")
        return

    count = 0
    message = ""
    for line in lines:
        line = line.strip()
        if line:
            message += f"`{line}`\n"
            count += 1
        if count == 10:
            break

    await update.message.reply_text(message, parse_mode="Markdown")

# 📤 Send Names
async def send_names(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not os.path.exists(NAMES_FILE):
        await update.message.reply_text("📁 names.txt ফাইল পাওয়া যায়নি!")
        return

    with open(NAMES_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        await update.message.reply_text("⚠️ কোনো নাম নেই ফাইলে!")
        return

    count = 0
    message = ""
    for line in lines:
        line = line.strip()
        if line:
            message += f"`{line}`\n"
            count += 1
        if count == 10:
            break

    await update.message.reply_text(message, parse_mode="Markdown")

# 🔰 Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is active.\nSend /numbers or /names to get data.")

# 🚀 Run the Bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("numbers", send_numbers))
    app.add_handler(CommandHandler("names", send_names))
    app.run_polling()
