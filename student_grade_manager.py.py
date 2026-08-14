print("===== STUDENT GRADE MANAGER =====")

name = input("Enter your name:")
math = float(input("Enter your Math score:"))
python = float(input("enter your Python score:"))
english = float(input("Enter your English score:"))

average = (math + python + english) / 3

passing_score = 75
passed = average >= passing_score

print("\n===== STUDENT RESULTS =====")
print("Student name:", name)
print("Math score:", math)
print("Python score:", python)
print("Engish score:", english)
print("Average:", round(average, 2))
print("Passing score:", passing_score)
print("did the student pass?", "True" if passed else "False")
