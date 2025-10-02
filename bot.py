import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Включаем логирование, чтобы видеть ошибки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {user_name}! Я эхо-бот. Просто отправь мне любое сообщение, и я его повторю."
    )

# Функция, которая будет "отзеркаливать" сообщения
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=user_message
    )

def main():
    # Создаем объект Application и передаем ему токен вашего бота
    # ЗАМЕНИТЕ 'ВАШ_ТОКЕН_ЗДЕСЬ' НА ВАШ РЕАЛЬНЫЙ ТОКЕН
    application = Application.builder().token('8117802290:AAHtoZk4FbLMroOwKqXVMaQX-sKa703DMgg').build()

    # Создаем обработчик для команды /start
    start_handler = CommandHandler('start', start)

    # Создаем обработчик для всех текстовых сообщений
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    # Регистрируем обработчики в приложении
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    # Запускаем бота (он будет работать, пока вы не остановите программу)
    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
