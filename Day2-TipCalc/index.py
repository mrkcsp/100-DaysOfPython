bill = int(input("Quanto è il conto? "))
perc = int(input("Che percentuale di mancia vuoi/volete lasciare? "))
people = int(input("In quanti volete dividere il conto? "))

total_bill = bill + (bill*perc/100)

rounded_tot_for_person = round(total_bill/people)

rounded_with_two_decimal = round(total_bill/people, 2)


print(f"Il totale per persona è {rounded_with_two_decimal}")

print(f"Il totale per persona arrotondato è {rounded_tot_for_person}")
