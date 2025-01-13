def my_function(f_name, l_name):
    #docstring
    '''
    gets first and last name and format it to return the 
    title case version of the full name
    '''
    full_name = f"{f_name} {l_name}"
    return full_name.title()

names = my_function("mike", "almo")
print(names)


############################################################

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
    
print(is_leap_year(2100))
print(is_leap_year(2000))


############################################################

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)