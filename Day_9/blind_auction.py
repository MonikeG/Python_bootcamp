logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


import os

def ask (self):
    name = input("Your name is?: ")
    bid = input("What is your bid?: $")
    accumulation(name,bid)
    print(all_bid)
   
    


print ("This is The Secret Auction Program")
print(logo) 

bids ={}
bidding_finish = False

def find_high_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finish:
    name = input("Your name is?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    keep_going = input('Anyone else would like to bid? ')
    if keep_going == "no":
        bidding_finish = True
        find_high_bid(bids)
    elif keep_going == 'yes':
        os.system('cls')



    

