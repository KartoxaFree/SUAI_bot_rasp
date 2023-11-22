import sys
import os

from bot_settings import bot
import function
import random_students
import frazi


def send_msg(chat_id, st):
    bot.send_message(chat_id, st)


def send_random_students(message):
    students = random_students.get_random_list(message.chat.id)
    bot.send_message(message.chat.id, students)


def create_file_group(message):
    f = ""
    filename = "Name"
    folder_path = "students" + "/" + str(message.chat.id)

    try:
        file_path = os.path.join(str(folder_path), filename)

        f = open(file_path, 'r', encoding='utf-8')
        f.close()
        return "Группа уже создана"

    except FileNotFoundError:
        # Получаем список администраторов чата
        administrators = bot.get_chat_administrators(message.chat.id)

        # Формируем строку с именами и фамилиями администраторов
        admins_list = "\n".join(
            [f"{admin.user.first_name} {admin.user.last_name}" if admin.user.last_name else admin.user.first_name for
             admin in administrators])

        # Создаем директорию, если она не существует
        os.makedirs(folder_path, exist_ok=True)
        # Полный путь к файлу
        file_path = os.path.join(folder_path, filename)

        # Открываем файл для записи
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(admins_list)

        return frazi.complite_create_gruop

    except Exception as e:
        function.write_log(f"Произошла ошибка: {type(e).__name__}: {e}")
        return frazi.er_global
