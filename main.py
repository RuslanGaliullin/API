# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import random
import webbrowser

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


def start(bot, update):
    webbrowser.open_new_tab(
        'https://www.google.ru/search?q=' + 'flag lgbt' + '&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X')
    update.message.reply_text("Я Бот-помощник для игр. Что вам нужно?",
                              reply_markup=markup)


def dice(bot, update):
    update.message.reply_text("Вы выбрали dice.",
                              reply_markup=markup_dice)


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
