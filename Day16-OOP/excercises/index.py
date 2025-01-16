#import turtle

#timmy = turtle.Turtle()

# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100.00)
# timmy.circle(100)
# timmy.back(200.00)


# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()

##################################################

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("POKEMON NAME", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("TYPE", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)