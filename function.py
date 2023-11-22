import os
from datetime import datetime

import doit
import edit_mode_function
import frazi
from bot_settings import bot

user_states = {}

users_id = []


# Определение состояний
class State:
    edit_group = 1
    create_group = 2
    join_group = 3
    edit_mode = 4


def write_log(st):
    print(st)

    folder_path = "admin"
    filename = "Log"

    # Получаем текущую дату и время
    current_datetime = datetime.now()
    # Преобразуем в строку
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def_write_file(folder_path, filename, f"{formatted_datetime} {st}", "a")


def del_file(folder_path, filename):
    folder_path = str(folder_path)
    filename = str(filename)

    try:
        file_path = os.path.join(folder_path, filename)

        st = read_file(folder_path, filename)
        def_write_file("backup", "_" + filename, st + "\n\n", "a")

        os.remove(file_path)
    except FileNotFoundError:
        pass
    except Exception as e:
        write_log(f"Произошла ошибка: {type(e).__name__}: {e}")


def read_file(folder_path, filename):
    folder_path = str(folder_path)
    filename = str(filename)

    st = ""
    try:
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем файл построчно
            for line in file:
                st += line.strip() + "\n"  # strip() используется для удаления символа новой строки

        return st
    except FileNotFoundError:
        return None
    except Exception as e:
        write_log(f"Произошла ошибка: {type(e).__name__}: {e}")


def def_write_file(folder_path, filename, st, type_work):
    folder_path = str(folder_path)
    filename = str(filename)
    st = str(st)

    try:
        # Создаем директорию, если она не существует
        os.makedirs(folder_path, exist_ok=True)

        # Полный путь к файлу
        file_path = os.path.join(folder_path, filename)

        # Открываем файл для записи
        with open(file_path, type_work, encoding='utf-8') as file:
            file.write(f"{st}\n")  # Ваш код для записи в файл

    except Exception as e:
        print(f"Произошла ошибка: {type(e).__name__}: {e}")


# переписывает нужный параметр не удаляя содержимое файла
def condition_write_file(folder_path, filename, st, type_work):
    folder_path = str(folder_path)
    filename = str(filename)
    st = str(st)
    stroka = []

    try:
        # Создаем директорию, если она не существует
        os.makedirs(folder_path, exist_ok=True)

        # Полный путь к файлу
        file_path = os.path.join(folder_path, filename)

        if type_work == "a":
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Читаем файл построчно
                    for line in file:
                        if line.strip().split(":")[0] != st.split(":")[0]:
                            stroka.append(line.strip())
            except FileNotFoundError:
                pass
            except Exception as e:
                write_log(f"Произошла ошибка: {type(e).__name__}: {e}")

        # Открываем файл для записи
        with open(file_path, "w", encoding='utf-8') as file:
            for i in stroka:
                file.write(i + "\n")
            if st.split(":")[1] != "":
                file.write(f"{st}\n")  # Ваш код для записи в файл

    except Exception as e:
        write_log(f"Произошла ошибка: {type(e).__name__}: {e}")


