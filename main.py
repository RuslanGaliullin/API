from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler


def echo(bot, update):
    update.message.reply_text('Привет, это телешоу. Для начала игры напишите /start_cities')


class Cities:
    def start(bot, update):
        update.message.reply_text(
            "Привет. Пройдите небольшой опрос, пожалуйста!\n"
            "Вы можете прервать опрос, послав команду /stop.\n"
            "В каком городе вы живёте?")

        # Число-ключ в словаре states —
        # втором параметре ConversationHandler'а.
        return 1
        # Оно указывает, что дальше на сообщения
        # от этого пользователя должен отвечать обработчик states[1].
        # До этого момента обработчиков текстовых сообщений
        # для этого пользователя не существовало,
        # поэтому текстовые сообщения игнорировались.

    def first_response(bot, update):
        # Это ответ на первый вопрос.
        # Мы можем использовать его во втором вопросе.
        locality = update.message.text
        update.message.reply_text(
            "Какая погода в городе {locality}?".format(**locals()))
        # Следующее текстовое сообщение
        # будет обработано обработчиком states[2]
        return 2

    def second_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def third_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def fourth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def fivth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def sixth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def seventh_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def eighth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def ninth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def tenth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def stop(bot, update):
        update.message.reply_text(
            "Жаль. А было бы интерсно пообщаться. Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога

    def end(self):
        return ConversationHandler.END


class Sights:
    def start(bot, update):
        update.message.reply_text(
            "Привет. Пройдите небольшой опрос, пожалуйста!\n"
            "Вы можете прервать опрос, послав команду /stop.\n"
            "В каком городе вы живёте?")

        # Число-ключ в словаре states —
        # втором параметре ConversationHandler'а.
        return 1
        # Оно указывает, что дальше на сообщения
        # от этого пользователя должен отвечать обработчик states[1].
        # До этого момента обработчиков текстовых сообщений
        # для этого пользователя не существовало,
        # поэтому текстовые сообщения игнорировались.

    def first_response(bot, update):
        # Это ответ на первый вопрос.
        # Мы можем использовать его во втором вопросе.
        locality = update.message.text
        update.message.reply_text(
            "Какая погода в городе {locality}?".format(**locals()))
        # Следующее текстовое сообщение
        # будет обработано обработчиком states[2]
        return 2

    def second_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def third_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def fourth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def fivth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def sixth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def seventh_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def eighth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def ninth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def tenth_response(bot, update):
        # Ответ на второй вопрос. Мы можем его сохранить
        # в базе данных или переслать куда-либо.
        weather = update.message.text
        update.message.reply_text(
            "Спасибо за участие в опросе! Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога.
        # Все обработчики из states и fallbacks становятся неактивными.

    def stop(bot, update):
        update.message.reply_text(
            "Жаль. А было бы интерсно пообщаться. Всего доброго!")
        return ConversationHandler.END  # Константа, означающая конец диалога

    def end(self):
        return ConversationHandler.END


def main():
    # Создаём объект updater. Вместо слова "TOKEN" надо разместить
    # полученный от @BotFather токен
    updater = Updater("TOKEN")

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере эта функция
    # будет вызываться при получении сообщения с типом "текст",
    # т.е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    city_game = Cities
    sight_game = Sights

    conv_handler_cities = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start_game_cities', city_game.start)],

        # Состояние внутри диалога. Вариант с двумя обработчиками,
        # фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, city_game.first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text, city_game.second_response)],
            3: [MessageHandler(Filters.text, city_game.third_response)],
            4: [MessageHandler(Filters.text, city_game.fourth_response)],
            5: [MessageHandler(Filters.text, city_game.fivth_response)],
            6: [MessageHandler(Filters.text, city_game.sixth_response)],
            7: [MessageHandler(Filters.text, city_game.second_response)],
            8: [MessageHandler(Filters.text, city_game.eighth_response)],
            9: [MessageHandler(Filters.text, city_game.ninth_response)],
            10: [MessageHandler(Filters.text, city_game.tenth_response)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop_game_cities', city_game.stop)]
    )
    conv_handler_sights = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start_game_sights', sight_game.start)],

        # Состояние внутри диалога. Вариант с двумя обработчиками,
        # фильтрующими текстовые сообщения.
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text, sight_game.first_response)],
            # Функция читает ответ на второй вопрос и завершает диалог.
            2: [MessageHandler(Filters.text, sight_game.second_response)],
            3: [MessageHandler(Filters.text, sight_game.third_response)],
            4: [MessageHandler(Filters.text, sight_game.fourth_response)],
            5: [MessageHandler(Filters.text, sight_game.fivth_response)],
            6: [MessageHandler(Filters.text, sight_game.sixth_response)],
            7: [MessageHandler(Filters.text, sight_game.second_response)],
            8: [MessageHandler(Filters.text, sight_game.eighth_response)],
            9: [MessageHandler(Filters.text, sight_game.ninth_response)],
            10: [MessageHandler(Filters.text, sight_game.tenth_response)]
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop_game_sights', sight_game.stop)]
    )

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
