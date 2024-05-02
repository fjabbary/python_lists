# ======================================================== 
# =================|| Task 1 - subtask 1 ||===============
# ======================================================== 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# ======================================================== 
# =================|| Task 1 - subtask 2 ||===============
# ======================================================== 
# We can loop through the list and calculate sum, or we can use built-in function called sum()
sum = 0
number_of_elements = len(grades)

for item in grades:
  sum += item
average = sum / number_of_elements
print("Average is :", average)


# ======================================================== 
# =================|| Task 2 - subtask 1 ||===============
# ======================================================== 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

students_submitted_and_attended = []

for item in submitted:
  if item in attended:
    students_submitted_and_attended.append(item)
print(students_submitted_and_attended)    


# ======================================================== 
# =================|| Task 3 - subtask 1 ||===============
# ======================================================== 
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14:]
print(second_week)


# ======================================================== 
# =================|| Task 3 - subtask 2 ||===============
# ======================================================== 
temperatures_over_100 = [];
for temperature in temperatures:
  if temperature > 100:
    temperatures_over_100.append(temperature)
    
print(temperatures_over_100)    
