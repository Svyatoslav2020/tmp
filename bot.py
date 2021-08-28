import telebot

bot = telebot.TeleBot('1984184464:AAErugPa5Io_0KzTXOMAyoQb5_0pHrIIpA4')


@bot.message_handler(content_types=['text'])
def send_message(message):
    f = open(message.text)
    bot.send_document(575335047, f)
    f.close()

bot.polling(none_stop=True)
