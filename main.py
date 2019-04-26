# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
import wolframalpha

reply_keyboard = [['/zontik', '/perevod', '/pogoda'],
                  ['/kartinka', '/dobratsa', '/apteka']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


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
        alll = {'английский': 'en', 'русский': 'ru', 'абхазский': 'ab', 'арабский'
        : 'ar', 'азербайджанский': 'az', 'армянский': 'hy', 'башкирский': 'ba', 'белорусский': 'be',
                'болгарский': 'bg',
                'венгерский': 'hu', 'вьетнамский': 'vi', 'грузинский': 'ka', 'датский': 'da', 'иврит': 'he',
                'испанский': 'es', 'итальянский': 'it', 'немецкий': 'de', 'корейский': 'ko', 'японский': 'ja',
                'португальский': 'pt'}
        if lang in alll.keys():
            return alll[lang]
        return None


helpp = Helper()


def urawn(bot, update, args):
    client = wolframalpha.Client('Y2J834-KHE8APQ9HU')
    res = client.query(' '.join(args))
    answer = next(res.results).text
    update.message.reply_text(answer)


def start(bot, update):
    pass


def zontik(bot, update):
    print(0)
    adressa = update.message.text.split()[1:]
    adress = helpp.get_coords(adressa).split()
    print(adress)
    api_forecast = 'https://api.weather.yandex.ru/v1/forecast?'
    params = {'lat': adress[0], 'lon': adress[1], 'lang': 'ru_RU',
              'X-Yandex-API-Key': 'e43cb430-0dd4-481d-884e-8423a36a6d9a'}
    response = requests.get(api_forecast, params=params)
    print(response.content)


def perevod(bot, update):
    from_trans = update.message.text.split()[1]
    to_trans = update.message.text.split()[2]
    words = update.message.text.split()[3:]
    if helpp.get_language(from_trans) is not None:
        if helpp.get_language(to_trans) is not None:
            from_trans = helpp.get_language(from_trans)
            to_trans = helpp.get_language(to_trans)
            translator_uri = \
                "https://translate.yandex.net/api/v1.5/tr.json/translate"
            response = requests.get(
                translator_uri,
                params={
                    "key":
                        "trnsl.1.1.20190421T150726Z.fe7b6a8c58b8788e.422cda1d99bc4cbed5fd2685e0f4f423a6ec5eda",
                    "lang": "{}-{}".format(from_trans, to_trans),
                    # То, что нужно перевести.
                    "text": ' '.join(words)
                })
            update.message.reply_text(
                " ".join(response.json()["text"]))
        else:
            update.message.reply_text('Я не знаю такого языка: {}'.format(to_trans))
    else:
        update.message.reply_text('Я не знаю такого языка: {}'.format(from_trans))


def pogoda(bot, update):
    # погода
    city = update.message.text.split()[1:]
    api_weather = 'https://api.weather.yandex.ru/v1/informers?'
    cords = helpp.get_coords(city).split()
    params = {'lat': cords[0], 'lon': cords[1], 'lang': 'ru_RU'}
    response = requests.get(api_weather, params=params)
    update.message.reply_text("Я Бот-помощник для ДЭБИЛ. Что вам нужно?",
                              reply_markup=markup)


def kartinka(bot, update):
    find = update.message.text.split()[1:]
    translator_uri = \
        "https://translate.yandex.net/api/v1.5/tr.json/translate"
    response = requests.get(
        translator_uri,
        params={
            "key":
            # Ключ, который надо получить по ссылке в тексте.
                "trnsl.1.1.20190421T150726Z.fe7b6a8c58b8788e.422cda1d99bc4cbed5fd2685e0f4f423a6ec5eda",
            # Направление перевода: с русского на английский.
            "lang": "ru-en",
            # То, что нужно перевести.
            "text": find
        })
    text = ''.join(response.json()['text'])
    update.message.reply_text('Вот то, что вы искали ' +
                              'https://www.google.ru/search?q=' + text + '&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X')


def dobratsa(bot, update):
    pass


def apteka(bot, update):
    pass


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
    dp.add_handler(CommandHandler("zontik", zontik))
    dp.add_handler(CommandHandler("perevod", perevod))
    dp.add_handler(CommandHandler("pogoda", pogoda))
    dp.add_handler(CommandHandler("kartinka", kartinka))
    dp.add_handler(CommandHandler("dobratsa", dobratsa))
    dp.add_handler(CommandHandler("apteka", apteka))
    dp.add_handler(CommandHandler("urawn", urawn, pass_args=True))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
