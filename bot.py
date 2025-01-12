import config
import telebot
import random

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, хз че писать. Хз че писать, но вы лайкайте!")

# Handle '/start' and '/help'
@bot.message_handler(commands=['random'])
def send_random_number(message):
    random_number = random.randint(1, 100)
    bot.reply_to(message, f"Твое случайное число: {random_number}")


# Handle '/start' and '/help'
@bot.message_handler(commands=['fact'])
def send_random_fact(message):
    facts = ["Самая крупная жемчужина в мире достигает 6 килограммов в весе.", "Законодательство США допускало отправку детей по почте до 1913 года.", "В языке древних греков не существовало слова, которое обозначало религию.", "В современной истории есть промежуток времени, когда на счетах компании «Apple», было больше средств, чем у американского правительства.", "Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.", "В Ирландии никогда не было кротов.", "Флот США содержит больше авианосцев, чем все флоты мира вместе взятые.", "Скорость распространения лавы после извержения, близка к скорости бега гончей.", "Изначально, отвертка была изобретена для выковыривания гвоздей, шуруп был изобретен на 100 лет позже.", "Библия – книга, которую чаще всего воруют в американских магазинах."]
    random_fact = random.choice(facts)
    bot.reply_to(message, f"Твой случайный факт: {random_fact}")

@bot.message_handler(commands=['ban'])
def ban(message):
    if message.reply_to_message:
        chat_id = message.chat.id 
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id)
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()