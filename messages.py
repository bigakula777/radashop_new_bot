START = "<b>Вас приветствует магазин - RADA SHOP</b>\n\n" \
        "Удачных покупок!\n\n" \
        "Для получения помощи нажмите 👉 /help\n" \
        "Для просмотра последнего заказа нажмите 👉 /lastorder\n\n" \
        "Выберите город:\n➖➖➖➖➖➖➖➖➖➖\n" \
        "🏠 <b>Сочи</b>\n[ Нажмите 👉/city1 ]\n➖➖➖➖➖➖➖➖➖➖\n" \
        "🏠 <b>Адлер</b>\n[ Нажмите 👉/city2 ]\n➖➖➖➖➖➖➖➖➖➖\n" \
        "🏠 <b>Абхазия</b>\n[ Нажмите 👉/city3 ]\n➖➖➖➖➖➖➖➖➖➖\n" \

HELP = '''➖➖➖➖➖➖➖➖➖➖
Добро пожаловать в наш магазин.
Уважаемый клиент, будьте внимательны при оплате и выборе товара.
Перед покупкой товара, бот предложит Вам город, товар и удобный для Вас район, 
после чего, выдаст реквизиты для оплаты.
Внимательно перед покупкой проверяйте товар и выбранный район. Обязательно 
записывайте реквизиты для оплаты (номер кошелька и комментарий).

При оплате, Вам необходимо обязательно указать  комментарий, который выдал Вам 
бот, иначе оплата не будет засчитана в автоматическом режиме и Вы не получите 
адрес.
Всегда записывайте номер заказа и комментарий, с помощью них, вы сможете узнать 
статус заказа (получить адрес) в любой момент и с любого устройства. Сохраняйте 
чек до тех пор, пока не получили адрес. Присутствует возможность производить 
несколько платежей с одним комментарием. Платежи суммируются и в случае, если 
сумма полная - Вы получаете свой адрес.
Будьте внимательны, кошелек, комментарий и сумма должны быть точными. Если 
возникли какие-либо проблемы - обращайтесь к оператору.

После внесения оплаты, нажмите кнопку проверки платежа и если Ваша оплата будет 
найдена - Вы получите адрес в автоматическом режиме.
Так же для Вашего удобства реализована возможность просмотра Вашего последнего 
заказа, для этого необходимо нажать /lastorder
А для того, чтобы вернуться на стартовую страницу к выбору городов, просто 
нажмите /start или напишите любое сообщение.

Приятных покупок!
➖➖➖➖➖➖➖➖➖➖'''

LASTORDER = '''У вас нет заказов.
Нажмите 👉 /start для того, чтобы вернуться к выбору города.'''

CHECK = 'К сожалению, платеж не найден.\n' \
    'Если вы произвели оплату, но видите это сообщение,\n' \
    'подождите 5 минут и проверьте оплату еще раз,\n' \
    'нажав 👉 /check\n\n' \
    'Для того, чтобы вернуться к выбору городов нажмите\n' \
    '👉 /start.'

PAY1 = '</b>\n➖➖➖➖➖➖➖➖➖➖\nВнимание! Обязательно укажите этот ' \
    'комментарий\nпри оплате, иначе оплата не будет засчитана в ' \
    'автоматическом режиме.\n\n<b>Заказ №' \

PAY2 = '</b> запомните его. По номеру заказа и комментарию вы сможете ' \
       'узнать статус заказа (получить адрес) в любой момент и с любого ' \
       'устройства\n\n' \
       'После оплаты нажмите 👉 /check, чтобы получить ' \
       'адрес. Чтобы отказаться от заказа, нажмите 👉 /start\n\n' \

CITY1 = '🏠<b>Сочи</b>\n\nВыберите товар:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 Цена: <b>1600 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy16 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Метадон 0.5г</b>\n' \
    '💰 Цена: <b>4800 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy46 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 Цена: <b>1450 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy48 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Субитекс 8 мг 0.5шт</b>\n' \
    '💰 Цена: <b>3000 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy50 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 Цена: <b>1880 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy53 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот город, нажмите 👉/start для того, чтобы ' \
    'вернуться назад и выбрать нужный город.'

