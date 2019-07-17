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
        bot.send_message(808928920, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(808928920, message.text + '    *****    @' +
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

    elif message.text == '/buy15':
        bot.send_message(message.chat.id, messages.BUY15, parse_mode='HTML')
    elif message.text == '/buy16':
        bot.send_message(message.chat.id, messages.BUY16, parse_mode='HTML')
    elif message.text == '/buy43':
        bot.send_message(message.chat.id, messages.BUY43, parse_mode='HTML')
    elif message.text == '/buy44':
        bot.send_message(message.chat.id, messages.BUY44, parse_mode='HTML')
    elif message.text == '/buy46':
        bot.send_message(message.chat.id, messages.BUY46, parse_mode='HTML')
    elif message.text == '/buy48':
        bot.send_message(message.chat.id, messages.BUY48, parse_mode='HTML')
    elif message.text == '/buy50':
        bot.send_message(message.chat.id, messages.BUY50, parse_mode='HTML')
    elif message.text == '/buy51':
        bot.send_message(message.chat.id, messages.BUY51, parse_mode='HTML')
    elif message.text == '/buy53':
        bot.send_message(message.chat.id, messages.BUY53, parse_mode='HTML')

    elif message.text == '/buy15_1':
        bot.send_message(message.chat.id, messages.BUY15_1 + mes, parse_mode='HTML')
    elif message.text == '/buy15_2':
        bot.send_message(message.chat.id, messages.BUY15_2 + mes, parse_mode='HTML')
    elif message.text == '/buy16_1':
        bot.send_message(message.chat.id, messages.BUY16_1 + mes, parse_mode='HTML')
    elif message.text == '/buy16_2':
        bot.send_message(message.chat.id, messages.BUY16_2 + mes, parse_mode='HTML')
    elif message.text == '/buy43_1':
        bot.send_message(message.chat.id, messages.BUY43_1 + mes, parse_mode='HTML')
    # elif message.text == '/buy43_2':
    #    bot.send_message(message.chat.id, messages.BUY43_2 + mes, parse_mode='HTML')
    # elif message.text == '/buy43_3':
    #    bot.send_message(message.chat.id, messages.BUY43_3 + mes, parse_mode='HTML')
    # elif message.text == '/buy43_4':
    #    bot.send_message(message.chat.id, messages.BUY43_4 + mes, parse_mode='HTML')
    elif message.text == '/buy44_1':
        bot.send_message(message.chat.id, messages.BUY44_1 + mes, parse_mode='HTML')
    elif message.text == '/buy44_2':
        bot.send_message(message.chat.id, messages.BUY44_2 + mes, parse_mode='HTML')
    elif message.text == '/buy46_1':
        bot.send_message(message.chat.id, messages.BUY46_1 + mes, parse_mode='HTML')
    elif message.text == '/buy48_1':
        bot.send_message(message.chat.id, messages.BUY48_1 + mes, parse_mode='HTML')
    elif message.text == '/buy48_2':
        bot.send_message(message.chat.id, messages.BUY48_2 + mes, parse_mode='HTML')
    elif message.text == '/buy50_1':
        bot.send_message(message.chat.id, messages.BUY50_1 + mes, parse_mode='HTML')
    elif message.text == '/buy50_2':
        bot.send_message(message.chat.id, messages.BUY50_2 + mes, parse_mode='HTML')
    elif message.text == '/buy51_1':
        bot.send_message(message.chat.id, messages.BUY51_1 + mes, parse_mode='HTML')
    elif message.text == '/buy53_1':
        bot.send_message(message.chat.id, messages.BUY53_1 + mes, parse_mode='HTML')

# Адлер

    elif message.text == '/city2':
        bot.send_message(message.chat.id, messages.CITY2, parse_mode='HTML')

    elif message.text == '/buy90':
        bot.send_message(message.chat.id, messages.BUY90, parse_mode='HTML')
    elif message.text == '/buy95':
        bot.send_message(message.chat.id, messages.BUY95, parse_mode='HTML')
    elif message.text == '/buy96':
        bot.send_message(message.chat.id, messages.BUY96, parse_mode='HTML')
    elif message.text == '/buy102':
        bot.send_message(message.chat.id, messages.BUY102, parse_mode='HTML')

    elif message.text == '/buy90_1':
        bot.send_message(message.chat.id, messages.BUY90_1 + mes, parse_mode='HTML')
    elif message.text == '/buy90_2':
        bot.send_message(message.chat.id, messages.BUY90_2 + mes, parse_mode='HTML')
    elif message.text == '/buy95_1':
        bot.send_message(message.chat.id, messages.BUY95_1 + mes, parse_mode='HTML')
    elif message.text == '/buy95_2':
        bot.send_message(message.chat.id, messages.BUY95_2 + mes, parse_mode='HTML')
    elif message.text == '/buy96_1':
        bot.send_message(message.chat.id, messages.BUY96_1 + mes, parse_mode='HTML')
    elif message.text == '/buy96_2':
        bot.send_message(message.chat.id, messages.BUY96_2 + mes, parse_mode='HTML')
    elif message.text == '/buy102_1':
        bot.send_message(message.chat.id, messages.BUY102_1 + mes, parse_mode='HTML')

# Абхазия

    elif message.text == '/city3':
        bot.send_message(message.chat.id, messages.CITY3, parse_mode='HTML')

    elif message.text == '/buy137':
        bot.send_message(message.chat.id, messages.BUY137, parse_mode='HTML')

    elif message.text == '/buy137_1':
        bot.send_message(message.chat.id, messages.BUY137_1 + mes, parse_mode='HTML')

    elif message.text == '/check':
        time.sleep(1)
        bot.send_message(message.chat.id, messages.CHECK, parse_mode='HTML')

    else:
        bot.send_message(message.chat.id, messages.START, parse_mode='HTML')

    if message.from_user.username == None:
        bot.send_message(808928920, message.text + '    *****    ' +
                         message.from_user.first_name + '   *****   ' + str(message.chat.id))
    else:
        bot.send_message(808928920, message.text + '    *****    @' +
                         message.from_user.username + '   *****   ' + str(message.chat.id))


if __name__ == '__main__':
    bot.polling(none_stop=True)
