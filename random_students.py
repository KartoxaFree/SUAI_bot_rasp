import random
import os

import frazi


def select(list_students, out_list, n):
    for i in range(n):
        if out_list[i] == "":
            selected_student = random.randint(0, len(list_students) - 1)
            out_list[i] = list_students[selected_student]
            list_students.pop(selected_student)


def output(list):
    st = ""
    for i in range(len(list)):
        st += str(i) + ". " + str(list[i])
        st += '\n'

    return st


def remove_cheaters(list_st, end_list):
    for i in end_list:
        if i != "":
            list_st.remove(i)
    return list_st


def get_random_list(group_id):
    try:
        filename = "Name"
        folder_path = "students" + "/" + str(group_id)

        file_path = os.path.join(folder_path, filename)

        file = open(file_path, 'r', encoding='utf-8')

        st_out = []
        for line in file:
            st_out.append(line.strip())


    except FileNotFoundError:
        return frazi.er_not_group
    except Exception as e:
        print(f"Произошла ошибка: {type(e).__name__}: {e}")

        return frazi.er_global

    students_1 = st_out

    students_end_1 = []
    for i in range(len(students_1)):
        students_end_1.append("")

    n1 = len(students_1)

    students_1 = remove_cheaters(students_1, students_end_1)
    select(students_1, students_end_1, n1)

    return output(students_end_1)