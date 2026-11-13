logo = """
                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
"""

people = {}

def main():

    print(logo)

    while True:
        curr_name = input("What is your name?: ")
        bid = input("What is your bid: $")
        if input("Are there any other bidders? Type \'yes\' or \'no\'.\n").lower() == "yes":
            people[curr_name] = bid
            print("\n" * 100)
            continue
        else:
            break
    highest_bid = 0
    highest_bidder = ""
    for i in people:
        if people[i] > highest_bid:
            highest_bid = people[i]
            highest_bidder = i
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

if __name__ == '__main__':
    main()