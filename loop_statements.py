# =================|| Task 1 ||===========================
# ======================================================== 
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in range(len(days_of_week)):
  random_mood = random.choice(moods)
  print(f"On {days_of_week[day]}, you were feeling {random_mood}")

print("====================================================")
print("================|| Task 2 ||========================")



# =================|| Task 2 ||===========================
# ======================================================== 
time_of_the_day = ["morning", "afternoon", "evening"]
moods = ["happy", "tired", "sad", "calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days_of_week:
  for time in time_of_the_day:
    mood = random.choice(moods)
    print(f"On {day} {time} you were {mood}")