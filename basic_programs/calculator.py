"""
A Python program that computes a grade-point average (GPA).
"""

points = {"A": 4.0, "A-": 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

num_course = 0
total_point = 0
done = False

while not done:
    grade = input()
    if grade == '':  # empty line was entered
        done = True
    elif grade not in points:
        print("Unrecognised grade {0} being ignored".format(grade))
    else:
        num_course = num_course + 1
        total_point = total_point + points[grade]

if num_course > 0:
    print("Your CGPA is {0:.3}".format(total_point / num_course))
