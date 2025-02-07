def show_even_numbers(x, y):
    print(f"Even numbers from {x} to {y}:")
    for num in range(x, y + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print("\n")

def show_odd_numbers(x, y):
    print(f"Odd numbers from {x} to {y}:")
    for num in range(x, y + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print("\n")

def show_squares(x, y):
    print(f"Squares of numbers from {x} to {y}:")
    for num in range(x, y + 1):
        print(num ** 2, end=" ")
    print("\n")

def main():
    print("Welcome to the Number Sequence Generator!")
    x = int(input("Enter the starting number (x): "))
    y = int(input("Enter the ending number (y): "))

    while True:
        print("\nMenu:")
        print("1. Show the even numbers from x to y")
        print("2. Show the odd numbers from x to y")
        print("3. Show the squares of the numbers from x to y")
        print("4. Exit the program")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_even_numbers(x, y)
        elif choice == '2':
            show_odd_numbers(x, y)
        elif choice == '3':
            show_squares(x, y)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()