# поиск заданного параметра
def search_param(folder_path, filename, param):
    folder_path = str(folder_path)
    filename = str(filename)

    file_path = os.path.join(folder_path, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем файл построчно
            for line in file:
                ln = line.strip()
                if ln.split(":")[0] == param.split(":")[0]:
                    return ln.split(":")[1]

    except FileNotFoundError:
        return None
    except Exception as e:
        write_log(f"Произошла ошибка: {type(e).__name__}: {e}")
        return None

    return None


def obrabotchik(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # обработчик сообщений
    write_log(f"{chat_id} {user_id} {message.text}")

    # крысятничем
    if not str(user_id) in users_id:
        def_write_file("admin", "Users_id", user_id, "a")
        def_write_file("admin", "Users_name", message.from_user.first_name, "a")
        users_id.append(str(user_id))

    # команды админа
    if user_id == 1369533759:
        match message.text:
            case "/return_0":
                print(1 / 0)
            case "/info":
                bot.send_message(chat_id, frazi.hello_group)
            case "/create":
                doit.create_file_group(message)
            case "/spam":
                for i in range(25):
                    link_text = "Нажми на меня"
                    link_url = "https://www.example.com/youtu.be/dQw4w9WgXcQ?list=PLNTK9welGzDynukDlMqLGqY3rlaMPOJOl"  # Замените на вашу ссылку
                    hyperlink = f"[{link_text}]({link_url})"
                    bot.send_message(1369533759, f"{hyperlink}", parse_mode="Markdown")

    if int(chat_id) < 0:
        match message.text:
            case "/generate_random_list":
                doit.send_random_students(message)
            case "/get_id":
                doit.send_msg(chat_id, str(chat_id))
            case "/rickroll":
                for i in range(25):
                    link_text = "Нажми на меня"
                    link_url = "https://www.example.com/youtu.be/dQw4w9WgXcQ?list=PLNTK9welGzDynukDlMqLGqY3rlaMPOJOl"  # Замените на вашу ссылку
                    hyperlink = f"[{link_text}]({link_url})"
                    bot.send_message(user_id, f"{hyperlink}", parse_mode="Markdown")

    else:
        if user_states.get(chat_id, None) is None:
            match message.text:
                case "/rickroll":
                    for i in range(25):
                        link_text = "Нажми на меня"
                        link_url = "https://www.example.com/_youtu.be/dQw4w9WgXcQ?list=PLNTK9welGzDynukDlMqLGqY3rlaMPOJOl"  # Замените на вашу ссылку
                        hyperlink = f"[{link_text}]({link_url})"
                        bot.send_message(user_id, f"{hyperlink}", parse_mode="Markdown")
                case "/start":
                    doit.send_msg(chat_id, frazi.start)
                case "/help":
                    doit.send_msg(chat_id, frazi.help)
                    # voice_message = open('asd.mp3', 'rb')  # Замените путь к файлу на свой
                    # bot.send_voice(user_id, voice_message)
                    print()
                case "/edit_chat":
                    user_states[user_id] = State.edit_group
                    doit.send_msg(message.chat.id, frazi.indo_for_edit)
                case "/create_group":
                    user_states[user_id] = State.create_group
                    doit.send_msg(message.chat.id, frazi.create_group)
                    doit.send_msg(message.chat.id, "Введите номер группы")
                case "/delete_group":
                    del_file("groups", search_param("users", user_id, "Group"))
                    condition_write_file("users", user_id, "Group:", "a")
                    bot.send_message(user_id, "Группа удалена, для buckup обратитесь к модераторам")
                case "/join_group":
                    user_states[user_id] = State.join_group
                    doit.send_msg(message.chat.id, "Введите номер группы")
                case "/edit_group":
                    if search_param("users", user_id, "Group") is not None:
                        doit.send_msg(message.chat.id, "Вы вошли в режим редактирования" + frazi.for_exit)
                        doit.send_msg(message.chat.id, frazi.rules_edit_mode)
                        user_states[user_id] = State.edit_mode
                    else:
                        doit.send_msg(message.chat.id, "У вас нет управляемой группы")
        else:
            # машина состояний
            state = user_states.get(user_id, None)
            text = str(message.text)

            if text != "/exit":
                # запоминание группы
                match state:
                    case State.edit_group:
                        if text[0] == "-" and text.count("-") == 1 and text[1:-1].isdigit():
                            condition_write_file("users", user_id, "Edit_group:" + text, "a")
                            bot.send_message(user_id, "Спасибо за участие в программе, ваши данные записаны в память")
                            user_states[user_id] = None
                        else:
                            bot.send_message(user_id, "Неправильные данные" + frazi.for_exit)

                    case State.create_group:
                        if text == "/starosta":
                            bot.send_message(user_id, "Жалоба оставлена")
                            def_write_file("admin", "er", str(user_id), "a")
                            user_states[user_id] = None
                            return

                        if text == "/delete_group":
                            del_file("groups", search_param("users", user_id, "Group"))
                            condition_write_file("users", user_id, "Group:", "a")
                            bot.send_message(user_id, "Группа удалена, для buckup обратитесь к модераторам")
                            user_states[user_id] = None
                            return

                        if search_param("users", user_id, "Group"):
                            bot.send_message(user_id, frazi.warring_del_group)
                        else:
                            if read_file("groups", text) is None:
                                condition_write_file("groups", text, "Owner:" + str(user_id), "a")
                                condition_write_file("users", user_id, "Group:" + text, "a")
                                bot.send_message(user_id, "Группа создана")
                                user_states[user_id] = None
                            else:
                                bot.send_message(user_id, "Группа с таким именем уже существует\n"
                                                          "Если вы являетесь старостой напишите /starosta и ожидайте ответа")

                    case State.join_group:
                        if read_file("groups", text) is None:
                            bot.send_message(user_id, "Такой группы не существует" + frazi.for_exit)
                        else:
                            condition_write_file("users", user_id, "Tracking_group:" + text, "a")
                            bot.send_message(user_id, "Вы вступили в группу: " + text)
                            user_states[user_id] = None

                    case State.edit_mode:
                        if text == "/help":
                            doit.send_msg(message.chat.id, frazi.rules_edit_mode)
                        elif edit_mode_function.check_rasp(text):
                            bot.send_message(user_id, "Пары успешно добавленны")
                        else:
                            bot.send_message(user_id,
                                             "Неверный формат\nНапишите /help для просмотра примера заполнения")

            else:
                bot.send_message(user_id, "Выход: Успешно")
                user_states[user_id] = None