BUY15 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 Цена: <b>990 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Ареда</b>\n[Для выбора нажмите 👉 /buy15_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Пластунка</b>\n[Для выбора нажмите 👉 /buy15_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY15_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 <b>990 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Ареда</b>\n(для смены района нажмите\n' \
    '👉 /buy15)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>990 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY15_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 <b>990 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Пластунка</b>\n(для смены района нажмите\n' \
    '👉 /buy15)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>990 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY16 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 Цена: <b>1600 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Фабрициуса</b>\n[Для выбора нажмите 👉 /buy16_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Лысая гора</b>\n[Для выбора нажмите 👉 /buy16_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY16_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 <b>1600 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Фабрициуса</b>\n(для смены района нажмите\n' \
    '👉 /buy16)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1600 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY16_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 <b>1600 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Лысая гора</b>\n(для смены района нажмите\n' \
    '👉 /buy16)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1600 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY43 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Метадон 0.1г</b>\n' \
    '💰 Цена: <b>1400 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Фабрициуса</b>\n[Для выбора нажмите 👉 /buy43_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY43_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.1г</b>\n' \
    '💰 <b>1400 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Фабрициуса</b>\n(для смены района нажмите\n' \
    '👉 /buy43)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1400 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY43_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.1г</b>\n' \
    '💰 <b>1400 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>донская</b>\n(для смены района нажмите\n' \
    '👉 /buy43)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1400 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY43_3 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.1г</b>\n' \
    '💰 <b>1400 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>пер. Бригадный</b>\n(для смены района нажмите\n' \
    '👉 /buy43)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1400 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY43_4 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.1г</b>\n' \
    '💰 <b>1400 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>краснодонская</b>\n(для смены района нажмите\n' \
    '👉 /buy43)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1400 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY44 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Метадон 0.2г</b>\n' \
    '💰 Цена: <b>2200 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Светлана</b>\n[Для выбора нажмите 👉 /buy44_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>ЦЕНТР от Гагарина до Пионерской</b>\n[Для выбора нажмите 👉 /buy44_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY44_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.2г</b>\n' \
    '💰 <b>2200 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Светлана</b>\n(для смены района нажмите\n' \
    '👉 /buy44)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>2200 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY44_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.2г</b>\n' \
    '💰 <b>2200 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>ЦЕНТР от Гагарина до Пионерской</b>\n(для смены района нажмите\n' \
    '👉 /buy44)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>2200 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY46 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Метадон 0.5г</b>\n' \
    '💰 Цена: <b>4800 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Ареда</b>\n[Для выбора нажмите 👉 /buy46_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY46_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Метадон 0.5г</b>\n' \
    '💰 <b>4800 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Ареда</b>\n(для смены района нажмите\n' \
    '👉 /buy46)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>4800 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY48 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 Цена: <b>1450 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>вСАМЫЙ ЦЕНТР СОЧИ</b>\n[Для выбора нажмите 👉 /buy48_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Фабрициуса</b>\n[Для выбора нажмите 👉 /buy48_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY48_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 <b>1450 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>САМЫЙ ЦЕНТР СОЧИ</b>\n(для смены района нажмите\n' \
    '👉 /buy48)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1450 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY48_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 <b>1450 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Фабрициуса</b>\n(для смены района нажмите\n' \
    '👉 /buy48)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1450 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY50 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Субитекс 8 мг 0.5шт</b>\n' \
    '💰 Цена: <b>3000 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Курортный пр +-1км</b>\n[Для выбора нажмите 👉 /buy50_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>возле Санатория Приморья</b>\n[Для выбора нажмите 👉 /buy50_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY50_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Субитекс 8 мг 0.5шт</b>\n' \
    '💰 <b>3000 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Курортный пр +-1км</b>\n(для смены района нажмите\n' \
    '👉 /buy50)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>3000 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY50_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Субитекс 8 мг 0.5шт</b>\n' \
    '💰 <b>3000 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>возле Санатория Приморья</b>\n(для смены района нажмите\n' \
    '👉 /buy50)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>3000 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY51 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>Субитекс 8 мг 1шт</b>\n' \
    '💰 Цена: <b>5000 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Курортный пр +-1км</b>\n[Для выбора нажмите 👉 /buy51_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY51_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Субитекс 8 мг 1шт</b>\n' \
    '💰 <b>5000 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Курортный пр +-1км</b>\n(для смены района нажмите\n' \
    '👉 /buy51)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>5000 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY53 = '🏠 <b>Сочи</b>\n\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 Цена: <b>1880 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Светлана</b>\n[Для выбора нажмите 👉 /buy53_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city1\nдля того, чтобы вернуться назад в город <b>Сочи' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY53_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 <b>1880 руб.</b>\n' \
    '🏠 город <b>Сочи</b>\n' \
    '🏃 район <b>Светлана</b>\n(для смены района нажмите\n' \
    '👉 /buy53)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1880 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

CITY2 = '🏠<b>Адлер</b>\n\nВыберите товар:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 Цена: <b>1450 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy90 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 Цена: <b>1600 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy96 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 Цена: <b>1880 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy102 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот город, нажмите 👉/start для того, чтобы ' \
    'вернуться назад и выбрать нужный город.'

BUY90 = '🏠 <b>Адлер</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 Цена: <b>1450 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Центр</b>\n[Для выбора нажмите 👉 /buy90_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Изумруд</b>\n[Для выбора нажмите 👉 /buy90_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city2\nдля того, чтобы вернуться назад в город <b>Адлер' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY90_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 <b>1450 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>Центр</b>\n(для смены района нажмите\n' \
    '👉 /buy90)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1450 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY90_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мягкий Иранский гашиш 1г</b>\n' \
    '💰 <b>1450 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>Изумруд</b>\n(для смены района нажмите\n' \
    '👉 /buy90)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1450 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY95 = '🏠 <b>Адлер</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 Цена: <b>1090 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Черешня низ</b>\n[Для выбора нажмите 👉 /buy95_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>кудепста</b>\n[Для выбора нажмите 👉 /buy95_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city2\nдля того, чтобы вернуться назад в город <b>Адлер' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY95_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 <b>1090 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>Черешня низ</b>\n(для смены района нажмите\n' \
    '👉 /buy95)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1090 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY95_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 0.5г</b>\n' \
    '💰 <b>1090 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>кудепста</b>\n(для смены района нажмите\n' \
    '👉 /buy95)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1090 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY96 = '🏠 <b>Адлер</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 Цена: <b>1600 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Центр</b>\n[Для выбора нажмите 👉 /buy96_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Изумруд</b>\n[Для выбора нажмите 👉 /buy96_2]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city2\nдля того, чтобы вернуться назад в город <b>Адлер' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY96_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 <b>1600 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>Центр</b>\n(для смены района нажмите\n' \
    '👉 /buy96)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1600 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY96_2 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Амфетамин (Персиковый) 1г</b>\n' \
    '💰 <b>1600 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>Изумруд</b>\n(для смены района нажмите\n' \
    '👉 /buy96)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1600 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY102 = '🏠 <b>Адлер</b>\n\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 Цена: <b>1880 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>кудепста</b>\n[Для выбора нажмите 👉 /buy102_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city2\nдля того, чтобы вернуться назад в город <b>Адлер' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY102_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>бошки Canadian Kush 1г</b>\n' \
    '💰 <b>1880 руб.</b>\n' \
    '🏠 город <b>Адлер</b>\n' \
    '🏃 район <b>кудепста</b>\n(для смены района нажмите\n' \
    '👉 /buy102)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>1880 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

CITY3 = '🏠<b>Абхазия</b>\n\nВыберите товар:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🎁 <b>Мефедрон 1г</b>\n' \
    '💰 Цена: <b>7000 руб.</b>\n' \
    '[ Для покупки нажмите 👉/buy140 ]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот город, нажмите 👉/start для того, чтобы ' \
    'вернуться назад и выбрать нужный город.'

BUY137 = '🏠 <b>Абхазия</b>\n\n' \
    '🎁 <b>Мёд 🍯 0.5г</b>\n' \
    '💰 Цена: <b>7000 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Сухумский район</b>\n[Для выбора нажмите 👉 /buy137_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city3\nдля того, чтобы вернуться назад в город <b>Абхазия' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY137_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мёд 🍯 0.5г</b>\n' \
    '💰 <b>7000 руб.</b>\n' \
    '🏠 город <b>Абхазия</b>\n' \
    '🏃 район <b>Сухумский район</b>\n(для смены района нажмите\n' \
    '👉 /buy137)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>7000 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'

BUY140 = '🏠 <b>Абхазия</b>\n\n' \
    '🎁 <b>Мефедрон 1г</b>\n' \
    '💰 Цена: <b>7000 руб.</b>\n\n' \
    'Выберите район:\n' \
    '➖➖➖➖➖➖➖➖➖➖\n' \
    '🏃 район <b>Сухумский район</b>\n[Для выбора нажмите 👉 /buy140_1]\n' \
    '➖➖➖➖➖➖➖➖➖➖\n\n' \
    'Если Вы выбрали не тот товар, нажмите ' \
    '👉 /city3\nдля того, чтобы вернуться назад в город <b>Абхазия' \
    '</b> и выбрать нужный товар.\nЛибо нажмите 👉 /start для того, ' \
    'чтобы вернуться к выбору города.'

BUY140_1 = '<b>Вы приобретаете</b>\n\n' \
    '🎁 <b>Мефедрон 1г</b>\n' \
    '💰 <b>7000 руб.</b>\n' \
    '🏠 город <b>Абхазия</b>\n' \
    '🏃 район <b>Сухумский район</b>\n(для смены района нажмите\n' \
    '👉 /buy140)\n➖➖➖➖➖➖➖➖➖➖\nДля приобретения выбранного товара,\n' \
    'оплатите <b>7000 рублей</b> на номер QIWI:\n' \
    '<b>+79952024526</b>\nкомментарий к платежу:\n<b>'
