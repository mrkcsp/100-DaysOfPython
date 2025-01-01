number = int(input("Inserisci un numero: "))

modulo = number % 2

if modulo != 0:
    print(f"Il numero {number} è dispari")
else:
    print(f"Il numero {number} è pari")


############################################################################

height = int(input("Quanto sei alto in cm? "))
bill = 0
if height >= 120:
    print("Puoi passare!")
    age = int(input("Quanti anni hai? "))
    if age >= 45 and age <= 55:
    #if 45 >= age <= 55:  #another way
        print("Non devi pagare la corsa")
        bill = 0
    elif age >= 18:
        print("Puoi pagare 12 euro")
        bill = 12
    elif age <= 12: 
        print("Puoi pagare 5 euro")
        bill = 5
    else:
        print("Puoi pagare 7 euro")
        bill = 7 

    wants_photo = input("Vuoi fare una foto? Indica con 's' per SI e con 'n' per NO: ")
    if(wants_photo == "s"):
        bill += 3

    print(f"Il totale del biglietto è di {bill} euro!") 
else:
    print(f"Mi spiace, ma non puoi passare se sei alto {height}")

############################################################################

print("Benvenuti al Python Pizza Deliveries!")

size = input("Di che misura vorresti la pizza? S, M, L, XL: ")
pepperoni = input("Vorresti dei pepperoni sulla tua pizza? S o N: ")
extra_cheese = input("Vorresti del formaggio extra? S o N: ")
bill = 0

if size == "S":
    bill += 3
elif size == "M":
    bill += 5
elif size == "L":
    bill += 8
elif size == "XL":
    bill += 12
else:
    print("Hai scelto una misura che non c'è...")

if pepperoni == "S":
    if size == "S":
        bill += 1.5
    else:
        bill += 2
if extra_cheese == "S":
    if size == "S":
        bill += 2
    else:
        bill += 3

print(f"Il totale per la tua pizza è di {bill} euro!")

############################################################################

