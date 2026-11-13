import random
numbers = [random.randint(1, random.randint(1, 1000000000000000000000)) for _ in range(10)]

def main():
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    print(f"Custom max(): {largest}, Inbuilt max(): {max(numbers)}.")

if __name__ == "__main__":
    main()