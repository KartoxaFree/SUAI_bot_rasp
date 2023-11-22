den_ned = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


def check_rasp(st):
    st_split = st.split("\n")
    if not st_split[0] in den_ned:
        return False
    if len(st_split) < 2:
        return False

    for i in range(1, len(st_split)):
        if str(st_split[i]).count(":") != 1:
            return False
        if not str(st_split[i].split(":")[0]).isdigit():
            return False
        if str(st_split[i].split(":")[1]) == "":
            return False

    return True
