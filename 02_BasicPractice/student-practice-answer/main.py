from student.student import Student
from student.student_utilities.grade_map import GradeMap
import student.student_utilities.score_table as score_table


if __name__ == "__main__":
    mymap = GradeMap.instance()

    dict_list = [(14, "중1"), (15, "중2"), (16, "중3"), (17, "고1"), (18, "고2"), (19, "고3")]
    for item in dict_list:
        mymap.setitem(item[0], item[1])

    nayeon = Student(19, "나연", 88, 70, 67)
    dahyun = Student(17, "다현", 94, 94, 90)
    sana = Student(18, "사나", 58, 75, 70)
    momo = Student(15, "모모", 58, 90, 87)
    tzuyu = Student(16, "쯔위", 50, 98, 92)

    student_list = [nayeon, dahyun, sana, momo, tzuyu]
    sorted_student_list = score_table.student_sortby_keyword(student_list, 'age', rank=5, reverse=False)
    score_table.print_score_table(sorted_student_list)

    sorted_student_list = score_table.student_sortby_average(student_list, rank=5, reverse=True)
    score_table.print_score_table(sorted_student_list)