import random as r 
def main():
    val = bool(r.randint(0, 1))
    if val:
        print("Heads")
    else:
        print("Tails")

if __name__ == "__main__":
    main()