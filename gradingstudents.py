# If the difference between the grade and the next multiple of 5 is less than 3
# round  up to the next multiple of 5.
# If the value is less than 40, no rounding occurs as the result will still be a failing grade.


def gradingStudents(grades):
    final_grades = []
    for elem in grades:
        dec = elem // 10 
        unid = elem % 10
        redond = elem

        if unid > 5:
            redond = dec * 10 + 10
        if unid < 5:
            redond = dec * 10 + 5

        if redond - elem < 3 and elem > 37:

            final_grades.append(redond)
        else:
            final_grades.append(elem)

    return final_grades


if __name__ == '__main__':
    print(gradingStudents([25, 38, 43, 55, 61])) # 25, 40, 45, 55, 61 