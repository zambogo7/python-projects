from auction_ascii import logo

import os
clear = lambda:os.system('cls')


bid={}

bid_finished=False

def find_heighest_bider(bidding_record):
    heighest_bid=0
    winner=""
    for bidder in bidding_record:
        bidding_amount=bidding_record[bidder]
        if bidding_amount>heighest_bid:
            heighest_bid=bidding_amount
            winner=bidder
    print(f"the winner is {winner} who has ${heighest_bid}")


while not bid_finished:
    name=input("Enter your name")
    price=int(input("Enter the amount"))
    bid[name]=price

    another_one=input("are there other people to bid? Type 'yes' or 'no'").lower()
    if another_one=="no":
        bid_finished=True
    elif another_one=="yes":
        clear()
    find_heighest_bider(bid)


