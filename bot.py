import telebot
from telebot import types
import os

# Берем токен из переменных Railway или вставляем напрямую
TOKEN = os.getenv('BOT_TOKEN') or '8656931761:AAGX9YOFgdOiSn-PNFPeir89mJtuqjg5KUA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "бро"
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Кнопки для меню
    btn_guide = types.InlineKeyboardButton("🚀 Полная инструкция", callback_data='full_guide')
    btn_smart = types.InlineKeyboardButton("⚙️ Умная маршрутизация", callback_data='smart_route')
    btn_support = types.InlineKeyboardButton("🆘 Поддержка", url="https://t.me/anviht")
    
    markup.add(btn_guide, btn_smart, btn_support)
    
    welcome_text = (
        f"Привет, {user_name}! 👋\n\n"
        "Это официальный помощник **Viht VPN**.\n"
        "Выбери нужный раздел, чтобы быстро всё настроить: ↓"
    )
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    # Кнопка возврата
    back_markup = types.InlineKeyboardMarkup()
    back_markup.add(types.InlineKeyboardButton("⬅️ Назад в меню", callback_data='main_menu'))

    if call.data == "full_guide":
        # Вариант 1: Пошаговое руководство (полное)
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
        # Раздел про умную маршрутизацию
        text = (
            "⚙️ **Умная маршрутизация**\n"
            "_(VPN только для нужных приложений)_\n\n"
            "Чтобы не выключать VPN для банков или Госуслуг, сделайте следующее:\n\n"
            "1. Откройте приложение **Happ**.\n"
            "2. Нажмите на иконку **Шестерёнки ⚙️** в верхнем левом углу.\n"
            "3. Выберите пункт **«Прокси для выбранных приложений»**.\n"
            "4. Переключите тумблер в режим **«ВКЛ»**.\n"
            "5. Выберите из списка только те приложения, которым нужен VPN (например, Instagram, YouTube и т.д.).\n\n"
            "✅ **Результат:** Выбранные сервисы будут работать через VPN, а остальные — через вашу обычную сеть. "
            "Больше не нужно ничего переключать!\n\n"
            "🆘 **Поддержка:** @anviht"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=back_markup, parse_mode='Markdown')

    elif call.data == "main_menu":
        # Возврат в начало
        start(call.message)

if __name__ == '__main__':
    print("Бот Viht VPN запущен на Railway!")
    bot.polling(none_stop=True)
