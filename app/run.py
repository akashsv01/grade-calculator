

from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Weights object
weights = GradeWeights()

# Set grades achieved so far
"""Below is the method to manually input the grades from the student

    my_grades.quiz_1 = float(input("Enter your grade in Quiz 1 [from 0.0-1.0]: "))
    my_grades.quiz_2 = float(input("Enter your grade in Quiz 2 [from 0.0-1.0]: "))
    my_grades.midterm = float(input("Enter your grade in Midterm [from 0.0-1.0]: "))
    my_grades.project = float(input("Enter your grade in project [from 0.0-1.0]: "))
    my_grades.final = float(input("Enter your grade in the Final exam [from 0.0-1.0]: "))
"""

# Getting the grades from the file directly
grades = Grades.load_grades_from_json("app\\grades_exams.json")
# Print object 
print("Grades object: " + str(grades)) 

# Convert object back to JSON 
print("JSON of the Grades object: " + grades.model_dump_json())

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')