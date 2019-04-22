# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
import random

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
            return all[lang]
        return 'Я не знаю такой язык'


helpp = Helper()


def start(bot, update, city):
    # погода
    api_weather = 'https://api.weather.yandex.ru/v1/informers?'
    cords = helpp.get_coords(city).split()
    params = {'lat': cords[0], 'lon': cords[1], 'lang': 'ru_RU'}
    response = requests.get(api_weather, params=params)
    update.message.reply_text("Я Бот-помощник для ДЭБИЛ. Что вам нужно?",
                              reply_markup=markup)


def zontik(bot, update):
    pass


def perevod(bot, update):
    pass


def pogoda(bot, update):
    pass


def kartinka(bot, update):
    pass


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
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
