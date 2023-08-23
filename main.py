import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6503665664:AAEh1L5Nky8dJpO6ceUTpvMc-Yn_oe_VNws')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, Привет!"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Мое имя', callback_data='yes')
    markup.add(button_yes)
    button_why = types.InlineKeyboardButton(text='Кем я работаю', callback_data='why')
    markup.add(button_why)
    button_no = types.InlineKeyboardButton(text='Мой Телеграм', callback_data='no')
    markup.add(button_no)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "yes":
            second_mess = "Я Beishekeev Bek, мне 23"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Перейти на сайт",
                                                  url="https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B4%D0%BE%D0%B2%D0%BE%D0%BB%D1%8C%D0%BD%D0%BE-%D0%BE%D1%87%D0%B0%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B4%D0%B5%D0%B2%D1%83%D1%88%D0%BA%D0%B0-%D0%B2-%D0%BE%D1%87%D0%BA%D0%B0%D1%85-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D1%8E%D1%89%D0%B0%D1%8F-%D0%B4%D0%B2%D0%BE%D0%B9%D0%BD%D0%BE%D0%B9-%D0%B6%D0%B5%D1%81%D1%82-%D1%81%D1%80%D0%B5%D0%B4%D0%BD%D0%B5%D0%B3%D0%BE-%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D0%B0-gm1012417368-272721370"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'why':
            second_mess = " Программистом"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("!!", url="https://avtokafe.ru/tormoza/"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)
        elif function_call.data == 'no':
            second_mess = "!!!"
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Можешь нажать", url="https://t.me/beishekeev0011"))
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)


botTimeWeb.infinity_polling()
