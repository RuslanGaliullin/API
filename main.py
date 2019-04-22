# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
import random

reply_keyboard = [['/dice'],
                  ['/timer']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_dice = [['/RollOneDie', '/RollTwoDie'],
                       ['/RollMegaDie', '/back']]
markup_dice = ReplyKeyboardMarkup(reply_keyboard_dice, one_time_keyboard=False)

reply_keyboard_timer = [['/30sec', '/minute'],
                        ['/5min', '/back']]
markup_timer = ReplyKeyboardMarkup(reply_keyboard_timer, one_time_keyboard=False)

reply_keyboard_close = [['/close']]
markup_close = ReplyKeyboardMarkup(reply_keyboard_close, one_time_keyboard=False)


class Helper:
    def get_coords(self, adress):
        try:
            address = adress
            # Собираем параметры для запроса к StaticMapsAPI:
            map_api_server = "http://geocode-maps.yandex.ru/1.x/"

            map_params = {"geocode": address, "format": "json"}
            response_metro = requests.get(map_api_server, params=map_params)
            json_response = response_metro.json()

            # Получаем первый топоним из ответа геокодера.
            # Согласно описанию ответа, он находится по следующему пути:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            # Полный адрес топонима:
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            # Координаты центра топонима:
            toponym_coodrinates = toponym["Point"]["pos"]
            return toponym_coodrinates  # строка
        except:
            print('ошибочка')

    def get_language(self, lang):
        if lang in all.keys():
            all = {'английский': 'en', 'русский': 'ru', 'абхазский': 'ab', 'арабский'
            : 'ar', 'азербайджанский': 'az', 'армянский': 'hy', 'башкирский': 'ba', 'белорусский': 'be', 'болгарский': 'bg',
                   'венгерский': 'hu', 'вьетнамский': 'vi', 'грузинский': 'ka', 'датский': 'da', 'иврит': 'he',
                   'испанский': 'es', 'итальянский': 'it', 'немецкий': 'de', 'корейский': 'ko', 'японский': 'ja',
                   'португальский': 'pt'}
            return all[lang]
        return 'Я не знаю такой язык'


helpp = Helper()


def start(bot, update, city):
    # погода
    api_weather = 'https://api.weather.yandex.ru/v1/informers'
    cords = helpp.get_coords(city).split()
    params = {'lat': cords[0], 'lon': cords[1], 'lang': 'ru_RU'}
    response = requests.get(api_weather, params=params)
    update.message.reply_text("Я Бот-помощник для игр. Что вам нужно?",
                              reply_markup=markup)


def dice(bot, update, phrase, lang):
    # переводчик
    api_translation = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {'key': 'trnsl.1.1.20190421T150726Z.fe7b6a8c58b8788e.422cda1d99bc4cbed5fd2685e0f4f423a6ec5eda',
              'text': phrase, 'lang': helpp.get_language(lang)+'_'+helpp.get_language(lang).upper()}
    response = requests.get(api_translation, params=params)
    update.message.reply_text(
        "\n\n".join([response.json()["text"][0]]))


def RollOneDie(bot, update):
    update.message.reply_text(random.randint(1, 6))


def RollTwoDie(bot, update):
    update.message.reply_text('{0} {1}'.format(random.randint(1, 6), random.randint(1, 6)))


def RollMegaDie(bot, update):
    update.message.reply_text(random.randint(1, 20))


def back(bot, update):
    update.message.reply_text("Вы вышли в главное меню.", reply_markup=markup)


def timer(bot, update):
    update.message.reply_text("Вы выбрали timer.",
                              reply_markup=markup_timer)


def close(bot, update, chat_data):
    # Проверяем, что задача ставилась
    # (вот зачем нужно было ее записать в chat_data).
    print('ssds')
    if 'job' in chat_data:
        # планируем удаление задачи (выполнется, когда будет возможность)
        chat_data['job'].schedule_removal()
        # и очищаем пользовательские данные
        del chat_data['job']
    update.message.reply_text('Таймер сброшен', reply_markup=markup_timer)


def task30(bot, job):
    bot.send_message(job.context, text='30 секунд истекло')


def tri_sec(bot, update, job_queue, chat_data):
    # создаём задачу task в очереди job_queue через 20 секунд
    # передаём ей идентификатор текущего чата
    # (будет доступен через job.context)
    delay = 30  # секунд
    job = job_queue.run_once(task30, delay, context=update.message.chat_id)
    # Запоминаем в пользовательских данных созданную задачу.
    chat_data['job'] = job
    # Присылаем сообщение о том, что всё получилось.
    update.message.reply_text('засек 30 секунд', reply_markup=markup_close)


def task60(bot, job):
    bot.send_message(job.context, text='минута истекла')


def min_sec(bot, update, job_queue, chat_data):
    # создаём задачу task в очереди job_queue через 20 секунд
    # передаём ей идентификатор текущего чата
    # (будет доступен через job.context)
    delay = 60  # секунд
    job = job_queue.run_once(task30, delay, context=update.message.chat_id)
    # Запоминаем в пользовательских данных созданную задачу.
    chat_data['job'] = job
    # Присылаем сообщение о том, что всё получилось.
    update.message.reply_text('засек минуту', reply_markup=markup_close)


def task300(bot, job):
    bot.send_message(job.context, text='5 минут истекло')


def five_min_sec(bot, update, job_queue, chat_data):
    # создаём задачу task в очереди job_queue через 20 секунд
    # передаём ей идентификатор текущего чата
    # (будет доступен через job.context)
    delay = 300  # секунд
    job = job_queue.run_once(task300, delay, context=update.message.chat_id)
    # Запоминаем в пользовательских данных созданную задачу.
    chat_data['job'] = job
    # Присылаем сообщение о том, что всё получилось.
    update.message.reply_text('засек 5 минут', reply_markup=markup_close)


def main():
    # Создаём объект updater. Вместо слова "TOKEN" надо разместить
    # полученный от @BotFather токен
    updater = Updater("879379687:AAHXkIj5tPSCi7zlJaGH6fHAhoz_y-q88EU")
    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере эта функция
    # будет вызываться при получении сообщения с типом "текст",
    # т.е. текстовых сообщений.
    # Зарегистрируем их в диспетчере.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("RollOneDie", RollOneDie))
    dp.add_handler(CommandHandler("RollTwoDie", RollTwoDie))
    dp.add_handler(CommandHandler("RollMegaDie", RollMegaDie))
    dp.add_handler(CommandHandler("back", back))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(CommandHandler("30sec", tri_sec,
                                  pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("minute", min_sec,
                                  pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("5min", five_min_sec,
                                  pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("close", close, pass_chat_data=True))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
