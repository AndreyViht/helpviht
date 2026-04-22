import telebot
from telebot import types
import os

# Токен из Railway или напрямую
TOKEN = os.getenv('BOT_TOKEN') or '8656931761:AAGX9YOFgdOiSn-PNFPeir89mJtuqjg5KUA'
bot = telebot.TeleBot(TOKEN)

# Функция для создания главного меню
def get_main_menu(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "бро"
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🚀 Полная инструкция", callback_data='full_guide'),
        types.InlineKeyboardButton("⚙️ Умная маршрутизация", callback_data='smart_route'),
        types.InlineKeyboardButton("🆘 Поддержка", url="https://t.me/anviht")
    )
    text = (
        f"Привет, {user_name}! 👋\n\n"
        "Это официальный помощник **Viht VPN**.\n"
        "Выбери нужный раздел, чтобы быстро всё настроить: ↓"
    )
    return text, markup

# Команда /start - удаляет старое и присылает новое
@bot.message_handler(commands=['start'])
def start(message):
    try:
        # Пытаемся удалить сообщение пользователя с командой /start для чистоты
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass
    
    text, markup = get_main_menu(message)
    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')

# Обработка любого текста (кроме команд)
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🆘 Написать в поддержку", url="https://t.me/anviht"))
    
    bot.reply_to(
        message, 
        "Я не могу понять, что вы хотите. Опишите вашу проблему в поддержку, вам обязательно помогут!", 
        reply_markup=markup
    )

# Обработка кнопок (изменение сообщения)
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    back_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("⬅️ Назад в меню", callback_data='main_menu'))

    if call.data == "full_guide":
        text = (
            "🚀 **Инструкция по подключению Viht VPN**\n\n"
            "1️⃣ **Запуск**\n"
            "Перейдите в бота @VihtVPNbot и нажмите кнопку СТАРТ (или введите /start).\n\n"
            "2️⃣ **Личный кабинет**\n"
            "В ответном сообщении от бота нажмите на кнопку «Личный кабинет».\n\n"
            "3️⃣ **Подключение**\n"
            "В открывшемся веб-приложении нажмите синюю кнопку «Подключить устройство».\n\n"
            "4️⃣ **Активация**\n"
            "Выберите пункт «Открыть в Happ». Если приложение установлено, подписка подтянется автоматически. "
            "Если нет — сначала скачайте Happ из App Store/Play Market.\n\n"
            "🆘 **Поддержка:** @anviht\n"
            "🌐 **Наш сайт:** [anviht.ru](https://anviht.ru)\n"
            "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n"
            "_help Viht VPN | by 2025_"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown', disable_web_page_preview=True)
        
    elif call.data == "smart_route":
        text = (
            "⚙️ **Умная маршрутизация**\n"
            "_(VPN только для нужных приложений)_\n\n"
            "Чтобы не выключать VPN для банков или Госуслуг, сделайте следующее:\n\n"
            "1. Откройте приложение **Happ**.\n"
            "2. Нажмите на иконку **Шестерёнки ⚙️** в верхнем левом углу.\n"
            "3. Выберите пункт **«Прокси для выбранных приложений»**.\n"
            "4. Переключите тумблер в режим **«ВКЛ»**.\n"
            "5. Выберите из списка только те приложения, которым нужен VPN (например, Instagram, YouTube и т.д.).\n\n"
            "✅ **Результат:** Выбранные сервисы будут работать через VPN, а остальные — через вашу обычную сеть.\n\n"
            "🆘 **Поддержка:** @anviht"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown')

    elif call.data == "main_menu":
        text, markup = get_main_menu(call)
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode='Markdown')

if __name__ == '__main__':
    print("Бот Viht VPN запущен в режиме умного меню!")
    bot.polling(none_stop=True)
