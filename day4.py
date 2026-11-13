import random as r

def nl():
    print("\n")
def main():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)

    '''
    player = int(input('''
    Rock Paper scissors
    Type 0 for Rock, 1 for Paper & 2 for Scissors.
    '''))
    prngai = r.randint(0, 2)
    states = ["You Win", "You Lose.", "Draw."]
    n1 = states[2]
    n2 = states[1]
    n3 = states[0]
    n4 = states[2]
    possible_ends = [[0,0], [0, 1], [1, 0], [1, 1], [2, 2], [2, 1], [0, 2]]
    result = [n1, n2, n3, n4, n1, n2, n3]
    current_art = [rock, paper, scissors]
    status = result[possible_ends.index([player, prngai])]
    nl()
    print(current_art[player])
    nl()
    print("Computer Chose: ")
    nl()
    print(current_art[prngai])
    nl()
    print(status)

if __name__ == "__main__":
    main()
