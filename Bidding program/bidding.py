# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
answer = "yes"
bids = {}
while answer == 'yes':

    Name = input("What is your name? ")
    bid = int(input("How much would you like to bid? $"))
    bids |= {Name: bid}
    print(bids)
    answer = input("Are there any other bidders? \n")
    print("\n" * 100)
highest_person = ""
highest_bid = 0
for responses in bids:
    if bids[responses] > highest_bid:
        highest_bid = bids[responses]
        highest_person = responses
    else :
        highest_bid = bids[responses]

print(f"The winner is {highest_person} with a bid of ${highest_bid}")


