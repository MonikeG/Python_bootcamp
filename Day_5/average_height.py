'''You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164'''




# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height
print (f'total height = {total_height}')

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(f'number of students = {number_of_student}')

average_height = round(total_height/number_of_student)
print(average_height)


    #adicionar cada elemento e dividir por quantas vezes foi adicionado

