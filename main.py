from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, NUMBERS_FILE, NAMES_FILE
import os
import logging # লগিং মডিউল ইম্পোর্ট করা হলো

# লগিং কনফিগারেশন সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ---

async def _send_file_content(update: Update, file_path: str, empty_message: str, file_type_name: str):
    """
    একটি সাধারণ হেল্পার ফাংশন যা একটি ফাইল থেকে ডেটা পড়ে এবং টেলিগ্রাম বার্তায় পাঠায়।
    """
    if not os.path.exists(file_path):
        logger.warning(f"File not found: {file_path}")
        await update.message.reply_text(f"📂 {file_type_name} ফাইলটি খুঁজে পাওয়া যাচ্ছে না!")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        await update.message.reply_text(f"⚠️ {file_type_name} ফাইলটি পড়তে সমস্যা হচ্ছে!")
        return

    if not lines:
        logger.info(f"File {file_path} is empty.")
        await update.message.reply_text(empty_message)
        return

    count = 0
    message = ""
    for line in lines:
        line = line.strip()
        if line:
            message += f"`{line}`\n"
            count += 1
        if count == 10: # প্রথম 10টি লাইন পাঠানোর পর বন্ধ হবে
            break

    if message:
        await update.message.reply_text(message, parse_mode="Markdown")
    else:
        # যদি ফাইল থেকে কোনো বৈধ (খালি নয়) লাইন না পাওয়া যায়
        await update.message.reply_text(empty_message)


# 📲 Send Numbers কমান্ড
async def send_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /numbers command")
    await _send_file_content(update, NUMBERS_FILE, "⚠️ কোনো নাম্বার নেই ফাইলে!", "numbers.txt")


# 🧑‍💻 Send Names কমান্ড
async def send_names(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /names command")
    await _send_file_content(update, NAMES_FILE, "⚠️ কোনো নাম নেই ফাইলে!", "names.txt")


# ✅ Start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("Received /start command")
    await update.message.reply_text("✅ Bot is active.\nSend /numbers or /names to get data.")


# 🚀 বট চালু করুন
if __name__ == "__main__":
    logger.info("Starting Telegram Bot...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("numbers", send_numbers))
    app.add_handler(CommandHandler("names", send_names))

    app.run_polling()
    logger.info("Telegram Bot stopped.")

