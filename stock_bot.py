import requests
import os
import logging
from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

TELEGRAM_TOKEN = os.getenv('TOKEN')  # Добавьте токен в код (не делайте так в реальных проектах!)
API_KEY = os.getenv('APIKEY')

URL = f"https://api.finage.co.uk/last/trade/stock/TSLA?apikey={API_KEY}"


# def get_new_image():
#     try:
#         response = requests.get(URL)
#     except Exception as error:
#         logging.error(f'Ошибка при запросе к основному API: {error}')
#         new_url = 'https://api.thedogapi.com/v1/images/search'
#         response = requests.get(new_url)
#
#     response = response.json()
#     random_cat = response[0].get('url')
#     return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


# def wake_up(update, context):
#     chat = update.effective_chat
#     name = update.message.chat.first_name
#     buttons = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
#
#     context.bot.send_message(
#         chat_id=chat.id,
#         text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
#         reply_markup=buttons
#     )
#
#     context.bot.send_photo(chat.id, get_new_image())


def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    print(me)
    # Регистрируется обработчик MessageHandler;
    # из всех полученных сообщений он будет выбирать только текстовые сообщения
    # и передавать их в функцию say_hi()
    # updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    # Метод start_polling() запускает процесс polling,
    # приложение начнёт отправлять регулярные запросы для получения обновлений.
    updater.start_polling()
    # Бот будет работать до тех пор, пока не нажмете Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()