import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

fl = len(friends) - 1

def main():
    print(friends[random.randint(0, fl)])

if __name__ == "__main__":
    main()