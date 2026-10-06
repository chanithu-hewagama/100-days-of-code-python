def percent(x, y):
    return (x / 100) * y
def main():
    print("Welcome to te tip calculator!")
    bill = float(input("What was the total bill? $"))
    tipPercent = float(input("How much tip would you like to give? "))
    split = int(input("How many people to split the bill?"))
    print(f"each person should pay: ${round((percent(tipPercent, bill) + bill) / split, 2)}")

if __name__ == "__main__":
    main()
    