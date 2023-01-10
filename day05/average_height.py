# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)
total_height = 0

for height in student_heights:
    total_height += height
print(total_height)

total_length = 0
for length in student_heights:
    length = 1
    total_length += length
print(total_length)

average_height = round(total_height/total_length)
print("The average height for the list you proved is " +  str(average_height))
