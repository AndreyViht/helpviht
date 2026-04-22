import telebot
from telebot import types

# Твой токен
TOKEN = '8656931761:AAGX9YOFgdOiSn-PNFPeir89mJtuqjg5KUA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Узнаем имя, чтобы бот не был "сухим"
    user_name = message.from_user.first_name if message.from_user.first_name else "друг"
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Кнопки с нужным приложением и стикерами
    btn_setup = types.InlineKeyboardButton("📲 Настройка Happ", callback_data='setup')
    btn_smart = types.InlineKeyboardButton("🧠 Умная маршрутизация", callback_data='smart')
    btn_support = types.InlineKeyboardButton("🆘 Помощь / Админ", callback_data='support')
    
    markup.add(btn_setup, btn_smart, btn_support)
    
    welcome_text = (
        f"Привет, {user_name}! 👋\n\n"
        "Это бот-помощник **Viht VPN**.\n"
        "Давай быстро настроим интернет через приложение **Happ**. 🚀\n\n"
        "Жми на кнопку ниже: ↓"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # Кнопка возврата
    back_markup = types.InlineKeyboardMarkup()
    back_markup.add(types.InlineKeyboardButton("⬅️ В главное меню", callback_data='main_menu'))

    if call.data == "setup":
        setup_text = (
            "**⚙️ Инструкция для Happ:**\n\n"
            "1️⃣ **Установи Happ**\n"
            "Скачай и установи приложение на свой телефон.\n\n"
            "2️⃣ **Скопируй ключ**\n"
            "Твой ключ VLESS должен быть в буфере обмена.\n\n"
            "3️⃣ **Добавь конфиг**\n"
            "В приложении Happ нажми кнопку добавления (обычно '+' или импорт).\n\n"
            "4️⃣ **Лети!**\n"
            "Выбирай сервер Viht VPN и подключайся. Всё должно работать! ✅"
        )
        bot.edit_message_text(setup_text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown')
        
    elif call.data == "smart":
        smart_text = (
            "**🧠 Умная маршрутизация в Happ:**\n\n"
            "Это когда VPN работает только там, где нужно.\n\n"
            "• Инста и Ютуб работают через прокси.\n"
            "• Твои банковские приложения не тупят и видят твой реальный IP.\n"
            "• Телефон не греется и зарядка живет дольше! 🔥"
        )
        bot.edit_message_text(smart_text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown')

    elif call.data == "support":
        support_text = (
            "**🆘 Есть вопросы?**\n\n"
            "Если Happ не подключается или есть вопросы по подписке — пиши админу прямо сейчас.\n\n"
            "Мы всё решим! 🤝"
        )
        bot.edit_message_text(support_text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown')

    elif call.data == "main_menu":
        user_name = call.from_user.first_name
        main_markup = types.InlineKeyboardMarkup(row_width=1)
        main_markup.add(
            types.InlineKeyboardButton("📲 Настройка Happ", callback_data='setup'),
            types.InlineKeyboardButton("🧠 Умная маршрутизация", callback_data='smart'),
            types.InlineKeyboardButton("🆘 Помощь / Админ", callback_data='support')
        )
        bot.edit_message_text(f"Что еще подсказать, {user_name}? 👇", call.message.chat.id, call.message.message_id, reply_markup=main_markup, parse_mode='Markdown')

if __name__ == '__main__':
    print("Viht VPN (Happ) Bot запущен!")
    bot.polling(none_stop=True)
