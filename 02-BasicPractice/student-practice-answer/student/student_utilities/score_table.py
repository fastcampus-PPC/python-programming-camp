import operator


def student_sortby_keyword(students, keyword, rank, reverse=False):
    return sorted(students, key=operator.attrgetter(keyword), reverse=reverse)[:rank]


def student_sortby_average(students, rank, reverse=False):
    return sorted(students, key=lambda item: item.korean + item.mathematics + item.english, reverse=reverse)[:rank]

    ### sorting for custom attributes
    # return sorted(students, key=lambda item: (item.korean, item.mathematics, item.english), reverse=reverse)[:rank]


def print_score_table(students):
    for idx, student in enumerate(students):
        print(idx+1, "등 : ", student.name, ", ", student.grade)
        print("KOR : ", student.korean, ", ", "MATH : ", student.mathematics, ", ", "ENG : ", student.english)
        print("average : ", round(((student.korean + student.mathematics + student.english) / 3), 2))