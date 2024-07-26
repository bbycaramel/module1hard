# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)

average_grade = {} #pustoy dict
for student, grades_list in zip(sorted_students, grades):
    average_grade[student] = sum(grades_list) / len(grades_list)
print(average_grade)

