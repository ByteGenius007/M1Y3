import config
import telebot
import random

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, хз че писать. Но вы лайкайте!")

# Handle '/start' and '/help'
@bot.message_handler(commands=['random'])
def send_random_number(message):
    random_number = random.randint(1, 100)
    bot.reply_to(message, f"Твое случайное число: {random_number}")

@bot.message_handler(commands=['kick'])
def kick(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно выгнать администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, "Пользователь был выгнан из чата.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите выгнать.")

# Handle '/start' and '/help'
@bot.message_handler(commands=['fact'])
def send_random_fact(message):
    facts = ["Самая крупная жемчужина в мире достигает 6 килограммов в весе.", "Законодательство США допускало отправку детей по почте до 1913 года.", "В языке древних греков не существовало слова, которое обозначало религию.", "В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.", "Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.", "В Ирландии никогда не было кротов.", "Флот США содержит больше авианосцев, чем все флоты мира вместе взятые.", "Скорость распространения лавы после извержения, близка к скорости бега гончей.", "Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.", "Библия – книга, которую чаще всего воруют в американских магазинах."]
    random_fact = random.choice(facts)
    bot.reply_to(message, f"Твой случайный факт: {random_fact}")

@bot.message_handler(commands=['ban1'])
def ban(message):
    if message.reply_to_message:
        chat_id = message.chat.id 
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, "Пользователь был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

@bot.message_handler(commands=['info'])
def info(message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username or "No username"
        bot.reply_to(message, f"Его ID: {user_id}, Его username: {username}")
    else:
        user_id = message.from_user.id
        username = message.from_user.username or "No username"
        bot.reply_to(message, f"Ваш ID: {user_id}, Ваш username: {username}")


@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'Хз чо писать!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if "https://" in message.text:
        # Сохраняем информацию о пользователе
        user_id = message.from_user.id
        chat_id = message.chat.id

        # Проверяем статус пользователя перед баном
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
            bot.reply_to(message, "Вы были забанены за отправку запрещённых ссылок.")
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()