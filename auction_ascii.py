logo='''
                  _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                    
'''

bids={}
is_bidding_finished=False
while not is_bidding_finished:
    name=input("Enter your name: ")
    bid=input("Enter your bid: $")
    bids[name]=bid
    should_continue=input("is there any person whishing to bid in the aunction type 'yes' or 'no' ").lower()
    if should_continue=="no":
        is_bidding_finished=True



    
    print(bids)

