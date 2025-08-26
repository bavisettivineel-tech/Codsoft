import string
import random

def password_generator():
    length = int(input("Enter Password length you want: "))

    # password complexity
    print("\nSelect complexity level:")
    print("\n1.- Lower case only!\n2.- Letters (Uppercase + Lowercase)"
          "\n3.- Letters + Digits\n4.- Letters + Digits + Symbols")
    complexity = int(input("Enter your choice (1-4): "))

    if complexity == 1:
        char_pool = string.ascii_lowercase  # lowercase
    elif complexity == 2:
        char_pool = string.ascii_letters  # upper and lower
    elif complexity == 3:
        char_pool = string.ascii_letters + string.digits
    elif complexity == 4:
        char_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid choice, defaulting to lower case!")
        char_pool = string.ascii_lowercase

    password = ''.join(random.choice(char_pool) for _ in range(length))
    print("Generated password is: ", password)

def main():
    while True:
        password_generator()
        again = input("Do you want to create another password? (yes/no): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()


