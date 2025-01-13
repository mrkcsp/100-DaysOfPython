#dictionaries
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
       student_grades[student] = "Outstanding"
    elif student_scores[student] >= 81:
       student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
       student_grades[student] = "Acceptable"
    elif student_scores[student] < 71:
       student_grades[student] = "Fail"


print(student_grades)


########################################################

capitals = {
   "France": "Paris",
   "Germany": "Berlin"
}

travel_log = {
   "France": ["Paris", "Lile", "Dijon"],
   "Germany": ["Stuttgart", "Berlin"]
}

#print "Lile"

print(travel_log["France"][1])

########################################################

#print C
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][0])

########################################################
#print "Berlin"

travel_log_nested = {
   "France": {
      "total_visits": 13,
      "cities_visited": ["Paris", "Lile", "Dijon"]
   },
   "Germany": {
      "total_visits": 5,
      "cities_visited": ["Stuttgart", "Berlin", "Hamburg"]
      }
}

print(travel_log_nested["Germany"]["cities_visited"][2])