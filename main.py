# Modules
from os import system
from art import logo

print(logo)

bids = {}
bidding_finished = False

# Defining function
def find_highest_bidder(bidding_record):
  # bidding_record = {"Hussain": 300, "Ali": 600, "Alex": 100}
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What's your name?: ")
  price =  int(input("What's your bid?: $"))
  # Adding them into a dictionary
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    system('cls')
    find_highest_bidder(bids)
  elif should_continue == "yes":
    # Clear console on cmd in Windows
    system('cls')