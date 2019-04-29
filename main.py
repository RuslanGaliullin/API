# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
import wolframalpha
import wikipedia
import pymorphy2
import ssl

reply_keyboard = [['/zontik', '/perevod', '/pogoda', '/info'],
                  ['/kartinka', '/dobratsa', '/apteka', '/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def help(bot, update):
    update.message.reply_text("/zontik - функция показывающая прогноз погоды")


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
    update.message.reply_text("Привет! Я бот помощник для учебы. Список команд доступен по /help",
                              reply_markup=markup)


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


# def pogoda(bot, update):
#    # погода
#    city = update.message.text.split()[1:]
#    api_weather = 'https://api.weather.yandex.ru/v1/informers?'
#    cords = helpp.get_coords(city).split()
#    params = {'lat': cords[0], 'lon': cords[1], 'lang': 'ru_RU'}
#    response = requests.get(api_weather, params=params)
#    update.message.reply_text("Я Бот-помощник для ДЭБИЛ. Что вам нужно?",
#                              reply_markup=markup)


def kartinka(bot, update, chat_data):
    update.message.reply_text('Какая картинка вас интересует?')
    chat_data['kartinka'] = 1


def info(bot, update, chat_data):
    update.message.reply_text('Что вас интересует?')
    chat_data['wiki'] = 1


def priem(bot, update, chat_data):
    if 'kartinka' in chat_data:
        print(1)
        find = update.message.text
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
        del chat_data['kartinka']
    elif 'wiki' in chat_data:
        wikipedia.set_lang("ru")
        translator_uri = \
            "https://translate.yandex.net/api/v1.5/tr.json/translate"
        response = requests.get(
            translator_uri,
            params={
                "key":
                    "trnsl.1.1.20190421T150726Z.fe7b6a8c58b8788e.422cda1d99bc4cbed5fd2685e0f4f423a6ec5eda",
                "lang": 'ru-en',
                # То, что нужно перевести.
                "text": ' '.join(update.message.text.split()[1:])
            })
        asking = " ".join(response.json()["text"])
        update.message.reply_text(wikipedia.summary(asking, sentences=1))
        del chat_data['wiki']
    elif 'word' in chat_data:
        try:
            word = update.message.text.split()[0]
            morph = pymorphy2.MorphAnalyzer()
            chosen = morph.parse(word)[1]
            print('Часть речи: ', chosen.tag.POS,
                  'Одушивленность: ', chosen.tag.animacy,
                  'Bид: ', chosen.tag.aspect,
                  'Падеж: ', chosen.tag.case,
                  'Род: ', chosen.tag.gender,
                  'Лицо: ', chosen.tag.person,
                  'Время: ', chosen.tag.tense)
            if chosen.tag.POS == 'NOUN':
                update.message.reply_text(
                    'Часть речи: ' + chosen.tag.POS + '\n' + 'Одушивленность: ' + chosen.tag.animacy + '\n' + 'Падеж: ' + chosen.tag.case + '\n' + 'Род: ' + chosen.tag.gender)
            elif chosen.tag.POS == 'INFN':
                update.message.reply_text(
                    'Часть речи: ' + chosen.tag.POS + '\n' + 'Bид: ' + chosen.tag.aspect)
            elif chosen.tag.POS == 'VERB':
                update.message.reply_text(
                    'Часть речи: ' + chosen.tag.POS + '\n' + 'Bид: ' + chosen.tag.aspect + '\n' + 'Род: ' + chosen.tag.gender + '\n' + 'Время: ' + chosen.tag.tense)
            elif chosen.tag.POS == 'ADVB' or chosen.tag.POS == 'INTJ':
                update.message.reply_text('Часть речи: ' + chosen.tag.POS)
            else:
                update.message.reply_text('Неизвестное слово')
        except Exception as e:
            update.message.reply_text(e)
        del chat_data['word']
    else:
        update.message.reply_text('Вы не выбрали никакой функции')


def word(bot, update, chat_data):
    update.message.reply_text('Какое слово вас интересует?')
    chat_data['word'] = 1


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
    text_handler = MessageHandler(Filters.text, priem, pass_chat_data=True)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("word", word, pass_chat_data=True))
    dp.add_handler(CommandHandler("perevod", perevod, pass_chat_data=True))
    dp.add_handler(CommandHandler("kartinka", kartinka, pass_chat_data=True))
    dp.add_handler(CommandHandler("info", info, pass_chat_data=True))
    dp.add_handler(CommandHandler("urawn", urawn, pass_args=True))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()
    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
