import random 
import my_module

############################## RANDOM MODULE ##############################

random_integer = random.randint(1, 10)

print(f"Random int 1 to 10 {random_integer}")

###########################################################################

print(my_module.my_fav_number)

###########################################################################

random_num_0_to_1 = random.random() * 10

print(random_num_0_to_1)

###########################################################################

random_float = random.uniform(1, 10)

print(random_float)

###########################################################################

gen_random = random.randint(0, 1)

if gen_random == 0:
    print("Heads")
else:
    print("Tails")


############################### PYTHON LIST ###############################

states = ["Pennsylvenia", "Delaware", "Ohio", "Virginia"]

print(states[1])

states.append("Maryland")

print(states[-1])

states.extend(["Washington ", "Denver"])

print(states)

############################### RANDOMIZED BILL PAY ###############################

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#to avoid IndexError:   
friends_max_lenght = len(friends) - 1

# option 1
who_pays = random.randint(0, friends_max_lenght)
print(friends[who_pays])

# option 2
print(random.choice(friends))

############################### Nested List ###############################

dirty_dozen = [states, friends]

print(dirty_dozen)
