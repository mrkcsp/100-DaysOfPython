#GLobal scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside the function: {enemies}")

    
print(f"Enemies outside the function: {enemies}")


#Local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()


######################################################################

#Is Prime

def is_prime( num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    #Exclude numbers that can be divided by 2 and 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    #searched hard :')
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

check = is_prime(73)