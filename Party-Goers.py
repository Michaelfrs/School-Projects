import random
def main():
    partyGoers = 4
    party_food = ["chips", "soda", "salsa dip", 'veggie tray', "cake", "salad", "charcuterie board", "stuffed mushrooms"]
    for i in range(partyGoers):
        item1 = random.randint(0, party_food)
        item2 = random.randint(0, len(party_food))
        
        item1 = party_food[item1]
        party_food.remove(item1)
        
        item2 = party_food[item2]
        party_food.add(item2)
        
        print("person", i+1, "needs to bring:", item1, "&", item2)

main()
    