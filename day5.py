import random
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'j', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passwd = []


def main():
    password = ""
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    if not nr_letters == 0:
        for i in range(1, nr_letters + 1):
            passwd.append(letters[random.randint(0, len(letters) - 1)])
    if not nr_symbols == 0:
        for i in range(1, nr_symbols + 1):
            passwd.append(symbols[random.randint(0, len(symbols) - 1)])
    if not nr_numbers == 0:
        for i in range(1, nr_numbers + 1):
            passwd.append(numbers[random.randint(0, len(numbers) - 1)])
    random.shuffle(passwd)
    for i in passwd:
        password = f"{password}{i}"
    print(f"Your password is: {password}")
