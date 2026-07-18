import random
from datetime import datetime

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

users = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        users[user_id] = 0

    keyboard = [
        ["🎲 Случайное число", "🪙 Монетка"],
        ["⏰ Время", "📊 Мой профиль"],
    ]

    await update.message.reply_text(
        "👋 Добро пожаловать!\n\nВыбери действие:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        ),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    users[user_id] = users.get(user_id, 0) + 1

    text = update.message.text

    if text == "🎲 Случайное число":
        await update.message.reply_text(
            f"🎲 Выпало число: {random.randint(1,100)}"
        )

    elif text == "🪙 Монетка":
        await update.message.reply_text(
            random.choice(["🦅 Орёл", "🪙 Решка"])
        )

    elif text == "⏰ Время":
        await update.message.reply_text(
            datetime.now().strftime("⏰ %H:%M:%S")
        )

    elif text == "📊 Мой профиль":
        await update.message.reply_text(
            f"""👤 {update.effective_user.first_name}

🆔 {user_id}

📈 Использований: {users[user_id]}"""
        )


app = ApplicationBuilder().token("8826087429:AAHRGd-gKEXOtlQIiQgJYOO1i7j537htZXs").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Бот запущен!")

app.run_polling()