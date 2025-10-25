# def add(*args):
#     return print(sum(args))

def add(*args):
    total = 0
    for n in args:
        total += n
    return print(total)

add(1, 2, 3, 4, 5)

#unlimited keyword arguments
# def calculate(**kwargs):
#     #dictionary
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)

#     print(kwargs['add'])
#     print(kwargs['multiply'])

# calculate(add=3, multiply=5)


def calculate(n, **kwargs):
    #dictionary
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    return print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']
        self.color = kw.get('color') #if color is not provided, it will return None instead of error
        self.seats = kw.get('seats')

my_car = Car(make="Nissan", model="GT-R", seats=2)
print(my_car.model)