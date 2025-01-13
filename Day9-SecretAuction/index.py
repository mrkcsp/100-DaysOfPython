bids = {}

def bid_system():
    name = ""
    while name == "" or name in bids:
        name = input("What's your name?:  ")
        if name == "" or name in bids:
            print("Please insert another name! Anonimity is admitted, blank or duplicate name's not")
    bid = 0
    while bid < 1:
        bid= int(input("What's your bid?:  "))
        if bid < 1:
            print("The bid cannot be under 1 dollar")
    bids[name] = bid
    print("\n" * 50)
    
    
def who_wins():
    print("Calculating...")
    


more_bis = True

while more_bis:
    bid_system()
    choice = input("More bids? 'yes' or 'no':  ")
    if choice.lower() != "yes":
        more_bis = False

who_wins()

print("Congrats!")