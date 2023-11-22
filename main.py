import bot_settings
import function


@bot_settings.bot.message_handler(content_types=['text'])
def get_text_messages(message):
    function.obrabotchik(message)


function.users_id = function.read_file("admin", "Users_id").split("\n")


bot_settings.bot.polling(none_stop=True, interval=0)