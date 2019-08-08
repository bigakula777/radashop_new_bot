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
    elif message.text == '/buy47':
        bot.send_message(message.chat.id, messages.BUY47, parse_mode='HTML')
    elif message.text == '/buy48':
        bot.send_message(message.chat.id, messages.BUY48, parse_mode='HTML')
    elif message.text == '/buy50':
        bot.send_message(message.chat.id, messages.BUY50, parse_mode='HTML')
    elif message.text == '/buy51':
        bot.send_message(message.chat.id, messages.BUY51, parse_mode='HTML')
    elif message.text == '/buy53':
        bot.send_message(message.chat.id, messages.BUY53, parse_mode='HTML')
    elif message.text == '/buy57':
        bot.send_message(message.chat.id, messages.BUY57, parse_mode='HTML')
    elif message.text == '/buy58':
        bot.send_message(message.chat.id, messages.BUY58, parse_mode='HTML')

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
    elif message.text == '/buy43_2':
        bot.send_message(message.chat.id, messages.BUY43_2 + mes, parse_mode='HTML')
    elif message.text == '/buy44_1':
        bot.send_message(message.chat.id, messages.BUY44_1 + mes, parse_mode='HTML')
    elif message.text == '/buy44_2':
        bot.send_message(message.chat.id, messages.BUY44_2 + mes, parse_mode='HTML')
    elif message.text == '/buy44_3':
        bot.send_message(message.chat.id, messages.BUY44_3 + mes, parse_mode='HTML')
    elif message.text == '/buy44_4':
        bot.send_message(message.chat.id, messages.BUY44_4 + mes, parse_mode='HTML')
    elif message.text == '/buy46_1':
        bot.send_message(message.chat.id, messages.BUY46_1 + mes, parse_mode='HTML')
    elif message.text == '/buy47_1':
        bot.send_message(message.chat.id, messages.BUY47_1 + mes, parse_mode='HTML')
    elif message.text == '/buy48_1':
        bot.send_message(message.chat.id, messages.BUY48_1 + mes, parse_mode='HTML')
    elif message.text == '/buy48_2':
        bot.send_message(message.chat.id, messages.BUY48_2 + mes, parse_mode='HTML')
    elif message.text == '/buy50_1':
        bot.send_message(message.chat.id, messages.BUY50_1 + mes, parse_mode='HTML')
    elif message.text == '/buy51_1':
        bot.send_message(message.chat.id, messages.BUY51_1 + mes, parse_mode='HTML')
    elif message.text == '/buy53_1':
        bot.send_message(message.chat.id, messages.BUY53_1 + mes, parse_mode='HTML')
    elif message.text == '/buy57_1':
        bot.send_message(message.chat.id, messages.BUY57_1 + mes, parse_mode='HTML')
    elif message.text == '/buy57_2':
        bot.send_message(message.chat.id, messages.BUY57_2 + mes, parse_mode='HTML')
    elif message.text == '/buy58_1':
        bot.send_message(message.chat.id, messages.BUY58_1 + mes, parse_mode='HTML')
    elif message.text == '/buy58_2':
        bot.send_message(message.chat.id, messages.BUY58_2 + mes, parse_mode='HTML')

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
    elif message.text == '/buy105':
        bot.send_message(message.chat.id, messages.BUY105, parse_mode='HTML')
    elif message.text == '/buy106':
        bot.send_message(message.chat.id, messages.BUY106, parse_mode='HTML')
    elif message.text == '/buy108':
        bot.send_message(message.chat.id, messages.BUY108, parse_mode='HTML')
    elif message.text == '/buy109':
        bot.send_message(message.chat.id, messages.BUY109, parse_mode='HTML')
    elif message.text == '/buy111':
        bot.send_message(message.chat.id, messages.BUY111, parse_mode='HTML')
    elif message.text == '/buy112':
        bot.send_message(message.chat.id, messages.BUY112, parse_mode='HTML')
    elif message.text == '/buy115':
        bot.send_message(message.chat.id, messages.BUY115, parse_mode='HTML')
    elif message.text == '/buy120':
        bot.send_message(message.chat.id, messages.BUY120, parse_mode='HTML')

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
    elif message.text == '/buy105_1':
        bot.send_message(message.chat.id, messages.BUY105_1 + mes, parse_mode='HTML')
    elif message.text == '/buy105_2':
        bot.send_message(message.chat.id, messages.BUY105_2 + mes, parse_mode='HTML')
    elif message.text == '/buy106_1':
        bot.send_message(message.chat.id, messages.BUY106_1 + mes, parse_mode='HTML')
    elif message.text == '/buy108_1':
        bot.send_message(message.chat.id, messages.BUY108_1 + mes, parse_mode='HTML')
    elif message.text == '/buy109_1':
        bot.send_message(message.chat.id, messages.BUY109_1 + mes, parse_mode='HTML')
    elif message.text == '/buy111_1':
        bot.send_message(message.chat.id, messages.BUY111_1 + mes, parse_mode='HTML')
    elif message.text == '/buy112_1':
        bot.send_message(message.chat.id, messages.BUY112_1 + mes, parse_mode='HTML')
    elif message.text == '/buy115_1':
        bot.send_message(message.chat.id, messages.BUY115_1 + mes, parse_mode='HTML')
    elif message.text == '/buy120_1':
        bot.send_message(message.chat.id, messages.BUY120_1 + mes, parse_mode='HTML')

# Абхазия

    elif message.text == '/city3':
        bot.send_message(message.chat.id, messages.CITY3, parse_mode='HTML')

    elif message.text == '/buy137':
        bot.send_message(message.chat.id, messages.BUY137, parse_mode='HTML')
    elif message.text == '/buy140':
        bot.send_message(message.chat.id, messages.BUY140, parse_mode='HTML')

    elif message.text == '/buy137_1':
        bot.send_message(message.chat.id, messages.BUY137_1 + mes, parse_mode='HTML')
    elif message.text == '/buy140_1':
        bot.send_message(message.chat.id, messages.BUY140_1 + mes, parse_mode='HTML')
    elif message.text == '/buy141_1':
        bot.send_message(message.chat.id, messages.BUY141_1 + mes, parse_mode='HTML')
    elif message.text == '/buy141_2':
        bot.send_message(message.chat.id, messages.BUY141_2 + mes, parse_mode='HTML')

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
