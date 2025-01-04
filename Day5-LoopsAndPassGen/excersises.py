fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

###########################################################################

student_scores = [78,56,26,54,45,89,67,1,15,31,54,12,34,95,76,18,7,6,64,1,8,10,70,61]

total_exam_score = sum(student_scores)
print(total_exam_score)

# OR

sum = 0
for score in student_scores:
    sum += score

print(sum)

###########################################################################

print(max(student_scores))

# OR

max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score

print(max_score)

###########################################################################

#RANGE

for number in range(1, 10):  # not including 10
    print(number)

for number in range(1, 10, 2):  # step by 2
    print(number)


#GAUSS
total = 0
for number in range(1, 101):
    total += number

print(total)

###########################################################################
#FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)