from bot import bot  # Импортируем объект бота
import random
import messages
import time

num = 0
zak = 0
num_shop = 1010000


@bot.message_handler(commands=['start'])  # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, messages.START, parse_mode='HTML')

    if message.from_user.username == None:
        bot.send_message(771112471, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(771112471, message.text + '    *****    @' +
                         message.from_user.username + '   *****   ' + str(message.chat.id))


@bot.message_handler(content_types=["text"])  # Любой текст
def repeat_all_messages(message):

    global num, zak, num_shop

    num = num_shop + random.randint(0, 9999)
    zak = 10000 + random.randint(0, 9999)
    mes = str(num) + messages.PAY1 + str(zak) + messages.PAY2

    if message.chat.id == 845474542 or message.chat.id == 815607100:
        bot.send_message(message.chat.id, 'Вы заблокированы за частое применение команд', parse_mode='HTML')
    elif message.text == '/help':
        bot.send_message(message.chat.id, messages.HELP, parse_mode='HTML')
    elif message.text == '/lastorder':
        bot.send_message(message.chat.id, messages.LASTORDER, parse_mode='HTML')

# СОЧИ

    elif message.text == '/city1':
        bot.send_message(message.chat.id, messages.CITY1, parse_mode='HTML')

    elif message.text == '/buy16':
        bot.send_message(message.chat.id, messages.BUY16, parse_mode='HTML')
    elif message.text == '/buy44':
        bot.send_message(message.chat.id, messages.BUY44, parse_mode='HTML')
    elif message.text == '/buy48':
        bot.send_message(message.chat.id, messages.BUY48, parse_mode='HTML')
    elif message.text == '/buy51':
        bot.send_message(message.chat.id, messages.BUY51, parse_mode='HTML')

    elif message.text == '/buy16_1':
        bot.send_message(message.chat.id, messages.BUY16_1 + mes, parse_mode='HTML')
    elif message.text == '/buy16_2':
        bot.send_message(message.chat.id, messages.BUY16_2 + mes, parse_mode='HTML')
    elif message.text == '/buy44_6':
        bot.send_message(message.chat.id, messages.BUY44_6 + mes, parse_mode='HTML')
    elif message.text == '/buy48_6':
        bot.send_message(message.chat.id, messages.BUY48_6 + mes, parse_mode='HTML')
    elif message.text == '/buy51_1':
        bot.send_message(message.chat.id, messages.BUY51_1 + mes, parse_mode='HTML')

# Адлер

    elif message.text == '/city2':
        bot.send_message(message.chat.id, messages.CITY2, parse_mode='HTML')

    elif message.text == '/buy90':
        bot.send_message(message.chat.id, messages.BUY90, parse_mode='HTML')
    elif message.text == '/buy92':
        bot.send_message(message.chat.id, messages.BUY92, parse_mode='HTML')
    elif message.text == '/buy102':
        bot.send_message(message.chat.id, messages.BUY102, parse_mode='HTML')

    elif message.text == '/buy90_1':
        bot.send_message(message.chat.id, messages.BUY90_1 + mes, parse_mode='HTML')
    elif message.text == '/buy90_2':
        bot.send_message(message.chat.id, messages.BUY90_2 + mes, parse_mode='HTML')
    elif message.text == '/buy92_1':
        bot.send_message(message.chat.id, messages.BUY92_1 + mes, parse_mode='HTML')
    elif message.text == '/buy102_1':
        bot.send_message(message.chat.id, messages.BUY102_1 + mes, parse_mode='HTML')

# Абхазия

    elif message.text == '/city3':
        bot.send_message(message.chat.id, messages.CITY3, parse_mode='HTML')

    elif message.text == '/buy137':
        bot.send_message(message.chat.id, messages.BUY137, parse_mode='HTML')
    elif message.text == '/buy138':
        bot.send_message(message.chat.id, messages.BUY138, parse_mode='HTML')
    elif message.text == '/buy144':
        bot.send_message(message.chat.id, messages.BUY144, parse_mode='HTML')

    elif message.text == '/buy137_1':
        bot.send_message(message.chat.id, messages.BUY137_1 + mes, parse_mode='HTML')
    elif message.text == '/buy138_1':
        bot.send_message(message.chat.id, messages.BUY138_1 + mes, parse_mode='HTML')
    elif message.text == '/buy144_1':
        bot.send_message(message.chat.id, messages.BUY144_1 + mes, parse_mode='HTML')
    elif message.text == '/buy144_2':
        bot.send_message(message.chat.id, messages.BUY144_2 + mes, parse_mode='HTML')

    elif message.text == '/check':
        time.sleep(1)
        bot.send_message(message.chat.id, messages.CHECK, parse_mode='HTML')

    if message.from_user.username == None:
        bot.send_message(771112471, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(771112471, message.text + '    *****    @' +
                         message.from_user.username + '   *****   ' + str(message.chat.id))


if __name__ == '__main__':
    bot.polling(none_stop=True)
