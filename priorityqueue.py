#priority queue
students_grade=[]
students_grade.append((1,"A"))
students_grade.append((4,"B"))
students_grade.sort(reverse=True)
print("yes")
print(students_grade)
students_grade.append((3,"c"))
students_grade.sort(reverse=True)
students_grade.append((2,"D"))
students_grade.sort(reverse=True)
print("Priority wise sorted")
print("original queue")
while students_grade:
    print(students_grade.pop())